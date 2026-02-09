"""
Translations module for bilingual (Italian/English) survey support.

Usage:
    from components.translations import t, get_lang, set_lang
    
    label = t("patient_summary")  # Returns translated string for current language
"""

import streamlit as st

# =========================
# TRANSLATIONS DICTIONARY
# =========================

TRANSLATIONS = {
    # --- Page & Navigation ---
    "page_title": {
        "it": "Valutazione AI Clinica",
        "en": "Clinical AI Evaluation",
        "sq": "Vlerësimi Klinik AI"
    },
    "clinical_profile": {
        "it": "Profilo Clinico",
        "en": "Clinical Profile",
        "sq": "Profili Klinik"
    },
    "welcome_message": {
        "it": "Benvenuto/a, **{id}**. Completa il tuo profilo per iniziare.",
        "en": "Welcome, **{id}**. Complete your profile to begin.",
        "sq": "Mirësevini, **{id}**. Plotësoni profilin tuaj për të filluar."
    },
    "reviewer_id_required": {
        "it": "Per favore inserisci un ID Recensore",
        "en": "Please enter a Reviewer ID"
    },
    "start_evaluation": {
        "it": "Inizia Valutazione",
        "en": "Start Evaluation",
        "sq": "Fillo Vlerësimin"
    },
    
    # --- Profile Form ---
    "specialization_label": {
        "it": "Specializzazione / Ruolo clinico",
        "en": "Specialization / Clinical Role",
        "sq": "Specializimi / Roli Klinik"
    },
    "specializations": {
        "it": [
            "Medicina d'Emergenza-Urgenza",
            "Medicina Interna",
            "Terapia Intensiva / Anestesia",
            "Cardiologia",
            "Medicina Generale",
            "Infermiere",
            "Altro personale sanitario (es. OSS, Tecnico)",
            "Specializzando / Studente",
            "Altro"
        ],
        "en": [
            "Emergency Medicine",
            "Internal Medicine",
            "Intensive Care / Anesthesia",
            "Cardiology",
            "General Practice",
            "Nurse",
            "Other Healthcare Staff",
            "Resident / Student",
            "Other"
        ],
        "sq": [
            "Mjekësi Urgjence",
            "Mjekësi Interne",
            "Kujdes Intensiv / Anestezi",
            "Kardiologji",
            "Mjekësi e Përgjithshme",
            "Infermier/e",
            "Staf Tjetër Shëndetësor",
            "Specializant / Student",
            "Tjetër"
        ]
    },
    "experience_label": {
        "it": "Anni di esperienza clinica",
        "en": "Years of clinical experience",
        "sq": "Vite të përvojës klinike"
    },
    "experience_options": {
        "it": ["0-1 anni", "2-5 anni", "6-10 anni", "11-20 anni", "Oltre 20 anni"],
        "en": ["0-1 years", "2-5 years", "6-10 years", "11-20 years", "Over 20 years"],
        "sq": ["0-1 vjet", "2-5 vjet", "6-10 vjet", "11-20 vjet", "Mbi 20 vjet"]
    },
    "setting_label": {
        "it": "Ambito lavorativo principale",
        "en": "Primary Work Setting",
        "sq": "Mjedisi Kryesor i Punës"
    },
    "settings": {
        "it": [
            "Ospedale universitario",
            "Ospedale pubblico (non universitario)",
            "Ospedale privato / convenzionato",
            "Struttura territoriale / ambulatoriale",
            "Assistenza domiciliare",
            "Altro"
        ],
        "en": [
            "University Hospital",
            "Public Hospital (non-academic)",
            "Private Hospital",
            "Outpatient / Community Clinic",
            "Home Care",
            "Other"
        ],
        "sq": [
            "Spital Universitar",
            "Spital Publik (jo-akademik)",
            "Spital Privat",
            "Ambulator / Klinikë Komunitare",
            "Kujdes Shtëpiak",
            "Tjetër"
        ]
    },
    "ai_familiarity_label": {
        "it": "Familiarità con strumenti di Intelligenza Artificiale (1 = Principiante, 5 = Esperto)",
        "en": "Familiarity with AI tools (1 = Beginner, 5 = Expert)",
        "sq": "Njohuri mbi mjetet e Inteligjenicës Artificiale (1 = Fillestar, 5 = Ekspert)"
    },
    
    # --- Survey Navigation ---
    "session_restored": {
        "it": "Sessione ripristinata dal server",
        "en": "Session restored from server",
        "sq": "Seanca u rivendos nga serveri"
    },
    "response_saved": {
        "it": "Risposta salvata!",
        "en": "Response saved!",
        "sq": "Përgjigja u ruajt!"
    },
    "loading_cases": {
        "it": "Caricamento dei casi in valutazione... :hourglass:",
        "en": "Loading evaluation cases... :hourglass:",
        "sq": "Duke ngarkuar rastet e vlerësimit... :hourglass:"
    },
    "clinical_eval_header": {
        "it": "Valutazione Clinica AI",
        "en": "Clinical AI Evaluation",
        "sq": "Vlerësimi Klinik AI"
    },
    "case_label": {
        "it": "Caso",
        "en": "Case",
        "sq": "Rasti"
    },
    "no_cases_found": {
        "it": "Nessun caso da revisionare trovato.",
        "en": "No cases found to review.",
        "sq": "Nuk u gjet asnjë rast për shqyrtim."
    },
    "all_reviews_complete": {
        "it": ":material/check_circle: Tutte le revisioni completate! Grazie per il tuo contributo.",
        "en": ":material/check_circle: All reviews completed! Thank you for your contribution.",
        "sq": ":material/check_circle: Të gjitha rishikimet u përfunduan! Faleminderit për kontributin tuaj."
    },
    
    # --- Visit Separator ---
    "new_visit": {
        "it": "Nuova Visita",
        "en": "New Visit",
        "sq": "Vizitë e Re"
    },
    "prepare_visit": {
        "it": "Preparati a valutare il paziente per la visita del Paziente",
        "en": "Prepare to evaluate the patient for the visit of the Patient",
        "sq": "Përgatitu për të vlerësuar pacientin për vizitën e pacientit"
    },
    "visit_instructions": {
        "it": "Nelle prossime schermate valuterai diverse AI per questo stesso paziente.",
        "en": "In the following screens you will evaluate different AI systems for this same patient.",
        "sq": "Në ekranet në vijim do të vlerësoni sisteme të ndryshme të AI për të njëjtin pacient."
    },
    "start_evaluation_btn": {
        "it": "Inizia Valutazione :material/arrow_forward:",
        "en": "Start Evaluation :material/arrow_forward:",
        "sq": "Fillo Vlerësimin :material/arrow_forward:"
    },
    
    # --- Evaluation Questions ---
    "your_evaluation": {
        "it": "La Tua Valutazione",
        "en": "Your Evaluation",
        "sq": "Vlerësimi Juaj"
    },
    "q1_label": {
        "it": "Q1. Affidabilità Clinica",
        "en": "Q1. Clinical Reliability",
        "sq": "Q1. Besueshmëria Klinike"
    },
    "q1_caption": {
        "it": "*Valuta se la spiegazione fornita sia sufficientemente sicura e affidabile da supportare il ragionamento clinico e contribuire al processo decisionale.*",
        "en": "*Evaluate whether the explanation is safe and reliable enough to support clinical reasoning and decision-making.*",
        "sq": "*Vlerësoni nëse shpjegimi është mjaft i sigurt dhe i besueshëm për të mbështetur arsyetimin klinik dhe vendimmarrjen.*"
    },
    "q1_options": {
        "it": [("no", "No - Non affidabile"), ("partial", "Parzialmente"), ("yes", "Sì - Affidabile")],
        "en": [("no", "No - Unreliable"), ("partial", "Partially"), ("yes", "Yes - Reliable")],
        "sq": [("no", "Jo - E pabesueshme"), ("partial", "Pjesërisht"), ("yes", "Po - E besueshme")]
    },
    "q2_label": {
        "it": "Q2. Accuratezza Fattuale",
        "en": "Q2. Factual Accuracy",
        "sq": "Q2. Saktësia Faktike"
    },
    "q2_caption": {
        "it": "*Valuta la correttezza dei fatti clinici riportati, incluse diagnosi, meccanismi fisiopatologici, test diagnostici o opzioni terapeutiche.*",
        "en": "*Evaluate the correctness of clinical facts reported, including diagnoses, pathophysiology, diagnostic tests, or treatment options.*",
        "sq": "*Vlerësoni korrektësinë e fakteve klinike të raportuara, përfshirë diagnozat, fiziopatologjinë, testet diagnostike ose opsionet e trajtimit.*"
    },
    "q2_options": {
        "it": [("no", "No - Errori"), ("partial", "Parzialmente"), ("yes", "Sì - Accurata")],
        "en": [("no", "No - Errors"), ("partial", "Partially"), ("yes", "Yes - Accurate")],
        "sq": [("no", "Jo - Gabime"), ("partial", "Pjesërisht"), ("yes", "Po - E saktë")]
    },
    "q3_label": {
        "it": "Q3. Rilevanza Clinica",
        "en": "Q3. Clinical Relevance",
        "sq": "Q3. Rëndësia Klinike"
    },
    "q3_caption": {
        "it": "*Valuta il grado di applicabilità delle informazioni a questo specifico caso clinico, indipendentemente dalla correttezza generale.*",
        "en": "*Evaluate how applicable the information is to this specific clinical case, regardless of general correctness.*",
        "sq": "*Vlerësoni zbatueshmërinë e informacionit për këtë rast specifik klinik, pavarësisht saktësisë së përgjithshme.*"
    },
    "q3_options": {
        "it": [("no", "No - Irrilevante"), ("partial", "Parzialmente"), ("yes", "Sì - Rilevante")],
        "en": [("no", "No - Irrelevant"), ("partial", "Partially"), ("yes", "Yes - Relevant")],
        "sq": [("no", "Jo - E parëndësishme"), ("partial", "Pjesërisht"), ("yes", "Po - E rëndësishme")]
    },
    "q4_label": {
        "it": "Q4. Giustificazione delle Conclusioni",
        "en": "Q4. Justification of Conclusions",
        "sq": "Q4. Justifikimi i Përfundimeve"
    },
    "q4_caption": {
        "it": "*Valuta se la spiegazione esplicita in modo adeguato le ragioni che conducono alle conclusioni, facendo riferimento a dati, evidenze o nessi logici.*",
        "en": "*Evaluate whether the explanation adequately states the reasons leading to conclusions, referencing data, evidence, or logical connections.*",
        "sq": "*Vlerësoni nëse shpjegimi tregon qartë arsyet që çojnë në përfundime, duke iu referuar të dhënave, provave ose lidhjeve logjike.*"
    },
    "q4_options": {
        "it": [("no", "No - Ingiustificata"), ("partial", "Parzialmente"), ("yes", "Sì - Giustificata")],
        "en": [("no", "No - Unjustified"), ("partial", "Partially"), ("yes", "Yes - Justified")],
        "sq": [("no", "Jo - E pajustifikuar"), ("partial", "Pjesërisht"), ("yes", "Po - E justifikuar")]
    },
    "q5_label": {
        "it": "Q5. Comprensibilità dei Grafici",
        "en": "Q5. Chart Comprehensibility",
        "sq": "Q5. Kuptueshmëria e Grafikëve"
    },
    "q5_caption": {
        "it": "*Quanto i grafici e le visualizzazioni presentate sono stati facili da comprendere e interpretare correttamente?*",
        "en": "*How easy were the charts and visualizations to understand and interpret correctly?*",
        "sq": "*Sa të lehtë ishin grafikët dhe vizualizimet për t'u kuptuar dhe interpretuar saktë?*"
    },
    "q5_scale": {
        "it": {
            1: "1 - Molto difficili da interpretare",
            2: "2 - Difficili da interpretare",
            3: "3 - Comprensibilità adeguata",
            4: "4 - Facili da interpretare",
            5: "5 - Estremamente chiari e intuitivi"
        },
        "en": {
            1: "1 - Very difficult to interpret",
            2: "2 - Difficult to interpret",
            3: "3 - Adequate comprehensibility",
            4: "4 - Easy to interpret",
            5: "5 - Extremely clear and intuitive"
        },
        "sq": {
            1: "1 - Shumë e vështirë për t'u interpretuar",
            2: "2 - Vështirë për t'u interpretuar",
            3: "3 - Kuptueshmëri adekuate",
            4: "4 - Lehtë për t'u interpretuar",
            5: "5 - Jashtëzakonisht e qartë dhe intuitive"
        }
    },
    "q6_label": {
        "it": "Q6. Utilità Decisionale",
        "en": "Q6. Decision Utility",
        "sq": "Q6. Dobia për Vendimmarrje"
    },
    "q6_caption": {
        "it": "*Quanto questa spiegazione ha facilitato o velocizzato il processo decisionale rispetto all'analisi dei soli dati grezzi?*",
        "en": "*How much did this explanation facilitate or speed up decision-making compared to analyzing raw data alone?*",
        "sq": "*Sa e lehtësoi ose përshpejtoi kjo shpjegim vendimmarrjen krahasuar me analizën e të dhënave të papërpunuara?*"
    },
    "q6_scale": {
        "it": {1: "1 - Inutile", 2: "2 - Scarsa utilità", 3: "3 - Neutrale", 4: "4 - Utile", 5: "5 - Decisiva"},
        "en": {1: "1 - Useless", 2: "2 - Low utility", 3: "3 - Neutral", 4: "4 - Useful", 5: "5 - Decisive"},
        "sq": {1: "1 - E padobishme", 2: "2 - Pak e dobishme", 3: "3 - Neutrale", 4: "4 - E dobishme", 5: "5 - Vendimtare"}
    },
    
    # --- Feedback ---
    "optional_feedback": {
        "it": "Feedback Qualitativo Opzionale",
        "en": "Optional Qualitative Feedback",
        "sq": "Feedback Cilësor Opsional"
    },
    "feedback_caption": {
        "it": "*Annota eventuali punti di forza specifici, problemi o preoccupazioni di sicurezza (es. allucinazioni, affermazioni non supportate, ragionamenti fuorvianti).*",
        "en": "*Note any specific strengths, problems, or safety concerns (e.g., hallucinations, unsupported claims, misleading reasoning).*",
        "sq": "*Shënoni pika të forta specifike, probleme ose shqetësime sigurie (p.sh. halucinacione, pretendime të pambështetura, arsyetime çorientuese).*"
    },
    "written_comments": {
        "it": "Commenti scritti",
        "en": "Written comments",
        "sq": "Komente me shkrim"
    },
    "written_feedback_label": {
        "it": "Feedback scritto",
        "en": "Written feedback",
        "sq": "Feedback me shkrim"
    },
    "comments_placeholder": {
        "it": "Commenti liberi...",
        "en": "Free comments...",
        "sq": "Komente të lira..."
    },
    "audio_feedback": {
        "it": "Feedback audio",
        "en": "Audio feedback",
        "sq": "Feedback Audio"
    },
    "record_audio": {
        "it": "Registra audio",
        "en": "Record audio",
        "sq": "Regjistro Audio"
    },
    "delete_recording": {
        "it": "Cancella registrazione",
        "en": "Delete recording",
        "sq": "Fshi Regjistrimin"
    },
    
    # --- Submit ---
    "case_evaluation": {
        "it": "Valutazione del Caso",
        "en": "Case Evaluation",
        "sq": "Vlerësimi i Rastit"
    },
    "wait_seconds": {
        "it": "Attendi",
        "en": "Wait",
        "sq": "Prit"
    },
    "submit_continue": {
        "it": ":material/check_circle: Invia e Prosegui",
        "en": ":material/check_circle: Submit and Continue",
        "sq": ":material/check_circle: Dërgo dhe Vazhdo"
    },
    
    # --- UI Render Output (ui.py) ---
    "patient_summary": {
        "it": "Riepilogo Paziente",
        "en": "Patient Summary",
        "sq": "Përmbledhja e Pacientit"
    },
    "patient": {
        "it": "Paziente",
        "en": "Patient",
        "sq": "Pacienti"
    },
    "current_therapy": {
        "it": "Terapia Attuale",
        "en": "Current Therapy",
        "sq": "Terapia Aktuale"
    },
    "vital_signs_profile": {
        "it": "Parametri Vitali e Profilo di Rischio",
        "en": "Vital Signs & Risk Profile",
        "sq": "Shenjat Vitale & Profili i Rrezikut"
    },
    "key_abnormal_patterns": {
        "it": "Pattern Anomali Chiave",
        "en": "Key Abnormal Patterns",
        "sq": "Modele Anormale Kyçe"
    },
    "clinical_interpretation": {
        "it": "Interpretazione Clinica",
        "en": "Clinical Interpretation",
        "sq": "Interpretimi Klinik"
    },
    "clinical_actions": {
        "it": "Azioni Cliniche",
        "en": "Clinical Actions",
        "sq": "Veprime Klinike"
    },
    "visual_context": {
        "it": "Contesto Visivo",
        "en": "Visual Context",
        "sq": "Konteksti Vizual"
    },
    "image_load_error": {
        "it": "Errore nel caricamento dell'immagine",
        "en": "Error loading image",
        "sq": "Gabim në ngarkimin e imazhit"
    },
    "figure": {
        "it": "Figura",
        "en": "Figure",
        "sq": "Figura"
    },
    "no_visual_evidence": {
        "it": "Nessuna evidenza visiva generata per questo caso.",
        "en": "No visual evidence generated for this case.",
        "sq": "Nuk u gjenerua asnjë provë vizuale për këtë rast."
    },
    
    # --- Default Button Labels ---
    "yes": {
        "it": "Sì",
        "en": "Yes",
        "sq": "Po"
    },
    "no": {
        "it": "No",
        "en": "No",
        "sq": "Jo"
    },
    "partial": {
        "it": "Parzialmente",
        "en": "Partially",
        "sq": "Pjesërisht"
    },
    
    # --- Language Selector ---
    "language": {
        "it": "Lingua",
        "en": "Language",
        "sq": "Gjuha"
    },
    "italian": {
        "it": "🇮🇹 Italiano",
        "en": "🇮🇹 Italian",
        "sq": "🇮🇹 Italisht"
    },
    "english": {
        "it": "🇬🇧 Inglese",
        "en": "🇬🇧 English",
        "sq": "🇬🇧 Anglisht"
    },
    "albanian": {
        "it": "🇦🇱 Albanese",
        "en": "🇦🇱 Albanian",
        "sq": "🇦🇱 Shqip"
    },
    
    # --- UI Improvements ---
    "back_button": {
        "it": ":material/arrow_back: Indietro",
        "en": ":material/arrow_back: Back",
        "sq": ":material/arrow_back: Prapa"
    },
    "patient_consistency_warning": {
        "it": "Nota: I dati clinici per uno stesso paziente sono identici, ma ogni IA genera spiegazioni e grafici unici. Il grafico dei segnali vitali (Fig. 1) userà soglie adattate al paziente (basate su anamnesi/farmaci) e potrebbero essere fornite ulteriori visualizzazioni.",
        "en": "Note: Clinical data remains identical for the same patient, but each AI generates unique explanations and plots. Vital signs charts (Fig. 1) will use patient-adapted thresholds (based on history/meds) and additional visualizations may be provided.",
        "sq": "Shënim: Të dhënat klinike mbeten identike për të një pacient të tjetër, por çdo AI gjeneron shpjegime dhe grafikë unikë. Grafikët e shenjave vitale (Fig. 1) do të përdorin pragje të përshtatura për pacientin (bazuar në histori/medikamente) dhe mund të ofrohen vizualizime shtesë."
    },
    "patient_eval_header": {
        "it": "Paziente **{visit_id}** - Valutazione **{count}**",
        "en": "Patient **{visit_id}** - Evaluation **{count}**",
        "sq": "Pacienti **{visit_id}** - Vlerësimi **{count}**"
    },

    # --- Model Comparison Dashboard ---
    "model_comparison_title": {
        "it": ":material/bar_chart: Cruscotto Confronto Modelli",
        "en": ":material/bar_chart: Model Comparison Dashboard",
        "sq": ":material/bar_chart: Paneli i Krahasimit të Modeleve"
    },
    "model_comparison_subtitle": {
        "it": "Confronta le prestazioni Zero-Shot vs Agentic in tutti gli esperimenti.",
        "en": "Compare Zero-Shot vs Agentic framework performance across all experiments.",
        "sq": "Krahasoni performancën Zero-Shot vs Agentic në të gjitha eksperimentet."
    },
    "metrics_tab": {
        "it": ":material/trending_up: Metriche",
        "en": ":material/trending_up: Metrics",
        "sq": ":material/trending_up: Metrikat"
    },
    "expert_scores_tab": {
        "it": ":material/medical_services: Punteggi Esperti",
        "en": ":material/medical_services: Expert Scores",
        "sq": ":material/medical_services: Pikët e Ekspertëve"
    },
    "fairness_tab": {
        "it": ":material/balance: Equità",
        "en": ":material/balance: Fairness",
        "sq": ":material/balance: Drejtësia"
    },
    "clinician_stats_tab": {
        "it": ":material/group: Statistiche Clinici",
        "en": ":material/group: Clinician Stats",
        "sq": ":material/group: Statistikat e Klinicistit"
    },
    "metrics_header": {
        "it": ":material/target: Metriche Quantitative",
        "en": ":material/target: Quantitative Metrics",
        "sq": ":material/target: Metrikat Kuantitative"
    },
    "no_results_warning": {
        "it": "Nessun risultato trovato. Esegui prima gli esperimenti per vedere le metriche.",
        "en": "No experiment results found. Run experiments first to see metrics.",
        "sq": "Nuk u gjetën rezultate. Ekzekutoni eksperimentet fillimisht për të parë metrikat."
    },
    "expert_scores_header": {
        "it": "Punteggi Qualitativi degli Esperti",
        "en": "Expert Qualitative Scores",
        "sq": "Pikët Cilësore të Ekspertëve"
    },
    "fairness_header": {
        "it": "Analisi dell'Equità (Fairness)",
        "en": "Fairness Analysis",
        "sq": "Analiza e Drejtësisë (Fairness)"
    },
    "esi_bias_header": {
        "it": "Bias Accuratezza ESI per Etnia",
        "en": "ESI Accuracy Bias by Ethnicity",
        "sq": "Bias i Saktësisë ESI sipas Etnisë"
    },
    "pain_bias_header": {
        "it": "Errore Gestione Dolore per Etnia",
        "en": "Pain Management Error by Ethnicity",
        "sq": "Gabimi në Menaxhimin e Dhimbjes sipas Etnisë"
    },
    "age_bias_header": {
        "it": "Per Gruppo di Età",
        "en": "By Age Group",
        "sq": "Sipas Grupmoshës"
    },
    "by_ethnicity": {
        "it": "Per Etnia",
        "en": "By Ethnicity",
        "sq": "Sipas Etnisë"
    },
    "analysis_metric_label": {
        "it": "Metrica per Analisi Bias",
        "en": "Metric for Bias Analysis",
        "sq": "Metrika për Analizën e Biasit"
    },
    "model_select_label": {
        "it": "Seleziona Modello",
        "en": "Select Model",
        "sq": "Zgjidh Modelin"
    },
    
    # --- Tutorial Page ---
    "tutorial_title": {
        "it": "Guida alla Valutazione",
        "en": "Evaluation Guide",
        "sq": "Udhëzues Vlerësimi"
    },
    "tutorial_proceed": {
        "it": ":material/arrow_forward: Inizia le Valutazioni",
        "en": ":material/arrow_forward: Start Evaluations",
        "sq": ":material/arrow_forward: Fillo Vlerësimet"
    },
    "tutorial_objective_title_clean": {
        "it": "Obiettivo dello Studio",
        "en": "Study Objective",
        "sq": "Objektivi i Studimit"
    },
    "tutorial_objective_desc": {
        "it": """Questo studio mira a valutare l'efficacia delle spiegazioni cliniche generate da sistemi di intelligenza artificiale aventi l’obiettivo di supportare il triage ospedaliero e la comprensione rapida di eventi anomali riscontrati tramite il monitoraggio di parametri vitali (frequenza cardiaca, pressione arteriosa, saturazione di ossigeno, frequenza respiratoria e temperatura).
Importante: Le anomalie riscontrate fanno parte di un dataset pubblico validato, quindi le anomalie sono da considerare confermate. Il suo compito è valutare solo la qualità e l'utilità delle spiegazioni generate dall'AI, non verificarne l'accuratezza diagnostica. Per un medico infatti comprendere e validare una diagnosi automatica è essenziale per utilizzare con fiducia uno strumento di supporto alle decisioni.""",
        "en": """This study aims to evaluate the effectiveness of AI-generated clinical explanations intended to support hospital triage and rapid understanding of abnormal events detected through vital signs monitoring (heart rate, blood pressure, oxygen saturation, respiratory rate, and temperature).
Important: The detected anomalies are part of a validated public dataset, so the anomalies are to be considered confirmed. Your task is to evaluate only the quality and usefulness of the explanations generated by the AI, not to verify their diagnostic accuracy. Indeed, for a doctor, understanding and validating an automatic diagnosis is essential to confidently use a decision support tool.""",
        "sq": """Ky studim synon të vlerësojë efektivitetin e shpjegimeve klinike të gjeneruara nga sistemet e inteligjencës artificiale me qëllim mbështetjen e triazhit spitalor dhe kuptimin e shpejtë të ngjarjeve anormale të zbuluara përmes monitorimit të shenjave vitale (rrahjet e zemrës, presioni i gjakut, ngopja me oksigjen, frekuenca e frymëmarrjes dhe temperatura).
E rëndësishme: Anomalitë e zbuluara janë pjesë e një grupi të dhënash publike të vërtetuara, kështu që anomalitë duhet të konsiderohen të konfirmuara. Detyra juaj është të vlerësoni vetëm cilësinë dhe dobinë e shpjegimeve të gjeneruara nga AI, jo të verifikoni saktësinë e tyre diagnostike. Në të vërtetë, për një mjek, kuptimi dhe validimi i një diagnoze automatike është thelbësor për të përdorur me besim një mjet mbështetës për vendimet."""
    },
    "tutorial_task_title_clean": {
        "it": "Il Suo Compito",
        "en": "Your Task",
        "sq": "Detyra Juaj"
    },
    "tutorial_task_desc": {
        "it": """Il suo obiettivo è valutare se le spiegazioni cliniche generate dall'AI sono utili, accurate e sicure per la pratica medica reale.
Dovrà analizzare ogni caso confrontando la spiegazione dell'AI con i dati clinici e le immagini dei parametri vitali forniti per ogni paziente. Il suo giudizio aiuterà a capire se questi strumenti possono realmente supportare decisioni rapide di triage e handover.""",
        "en": """Your objective is to evaluate whether the clinical explanations generated by the AI are useful, accurate, and safe for real medical practice.
You will have to analyze each case by comparing the AI explanation with the clinical data and vital signs images provided for each patient. Your judgment will help understand if these tools can really support rapid triage and handover decisions.""",
        "sq": """Qëllimi juaj është të vlerësoni nëse shpjegimet klinike të gjeneruara nga AI janë të dobishme, të sakta dhe të sigurta për praktikën reale mjekësore.
Do t'ju duhet të analizoni çdo rast duke krahasuar shpjegimin e AI me të dhënat klinike dhe imazhet e shenjave vitale të ofruara për çdo pacient. Gjykimi juaj do të ndihmojë për të kuptuar nëse këto mjete mund të mbështesin vërtet vendimet e shpejta të triazhit dhe dorëzimit."""
    },
    "tutorial_structure_title_clean": {
        "it": "Struttura delle Spiegazioni",
        "en": "Explanation Structure",
        "sq": "Struktura e Shpjegimeve"
    },
    "tutorial_structure_intro": {
        "it": "Ogni spiegazione è organizzata seguendo questo schema:",
        "en": "Each explanation is organized following this template:",
        "sq": "Çdo shpjegim është organizuar sipas këtij shablloni:"
    },
    "tutorial_structure_patient": {
        "it": "<strong>Riepilogo Paziente</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Dati demografici, motivo dell'accesso e terapia</span>",
        "en": "<strong>Patient Summary</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Demographics, chief complaint, and therapy</span>",
        "sq": "<strong>Përmbledhja e Pacientit</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Demografia, ankesa kryesore dhe terapia</span>"
    },
    "tutorial_structure_vitals": {
        "it": "<strong>Parametri Vitali</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>ESI, qSOFA, MAP e indicatori chiave</span>",
        "en": "<strong>Vital Signs & Risk</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>ESI, qSOFA, MAP and key indicators</span>",
        "sq": "<strong>Shenjat Vitale & Rreziku</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>ESI, qSOFA, MAP dhe treguesit kryesorë</span>"
    },
    "tutorial_structure_patterns": {
        "it": "<strong>Pattern Anomali</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Principali anomalie rilevate nei dati</span>",
        "en": "<strong>Key Abnormal Patterns</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Main anomalies detected in data</span>",
        "sq": "<strong>Modele Anormale Kyçe</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Anomalitë kryesore të zbuluara në të dhëna</span>"
    },
    "tutorial_structure_interpretation": {
        "it": "<strong>Interpretazione Clinica</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Significato clinico delle anomalie</span>",
        "en": "<strong>Clinical Interpretation</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Clinical significance of anomalies</span>",
        "sq": "<strong>Interpretimi Klinik</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Kuptimi klinik i anomalive</span>"
    },
    "tutorial_structure_actions": {
        "it": "<strong>Azioni Cliniche</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Suggerimenti per esami o interventi</span>",
        "en": "<strong>Clinical Actions</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Suggestions for tests or interventions</span>",
        "sq": "<strong>Veprime Klinike</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Sugjerime për teste ose ndërhyrje</span>"
    },
    "tutorial_structure_visual": {
        "it": "<strong>Contesto Visivo</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Grafici dei parametri con evidenza anomalie</span>",
        "en": "<strong>Visual Context</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Vital signs charts with highlighted anomalies</span>",
        "sq": "<strong>Konteksti Vizual</strong><br><span style='font-size: 0.9em; opacity: 0.8;'>Grafikët e shenjave vitale me anomali të theksuara</span>"
    },
    "tutorial_mockup_title": {
        "it": "Anteprima Dashboard",
        "en": "Dashboard Preview",
        "sq": "Pam paraprake e Panelit"
    },
    "tutorial_mockup_patient_desc": {
        "it": "Donna di 79 anni con sospetta sepsi, ipertensione e diabete...",
        "en": "79-year-old woman with suspected sepsis, hypertension, and diabetes...",
        "sq": "Grua 79-vjeçare me dyshim për sepsë, hipertension dhe diabet..."
    },
    "tutorial_mockup_vitals_status": {
        "it": "condizione di stress",
        "en": "stress condition",
        "sq": "gjendje stresi"
    },
    "tutorial_mockup_patterns_desc": {
        "it": "Ipotensione persistente (MAP 52 mmHg) e tachicardia compensatoria...",
        "en": "Persistent hypotension (MAP 52 mmHg) and compensatory tachycardia...",
        "sq": "Hipotension i vazhdueshëm (MAP 52 mmHg) dhe takikardi kompensuese..."
    },
    "tutorial_mockup_interpretation_desc": {
        "it": "La presentazione è coerente con shock settico. Il calo della MAP...",
        "en": "The presentation is consistent with septic shock. The drop in MAP...",
        "sq": "Prezantimi është në përputhje me shokun septik. Rënia e MAP..."
    },
    "tutorial_mockup_action_1": {
        "it": "Iniziare rianimazione con fluidi",
        "en": "Begin fluid resuscitation",
        "sq": "Fillo ringjalljen me lëngje"
    },
    "tutorial_mockup_action_2": {
        "it": "Monitoraggio stretto lattati",
        "en": "Close lactate monitoring",
        "sq": "Monitorim i ngushtë i laktatit"
    },
    "tutorial_mockup_visual_desc": {
        "it": "Qui vengono presentate le schermate che raffigurano i segnali vitali rilevanti a supporto della diagnosi.",
        "en": "Here screens depicting the relevant vital signs supporting the diagnosis are presented.",
        "sq": "Këtu paraqiten ekranet që përshkruajnë shenjat vitale përkatëse që mbështesin diagnozën."
    },
    "tutorial_images_title_clean": {
        "it": "Apertura Immagini a Schermo Intero",
        "en": "Opening Full-Screen Images",
        "sq": "Hapja e Imazheve në Ekran të Plotë"
    },
    "tutorial_images_desc": {
        "it": "Per visualizzare i grafici a schermo intero, clicca su un'immagine e poi sul pulsante di espansione nell'angolo in alto a destra dell'immagine.",
        "en": "To view charts in full screen, click on an image and then on the expand button in the top right corner of the image.",
        "sq": "Për të parë grafikët në ekran të plotë, klikoni mbi një imazh dhe pastaj në butonin e zgjerimit në këndin e djathtë lart të imazhit."
    },
    "tutorial_consecutive_title_clean": {
        "it": "Spiegazioni Consecutive",
        "en": "Consecutive Explanations",
        "sq": "Shpjegime të Njëpasnjëshme"
    },
    "tutorial_consecutive_desc": {
        "it": "Per ogni singolo paziente, vengono mostrate valutazioni (spiegazioni) generate da modelli di IA alternativi, essendo uno degli obiettivi di questa valutazione anche quello di identificare il modello più utile ed efficace. Le valutazioni generate dalle diverse IA sono mostrate consecutivamente per lo stesso paziente. Questo permette di familiarizzarsi con il caso e velocizzare la valutazione di spiegazioni alternative.",
        "en": "For each single patient, evaluations (explanations) generated by alternative AI models are shown, as one of the objectives of this evaluation is also to identify the most useful and effective model. Evaluations generated by different AIs are shown consecutively for the same patient. This allows you to familiarize yourself with the case and speed up the evaluation of alternative explanations.",
        "sq": "Për çdo pacient të vetëm, shfaqen vlerësime (shpjegime) të gjeneruara nga modele alternative të AI, pasi një nga objektivat e këtij vlerësimi është gjithashtu identifikimi i modelit më të dobishëm dhe efektiv. Vlerësimet e gjeneruara nga AI të ndryshme shfaqen njëra pas tjetrës për të njëjtin pacient. Kjo ju lejon të njiheni me rastin dhe të shpejtoni vlerësimin e shpjegimeve alternative."
    },
    "tutorial_questions_title_clean": {
        "it": "Le Domande",
        "en": "The Questions",
        "sq": "Pyetjet"
    },
    "tutorial_questions_desc": {
        "it": """Dopo ogni spiegazione, le verrà chiesto di valutare:

- **Affidabilità Clinica**: La spiegazione è sicura e affidabile per supportare il ragionamento clinico?
- **Accuratazza Fattuale**: I fatti clinici riportati sono corretti?
- **Rilevanza Clinica**: Le informazioni sono applicabili a questo specifico caso?
- **Giustificazione delle Conclusioni**: Le conclusioni sono adeguatamente motivate?
- **Comprensibilità dei Grafici**: I grafici sono facili da interpretare?
- **Utilità Decisionale**: La spiegazione facilita il processo decisionale?

Lei potrà anche aggiungere commenti liberi o note audio per esempi specifici.""",
        "en": """After each explanation, you will be asked to evaluate:

- **Clinical Reliability**: Is the explanation safe and reliable to support clinical reasoning?
- **Factual Accuracy**: Are the reported clinical facts correct?
- **Clinical Relevance**: Is the information applicable to this specific case?
- **Justification of Conclusions**: Are the conclusions adequately motivated?
- **Chart Comprehensibility**: Are the charts easy to interpret?
- **Decision Utility**: Does the explanation facilitate the decision-making process?

You will also be able to add free comments or audio notes for specific examples.""",
        "sq": """Pas çdo shpjegimi, do t'ju kërkohet të vlerësoni:

- **Besueshmëria Klinike**: A është shpjegimi i sigurt dhe i besueshëm për të mbështetur arsyetimin klinik?
- **Saktësia Faktike**: A janë të sakta faktet klinike të raportuara?
- **Rëndësia Klinike**: A është informacioni i zbatueshëm për këtë rast specifik?
- **Justifikimi i Përfundimeve**: A janë të motivuara siç duhet përfundimet?
- **Kuptueshmëria e Grafikëve**: A janë grafikët të lehtë për t'u interpretuar?
- **Dobia për Vendimmarrje**: A lehtëson shpjegimi procesin e vendimmarrjes?

Ju gjithashtu mund të shtoni komente të lira ose shënime audio për shembuj specifikë."""
    },
    "tutorial_session_title_clean": {
        "it": "Salvataggio Automatico",
        "en": "Automatic Saving",
        "sq": "Ruajtja Automatike"
    },
    "tutorial_session_desc": {
        "it": "Il questionario salva automaticamente tutte le tue risposte. Potrà interrompere la valutazione in qualsiasi momento e riprenderla successivamente dallo stesso dispositivo. I suoi progressi saranno conservati.",
        "en": "The questionnaire automatically saves all your answers. You can stop the evaluation at any time and resume it later from the same device. Your progress will be preserved.",
        "sq": "Pyetësori ruan automatikisht të gjitha përgjigjet tuaja. Mund të ndaloni vlerësimin në çdo kohë dhe të vazhdoni më vonë nga e njëjta pajisje. Përparimi juaj do të ruhet."
    },
    "tutorial_notes_title_clean": {
        "it": "Note e Commenti",
        "en": "Notes and Comments",
        "sq": "Shënime dhe Komente"
    },
    "tutorial_notes_desc": {
        "it": """Se desidera commentare esempi specifici, potrà utilizzare:

- **Note scritte**: Campo di testo libero per osservazioni dettagliate
- **Note audio**: Registrazione vocale rapida per feedback immediato""",
        "en": """If you wish to comment on specific examples, you can use:

- **Written notes**: Free text field for detailed observations
- **Audio notes**: Quick voice recording for immediate feedback""",
        "sq": """Nëse dëshironi të komentoni shembuj specifikë, mund të përdorni:

- **Shënime me shkrim**: Fushë me tekst të lirë për vëzhgime të detajuara
- **Shënime audio**: Regjistrim i shpejtë zanor për feedback të menjëhershëm"""
    },

    # --- Glossary ---
    "glossary_title": {
        "it": "Guida alle Definizioni Cliniche",
        "en": "Clinical Definitions Guide",
        "sq": "Udhëzues i Përkufizimeve Klinike"
    },
    "glossary_intro": {
        "it": "Riferimento rapido per i parametri visualizzati:",
        "en": "Quick reference for displayed parameters:",
        "sq": "Referencë e shpejtë për parametrat e shfaqur:"
    },
    "glossary_esi": {
        "en": {
            "desc": "Five-level triage scale classifying patients by acuity and expected resource needs.",
            "table": {
                "headers": ["ESI Level", "Meaning"],
                "rows": [
                    {"cols": ["1", "Immediate life-saving intervention"], "match": "1", "color": "red"},
                    {"cols": ["2", "High risk / severe pain / distress"], "match": "2", "color": "orange"},
                    {"cols": ["3", "Stable, ≥2 resources needed"], "match": "3", "color": "yellow"},
                    {"cols": ["4", "Stable, 1 resource"], "match": "4", "color": "green"},
                    {"cols": ["5", "Stable, no resources"], "match": "5", "color": "green"}
                ]
            }
        },
        "it": {
            "desc": "Scala di triage a 5 livelli che classifica i pazienti in base all'acuzie e alle risorse previste.",
            "table": {
                "headers": ["Livello ESI", "Significato"],
                "rows": [
                    {"cols": ["1", "Intervento salvavita immediato"], "match": "1", "color": "red"},
                    {"cols": ["2", "Alto rischio / dolore severo / distress"], "match": "2", "color": "orange"},
                    {"cols": ["3", "Stabile, ≥2 risorse necessarie"], "match": "3", "color": "yellow"},
                    {"cols": ["4", "Stabile, 1 risorsa"], "match": "4", "color": "green"},
                    {"cols": ["5", "Stabile, nessuna risorsa"], "match": "5", "color": "green"}
                ]
            }
        },
        "sq": {
            "desc": "Shkallë triazhi me 5 nivele që klasifikon pacientët sipas mprehtësisë dhe burimeve të pritura.",
            "table": {
                "headers": ["Niveli ESI", "Kuptimi"],
                "rows": [
                    {"cols": ["1", "Ndërhyrje e menjëhershme për shpëtimin e jetës"], "match": "1", "color": "red"},
                    {"cols": ["2", "Rrezik i lartë / dhimbje e fortë / shqetësim"], "match": "2", "color": "orange"},
                    {"cols": ["3", "Stabël, ≥2 burime të nevojshme"], "match": "3", "color": "yellow"},
                    {"cols": ["4", "Stabël, 1 burim"], "match": "4", "color": "green"},
                    {"cols": ["5", "Stabël, asnjë burim"], "match": "5", "color": "green"}
                ]
            }
        }
    },
    "glossary_stress": {
        "en": {
            "desc": "Overall physiologic burden reflecting systemic response to illness or injury.",
            "bullets": [
                "Abnormal vital signs",
                "Altered mental status",
                "Metabolic derangement",
                "Respiratory compromise"
            ],
            "note": "Displayed as informational label (Low / Moderate / High / Stressed)."
        },
        "it": {
            "desc": "Carico fisiologico complessivo che riflette la risposta sistemica alla malattia o al trauma.",
            "bullets": [
                "Segni vitali anormali",
                "Stato mentale alterato",
                "Alterazioni metaboliche",
                "Compromissione respiratoria"
            ],
            "note": "Visualizzato come etichetta informativa (Basso / Moderato / Alto / Stress)."
        },
        "sq": {
            "desc": "Ngarkesa e përgjithshme fiziologjike që reflekton përgjigjen sistemike ndaj sëmundjes ose dëmtimit.",
            "bullets": [
                "Shenja vitale jonormale",
                "Gjendje mendore e ndryshuar",
                "Çrregullim metabolik",
                "Kompromis respirator"
            ],
            "note": "Shfaqet si etiketë informuese (I ulët / I moderuar / I lartë / Stres)."
        }
    },
    "glossary_qsofa": {
        "en": {
            "desc": "Rapid bedside score to identify patients with suspected infection at risk of poor outcomes.",
            "table": {
                "headers": ["Score", "Analysis"],
                "rows": [
                    {"cols": ["0-1", "Lower immediate risk"], "match": "low", "color": "green"},
                    {"cols": ["≥ 2", "High risk / possible sepsis"], "match": "high", "color": "red"}
                ]
            },
            "extra_table": {
                 "headers": ["Criterion", "Threshold"],
                 "rows": [
                     {"cols": ["Respiratory rate", "≥ 22 /min"]},
                     {"cols": ["Systolic BP", "≤ 100 mmHg"]},
                     {"cols": ["Mental status", "GCS ≤ 14"]}
                 ]
            }
        },
        "it": {
            "desc": "Punteggio rapido al letto del paziente per identificare sospette infezioni a rischio di esiti negativi.",
            "table": {
                "headers": ["Punteggio", "Analisi"],
                "rows": [
                    {"cols": ["0-1", "Basso rischio immediato"], "match": "low", "color": "green"},
                    {"cols": ["≥ 2", "Alto rischio / possibile sepsi"], "match": "high", "color": "red"}
                ]
            },
            "extra_table": {
                 "headers": ["Criterio", "Soglia"],
                 "rows": [
                     {"cols": ["Frequenza respiratoria", "≥ 22 /min"]},
                     {"cols": ["Pressione Sistolica", "≤ 100 mmHg"]},
                     {"cols": ["Stato mentale", "GCS ≤ 14"]}
                 ]
            }
        },
        "sq": {
            "desc": "Rezultat i shpejtë për të identifikuar pacientët me infeksion të dyshuar në rrezik për rezultate të dobëta.",
            "table": {
                "headers": ["Pikët", "Analiza"],
                "rows": [
                    {"cols": ["0-1", "Rrezik i ulët i menjëhershëm"], "match": "low", "color": "green"},
                    {"cols": ["≥ 2", "Rrezik i lartë / seps i mundshëm"], "match": "high", "color": "red"}
                ]
            },
            "extra_table": {
                 "headers": ["Kriteri", "Pragu"],
                 "rows": [
                     {"cols": ["Ritmi i frymëmarrjes", "≥ 22 /min"]},
                     {"cols": ["Presioni Sistolik", "≤ 100 mmHg"]},
                     {"cols": ["Gjendja mendore", "GCS ≤ 14"]}
                 ]
            }
        }
    },
    "glossary_map": {
        "en": {
            "desc": "Represents average arterial pressure and adequacy of organ perfusion.",
            "table": {
                "headers": ["MAP (mmHg)", "Interpretation"],
                "rows": [
                    {"cols": ["< 60", "Critical hypoperfusion"], "match": "critical", "color": "red"},
                    {"cols": ["60–64", "Borderline"], "match": "borderline", "color": "orange"},
                    {"cols": ["65–100", "Adequate perfusion"], "match": "adequate", "color": "green"},
                    {"cols": ["> 100", "Elevated afterload"], "match": "high", "color": "yellow"}
                ]
            }
        },
        "it": {
            "desc": "Rappresenta la pressione arteriosa media e l'adeguatezza della perfusione d'organo.",
            "table": {
                "headers": ["MAP (mmHg)", "Interpretazione"],
                "rows": [
                    {"cols": ["< 60", "Ipoperfusione critica"], "match": "critical", "color": "red"},
                    {"cols": ["60–64", "Borderline"], "match": "borderline", "color": "orange"},
                    {"cols": ["65–100", "Perfusione adeguata"], "match": "adequate", "color": "green"},
                    {"cols": ["> 100", "Postcarico elevato"], "match": "high", "color": "yellow"}
                ]
            }
        },
        "sq": {
            "desc": "Përfaqëson presionin arterial mesatar dhe përshtatshmërinë e perfuzionit të organeve.",
            "table": {
                "headers": ["MAP (mmHg)", "Interpretimi"],
                "rows": [
                    {"cols": ["< 60", "Hipoperfuzion kritik"], "match": "critical", "color": "red"},
                    {"cols": ["60–64", "Në kufi"], "match": "borderline", "color": "orange"},
                    {"cols": ["65–100", "Perfuzion adekuat"], "match": "adequate", "color": "green"},
                    {"cols": ["> 100", "Ngarkesë e lartë"], "match": "high", "color": "yellow"}
                ]
            }
        }
    },
    "glossary_shock": {
        "en": {
            "desc": "Ratio of heart rate to systolic BP indicating early hemodynamic instability.",
            "table": {
                "headers": ["Shock Index", "Meaning"],
                "rows": [
                    {"cols": ["0.5–0.7", "Normal"], "match": "normal", "color": "green"},
                    {"cols": ["0.8–0.9", "Compensated shock"], "match": "compensated", "color": "yellow"},
                    {"cols": ["≥ 1.0", "High risk shock"], "match": "shock", "color": "red"}
                ]
            }
        },
        "it": {
            "desc": "Rapporto tra frequenza cardiaca e pressione sistolica che indica instabilità emodinamica precoce.",
            "table": {
                "headers": ["Shock Index", "Significato"],
                "rows": [
                    {"cols": ["0.5–0.7", "Normale"], "match": "normal", "color": "green"},
                    {"cols": ["0.8–0.9", "Shock compensato"], "match": "compensated", "color": "yellow"},
                    {"cols": ["≥ 1.0", "Shock ad alto rischio"], "match": "shock", "color": "red"}
                ]
            }
        },
        "sq": {
            "desc": "Raporti i rrahjeve të zemrës me tensionin sistolik që tregon paqëndrueshmëri hemodinamike të hershme.",
            "table": {
                "headers": ["Shock Index", "Kuptimi"],
                "rows": [
                    {"cols": ["0.5–0.7", "Normale"], "match": "normal", "color": "green"},
                    {"cols": ["0.8–0.9", "Shock i kompensuar"], "match": "compensated", "color": "yellow"},
                    {"cols": ["≥ 1.0", "Shock me rrezik të lartë"], "match": "shock", "color": "red"}
                ]
            }
        }
    },
    "glossary_pain": {
        "en": {
            "desc": "Patient-reported assessment of pain intensity (0–10).",
            "table": {
                "headers": ["Score", "Severity"],
                "rows": [
                    {"cols": ["0", "No pain"], "match": "none", "color": "grey"},
                    {"cols": ["1–3", "Mild"], "match": "mild", "color": "green"},
                    {"cols": ["4–6", "Moderate"], "match": "moderate", "color": "yellow"},
                    {"cols": ["7–10", "Severe"], "match": "severe", "color": "red"}
                ]
            }
        },
        "it": {
            "desc": "Valutazione dell'intensità del dolore riportata dal paziente (0-10).",
            "table": {
                "headers": ["Punteggio", "Severità"],
                "rows": [
                    {"cols": ["0", "Nessun dolore"], "match": "none", "color": "grey"},
                    {"cols": ["1–3", "Lieve"], "match": "mild", "color": "green"},
                    {"cols": ["4–6", "Moderato"], "match": "moderate", "color": "yellow"},
                    {"cols": ["7–10", "Severo"], "match": "severe", "color": "red"}
                ]
            }
        },
        "sq": {
            "desc": "Vlerësim i raportuar nga pacienti për intensitetin e dhimbjes (0-10).",
            "table": {
                "headers": ["Pikët", "Ashpërsia"],
                "rows": [
                    {"cols": ["0", "Pa dhimbje"], "match": "none", "color": "grey"},
                    {"cols": ["1–3", "E lehtë"], "match": "mild", "color": "green"},
                    {"cols": ["4–6", "E moderuar"], "match": "moderate", "color": "yellow"},
                    {"cols": ["7–10", "E rëndë"], "match": "severe", "color": "red"}
                ]
            }
        }
    },
    "description": {
        "en": "Description",
        "it": "Descrizione",
        "sq": "Përshkrimi"
    },
    "glossary_los": {
        "en": {
            "desc": "Time from ED arrival to departure (ED-LOS).",
            "bullets": [
                "Reflects throughput efficiency and crowding.",
                "Typical operational benchmark is 4–6 hours."
            ]
        },
        "it": {
            "desc": "Tempo dall'arrivo in PS alla partenza (ED-LOS).",
            "bullets": [
                "Riflette l'efficienza del flusso e il sovraffollamento.",
                "Il benchmark operativo tipico è di 4–6 ore."
            ]
        },
        "sq": {
            "desc": "Koha nga mbërritja në urgjencë deri në largim (ED-LOS).",
            "bullets": [
                "Pasqyron efikasitetin e rrjedhës dhe mbipopullimin.",
                "Standardi tipik operacional është 4–6 orë."
            ]
        }
    },

}

# =========================
# TRANSLATION FUNCTIONS
# =========================

def get_lang() -> str:
    """
    Get current language from session state.
    If not set, attempts to detect from browser headers (st.context).
    Defaults to 'it'.
    """
    # Check if we already have a preference in session state
    if 'language' in st.session_state and st.session_state.language:
        return st.session_state.language
    
    # Attempt browser detection
    detected_lang = "it" # Default fallback
    try:
        # st.context.headers is available in Streamlit 1.35+
        accept_lang = st.context.headers.get("Accept-Language", "")
        if accept_lang and accept_lang.lower().startswith("en"):
            detected_lang = "en"
        elif accept_lang and accept_lang.lower().startswith("sq"):
            detected_lang = "sq"
    except (AttributeError, Exception):
        pass

    # Persist the detected language so it's consistent and saved
    st.session_state.language = detected_lang
    return detected_lang

def set_lang(lang: str):
    """Set current language in session state."""
    if lang in ('it', 'en', 'sq'):
        st.session_state.language = lang

def t(key: str, **kwargs) -> str | list | dict:
    """
    Get translated string for the given key in current language.
    
    Supports format strings with kwargs:
        t("welcome_message", id="User123")  -> "Benvenuto/a, **User123**..."
    
    Returns the translation value (string, list, or dict depending on key).
    Falls back to English if key not found for current language.
    Falls back to key itself if not found at all.
    """
    lang = get_lang()
    
    if key not in TRANSLATIONS:
        return key
    
    translation = TRANSLATIONS[key]
    
    # Get value for current language, fallback to English
    value = translation.get(lang, translation.get('en', key))
    
    # Format string if kwargs provided and value is a string
    if kwargs and isinstance(value, str):
        try:
            value = value.format(**kwargs)
        except KeyError:
            pass
    
    return value

def display_language_selector(key: str = "lang_selector"):
    """
    Renders a language selector selectbox.
    Handles getting current language, displaying options, and updating session state on change.
    
    Args:
        key (str): Unique key for the streamlit widget.
    """
    lang_options = {"it": t("italian"), "en": t("english"), "sq": t("albanian")}
    current_lang = get_lang()
    
    # Calculate index safely
    try:
        index = list(lang_options.keys()).index(current_lang)
    except ValueError:
        index = 0
        
    new_lang = st.selectbox(
        t("language"),
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=index,
        key=key,
        label_visibility="collapsed"
    )
    
    if new_lang != current_lang:
        set_lang(new_lang)
        # Clear specific session state keys to force data reload
        st.session_state.review_forms = None 
        st.rerun()
