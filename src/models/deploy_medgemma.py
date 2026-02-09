"""
Deploy MedGemma 27B to Vertex AI Endpoint.

This script checks if a MedGemma endpoint already exists and creates one if not.
It then deploys the MedGemma 27B model to the endpoint.

Usage:
    python src/models/deploy_medgemma.py [--dry-run] [--region REGION]
    
Environment Variables:
    GOOGLE_CLOUD_PROJECT: GCP project ID
    MEDGEMMA_ENDPOINT_ID: (optional) Existing endpoint ID to use
"""

import os
import sys
import argparse
import subprocess
import json
from pathlib import Path
import dotenv
dotenv.load_dotenv()

# Configuration
DEFAULT_REGION = os.getenv("GOOGLE_CLOUD_LOCATION", "eu-west1")
MODEL_ID = "google/medgemma-27b-it"  # 27B instruction-tuned
MACHINE_TYPE = "g2-standard-48"  # Recommended for 27B model
ACCELERATOR_TYPE = "NVIDIA_L4"
ACCELERATOR_COUNT = 4  # 27B needs multiple GPUs
ENDPOINT_DISPLAY_NAME = "medgemma-27b-endpoint"
DEPLOYED_MODEL_DISPLAY_NAME = "medgemma-27b"

def run_command(cmd: list[str], capture_output: bool = True, check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command and return the result."""
    print(f"  - Running: {' '.join(cmd)}")
    return subprocess.run(cmd, capture_output=capture_output, text=True, check=check)


def get_project_id() -> str:
    """Get the current GCP project ID."""
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        result = run_command(["gcloud", "config", "get-value", "project"])
        project_id = result.stdout.strip()
    if not project_id:
        print("ERROR: Could not determine GCP project ID.")
        print("Set GOOGLE_CLOUD_PROJECT or run: gcloud config set project YOUR_PROJECT")
        sys.exit(1)
    return project_id


def enable_required_services(project_id: str) -> None:
    """Enable necessary GCP services."""
    services = [
        "serviceusage.googleapis.com",
        "cloudquotas.googleapis.com",
        "aiplatform.googleapis.com"
    ]
    print(f"\nChecking enabled services...")
    for service in services:
        print(f"  - Enabling {service}...")
        # running synchronously to ensure they are ready
        subprocess.run(
            ["gcloud", "services", "enable", service, "--project", project_id],
            check=False  # Don't crash if already enabled or permission denied (user might see error later)
        )


def check_endpoint_exists(project_id: str, region: str, endpoint_id: str = None) -> dict | None:
    """Check if a MedGemma endpoint already exists."""
    if endpoint_id:
        # Check specific endpoint by ID
        try:
            result = run_command([
                "gcloud", "ai", "endpoints", "describe", endpoint_id,
                "--project", project_id,
                "--region", region,
                "--format", "json"
            ])
            return json.loads(result.stdout)
        except subprocess.CalledProcessError:
            return None
    
    # Search for endpoint by display name
    try:
        result = run_command([
            "gcloud", "ai", "endpoints", "list",
            "--project", project_id,
            "--region", region,
            "--filter", f'displayName="{ENDPOINT_DISPLAY_NAME}"',
            "--format", "json"
        ])
        endpoints = json.loads(result.stdout)
        if endpoints:
            return endpoints[0]
    except subprocess.CalledProcessError:
        pass
    
    return None

def check_model_deployed(project_id: str, region: str, endpoint_id: str) -> bool:
    """Check if MedGemma is already deployed to the endpoint."""
    try:
        result = run_command([
            "gcloud", "ai", "endpoints", "describe", endpoint_id,
            "--project", project_id,
            "--region", region,
            "--format", "json"
        ])
        endpoint_data = json.loads(result.stdout)
        deployed_models = endpoint_data.get("deployedModels", [])
        
        for model in deployed_models:
            if "medgemma" in model.get("displayName", "").lower():
                return True
        
        return False
    except subprocess.CalledProcessError:
        return False


def deploy_model(project_id: str, region: str, dry_run: bool = False) -> str | None:
    """Deploy MedGemma 27B - gcloud creates the endpoint automatically."""
    print(f"\nDeploying {MODEL_ID}")
    print(f"   Machine: {MACHINE_TYPE}")
    print(f"   Accelerator: {ACCELERATOR_COUNT}x {ACCELERATOR_TYPE}")
    
    # gcloud ai model-garden models deploy creates endpoint automatically
    # Syntax: --model=publisher/model@version
    # MedGemma format: google/medgemma@medgemma-27b-text-it
    model_spec = "google/medgemma@medgemma-27b-text-it"
    
    cmd = [
        "gcloud", "ai", "model-garden", "models", "deploy",
        f"--model={model_spec}",
        "--project", project_id,
        "--billing-project", project_id,  # Set quota project
        "--region", region,
        "--machine-type", MACHINE_TYPE,
        "--accelerator-type", ACCELERATOR_TYPE,
        "--accelerator-count", str(ACCELERATOR_COUNT),
        "--endpoint-display-name", ENDPOINT_DISPLAY_NAME,
        "--accept-eula",  # Auto-accept license
    ]
    
    if dry_run:
        print(f"  [DRY RUN] Would run: {' '.join(cmd)}")
        return "DRY_RUN_ENDPOINT_ID"
    
    print("  This may take 10-20 minutes...")
    result = run_command(cmd, capture_output=False, check=False)
    
    if result.returncode != 0:
        print(f"\nERROR: Deployment failed. Check the error above.")
        print("\nAlternative: Deploy via Cloud Console:")
        print("  1. Go to: https://console.cloud.google.com/vertex-ai/model-garden")
        print(f"  2. Search for 'MedGemma'")
        print("  3. Click 'Deploy' and follow the wizard")
        return None
    
    print(f"\nMedGemma 27B deployed successfully!")
    return None  # Endpoint ID will be in output

def main():
    parser = argparse.ArgumentParser(description="Deploy MedGemma 27B to Vertex AI")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without executing")
    parser.add_argument("--region", default=DEFAULT_REGION, help=f"GCP region (default: {DEFAULT_REGION})")
    parser.add_argument("--force-deploy", action="store_true", help="Deploy even if already deployed")
    args = parser.parse_args()
    
    print("=" * 60)
    print("MedGemma 27B Deployment Script")
    print("=" * 60)
    
    if args.dry_run:
        print("[DRY RUN MODE] - No changes will be made\n")
    
    # Get project ID
    project_id = get_project_id()
    print(f"Project: {project_id}")
    
    if not args.dry_run:
        enable_required_services(project_id)
        
    print(f"Region: {args.region}")
    
    # Check for existing endpoint with MedGemma
    existing_endpoint_id = os.getenv("MEDGEMMA_ENDPOINT_ID")
    if existing_endpoint_id:
        endpoint = check_endpoint_exists(project_id, args.region, existing_endpoint_id)
        if endpoint:
            endpoint_id = endpoint["name"].split("/")[-1]
            print(f"\nFound existing endpoint: {endpoint_id}")
            
            if check_model_deployed(project_id, args.region, endpoint_id):
                if not args.force_deploy:
                    print(f"MedGemma already deployed to endpoint!")
                    print("\nYour .env is correctly configured:")
                    print(f"   MEDGEMMA_ENDPOINT_ID={endpoint_id}")
                    return
                print("  (--force-deploy specified, will redeploy)")
    
    # Deploy the model (gcloud creates endpoint automatically)
    deploy_model(project_id, args.region, args.dry_run)
    
    print("\n" + "=" * 60)
    print("Deployment started!")
    print("=" * 60)
    print("\nNOTE: After deployment completes, get the endpoint ID from the output")
    print("   and add it to your .env file:")
    print("   MEDGEMMA_ENDPOINT_ID=<endpoint_id>")
    print("\nThen you can use 'medgemma-27b' in benchmarks:")
    print("  python run_benchmark.py --models medgemma-27b --n 1")


if __name__ == "__main__":
    main()
