"""
Thread synchronization utilities for matplotlib and other shared resources.

Matplotlib is not thread-safe and requires global locking when used from multiple threads.
This module provides a single shared lock that all plotting code should use.

IMPORTANT: This module MUST be imported before any matplotlib.pyplot imports to ensure
the Agg backend is set correctly for thread safety.
"""

import threading

# Set non-interactive backend BEFORE pyplot is ever imported
# This is critical for thread safety
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Global lock to synchronize matplotlib access across ALL threads and modules.
# Matplotlib is not thread-safe and can cause corruption if accessed concurrently.
# This single lock must be used by:
# - CoderAgent sandbox execution
# - Zero-Shot vitals panel generation
# - Any other plotting code
matplotlib_lock = threading.RLock()