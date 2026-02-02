"""
QIF Configuration — Single source of truth for all constants, thresholds, and metadata.

As-Code Principle: Every value used in the whitepaper, equations, or visualizations
is defined HERE. Nothing is hardcoded in documents.
"""

# ──────────────────────────────────────────────
# Framework Identity
# ──────────────────────────────────────────────

FRAMEWORK = {
    "name": "QIF — Quantum Indeterministic Framework for Neural Security",
    "pronunciation": "CHIEF",
    "predecessor": "ONI (Organic Neural Interface)",
    "layer_model_version": "v3.0 (Hourglass)",
    "layer_model_date": "2026-02-02",
    "github": "qinnovates/qinnovate",
    "authors": "Kevin Qi, with Claude (Anthropic)",
    "collaboration": "Quantum Intelligence (QI)",
}

# ──────────────────────────────────────────────
# Layer Architecture — v3.0 Hourglass Model
# ──────────────────────────────────────────────
# 3 Zones, 8 Bands. No OSI heritage.
# Numbers increase AWAY from the interface in both directions.
# Width = state space / possibility space (hourglass geometry).

ZONES = {
    "neural": {
        "name": "Neural Domain",
        "description": "Quantum-dominant: biological processing from subcortical relay to consciousness",
        "color": "#3fb950",  # green
        "bands": ["N1", "N2", "N3", "N4"],
    },
    "interface": {
        "name": "Interface Zone",
        "description": "Quasi-quantum bottleneck: electrode-tissue boundary, measurement/collapse",
        "color": "#f85149",  # red
        "bands": ["I0"],
    },
    "silicon": {
        "name": "Silicon Domain",
        "description": "Classical: analog front-end through digital processing to application software",
        "color": "#58a6ff",  # blue
        "bands": ["S1", "S2", "S3"],
    },
}

BANDS = [
    {
        "id": "N4", "name": "Identity & Consciousness", "zone": "neural",
        "description": "Executive function, agency, sense of self",
        "determinacy": "Quantum Indeterminate",
        "qi_range": (0.9, 1.0),
        "brain_regions": ["PFC (executive)", "anterior cingulate"],
        "hourglass_width": 1.0,  # widest in neural domain
    },
    {
        "id": "N3", "name": "Cognitive Integration", "zone": "neural",
        "description": "Decisions, language, memory encoding, emotion",
        "determinacy": "Quantum Uncertain",
        "qi_range": (0.7, 0.9),
        "brain_regions": ["PFC (decisions)", "Broca", "Wernicke", "HIPP", "amygdala"],
        "hourglass_width": 0.8,
    },
    {
        "id": "N2", "name": "Sensorimotor Processing", "zone": "neural",
        "description": "Primary motor/sensory cortices, movement planning",
        "determinacy": "Chaotic → Stochastic",
        "qi_range": (0.4, 0.7),
        "brain_regions": ["M1", "S1", "V1", "A1", "PMC", "SMA"],
        "hourglass_width": 0.55,
    },
    {
        "id": "N1", "name": "Subcortical Relay", "zone": "neural",
        "description": "Sensory gating, motor selection, coordination, arousal",
        "determinacy": "Stochastic",
        "qi_range": (0.2, 0.4),
        "brain_regions": ["thalamus", "basal ganglia", "cerebellum", "brainstem"],
        "hourglass_width": 0.35,
    },
    {
        "id": "I0", "name": "Neural Interface", "zone": "interface",
        "description": "Electrode-tissue boundary, measurement/collapse, quasi-quantum zone",
        "determinacy": "Quasi-quantum (ΓD ∈ (0,1))",
        "qi_range": (0.1, 0.3),
        "brain_regions": [],
        "hourglass_width": 0.2,  # narrowest — bottleneck
    },
    {
        "id": "S1", "name": "Analog Front-End", "zone": "silicon",
        "description": "Amplification, filtering, ADC/DAC conversion",
        "determinacy": "Stochastic (analog noise)",
        "qi_range": (0.01, 0.1),
        "brain_regions": [],
        "hourglass_width": 0.35,
    },
    {
        "id": "S2", "name": "Digital Processing", "zone": "silicon",
        "description": "Decoding algorithms, classification, feature extraction",
        "determinacy": "Deterministic",
        "qi_range": (0.0, 0.0),
        "brain_regions": [],
        "hourglass_width": 0.7,
    },
    {
        "id": "S3", "name": "Application", "zone": "silicon",
        "description": "Clinical software, user interface, data storage, networking",
        "determinacy": "Deterministic",
        "qi_range": (0.0, 0.0),
        "brain_regions": [],
        "hourglass_width": 1.0,  # widest in silicon domain
    },
]

# Quick lookup: band_id → band dict
BANDS_BY_ID = {b["id"]: b for b in BANDS}

# ──────────────────────────────────────────────
# Brain Region → Band Mapping
# ──────────────────────────────────────────────

BRAIN_REGION_MAP = {
    "PFC (executive)":    {"band": "N4", "connections": ["N3", "N2"]},
    "anterior cingulate": {"band": "N4", "connections": ["N3"]},
    "PFC (decisions)":    {"band": "N3", "connections": ["N4", "N2", "N1"]},
    "Broca":              {"band": "N3", "connections": ["Wernicke", "PFC (decisions)"]},
    "Wernicke":           {"band": "N3", "connections": ["A1", "Broca", "PFC (decisions)"]},
    "HIPP":               {"band": "N3", "connections": ["N1", "PFC (decisions)"]},
    "amygdala":           {"band": "N3", "connections": ["N1", "PFC (decisions)"]},
    "M1":                 {"band": "N2", "connections": ["PFC (decisions)", "PMC", "SMA", "basal ganglia"]},
    "S1":                 {"band": "N2", "connections": ["thalamus", "PFC (decisions)"]},
    "V1":                 {"band": "N2", "connections": ["thalamus"]},
    "A1":                 {"band": "N2", "connections": ["thalamus", "Wernicke"]},
    "PMC":                {"band": "N2", "connections": ["PFC (decisions)", "M1"]},
    "SMA":                {"band": "N2", "connections": ["PFC (decisions)", "M1"]},
    "thalamus":           {"band": "N1", "connections": ["S1", "V1", "A1", "PFC (decisions)"]},
    "basal ganglia":      {"band": "N1", "connections": ["M1", "PFC (decisions)"]},
    "cerebellum":         {"band": "N1", "connections": ["M1", "thalamus"]},
    "brainstem":          {"band": "N1", "connections": ["thalamus", "cerebellum"]},
}

# ──────────────────────────────────────────────
# Determinacy Spectrum (5 levels, mapped to bands)
# ──────────────────────────────────────────────

DETERMINACY_SPECTRUM = [
    {"level": 1, "name": "Deterministic",         "bands": ["S2", "S3"],  "description": "f(state,t) → next_state, no randomness"},
    {"level": 2, "name": "Stochastic",            "bands": ["S1", "N1"],  "description": "Known probability distributions, epistemic randomness"},
    {"level": 3, "name": "Chaotic",               "bands": ["N2"],        "description": "Deterministic but sensitive to initial conditions (λ_L > 0)"},
    {"level": 4, "name": "Quantum Uncertain",     "bands": ["N3"],        "description": "Heisenberg-bounded, ontic randomness (Bell's theorem)"},
    {"level": 5, "name": "Quantum Indeterminate",  "bands": ["N4"],        "description": "Robertson-Schrödinger, entangled, contextual"},
]

# ──────────────────────────────────────────────
# v2.0 → v3.0 Migration Map
# ──────────────────────────────────────────────

V2_TO_V3_MIGRATION = {
    "L1":  "S3",   # Physical medium → Application (classical networking)
    "L2":  "S3",   # Data Link → Application
    "L3":  "S3",   # Network → Application
    "L4":  "S3",   # Transport → Application
    "L5":  "S3",   # Session → Application
    "L6":  "S3",   # Presentation → Application
    "L7":  "S3",   # Application → Application
    "L8":  "I0",   # Neural Gateway → Neural Interface
    "L9":  "I0/N1",  # Signal Processing → Interface / Subcortical
    "L10": "N1/N2",  # Neural Protocol → Subcortical / Sensorimotor
    "L11": "N2",   # Cognitive Transport → Sensorimotor Processing
    "L12": "N3",   # Cognitive Session → Cognitive Integration
    "L13": "N3",   # Semantic Layer → Cognitive Integration
    "L14": "N4",   # Identity Layer → Identity & Consciousness
}

# DEPRECATED v2.0 — kept for migration reference only. Do NOT use in new code.
LAYERS_V2_DEPRECATED = [
    {"layer": 1,  "name": "Physical",           "domain": "OSI",    "description": "Physical medium, cabling"},
    {"layer": 2,  "name": "Data Link",           "domain": "OSI",    "description": "MAC addressing, framing"},
    {"layer": 3,  "name": "Network",             "domain": "OSI",    "description": "IP routing, addressing"},
    {"layer": 4,  "name": "Transport",           "domain": "OSI",    "description": "TCP/UDP, flow control"},
    {"layer": 5,  "name": "Session",             "domain": "OSI",    "description": "Connection management"},
    {"layer": 6,  "name": "Presentation",        "domain": "OSI",    "description": "Encryption, formatting"},
    {"layer": 7,  "name": "Application",         "domain": "OSI",    "description": "User-facing protocols"},
    {"layer": 8,  "name": "Neural Gateway",      "domain": "Neural", "description": "Firewall, trust boundary between silicon and biology"},
    {"layer": 9,  "name": "Signal Processing",   "domain": "Neural", "description": "Raw signal conditioning, phase coherence checking"},
    {"layer": 10, "name": "Neural Protocol",      "domain": "Neural", "description": "Oscillatory encoding, synchronization"},
    {"layer": 11, "name": "Cognitive Transport",   "domain": "Neural", "description": "Reliable neural data delivery"},
    {"layer": 12, "name": "Cognitive Session",     "domain": "Neural", "description": "Context, working memory"},
    {"layer": 13, "name": "Semantic Layer",        "domain": "Neural", "description": "Intent, goals, meaning"},
    {"layer": 14, "name": "Identity Layer",        "domain": "Neural", "description": "Agency, sense of self"},
]

# ──────────────────────────────────────────────
# Coherence Metric Thresholds
# ──────────────────────────────────────────────

COHERENCE_THRESHOLDS = {
    "high": 0.6,
    "low": 0.3,
}

DECISION_MATRIX = [
    {"coherence": "High (Cₛ > 0.6)",          "auth": "Valid",   "action": "ACCEPT"},
    {"coherence": "High (Cₛ > 0.6)",          "auth": "Invalid", "action": "REJECT + ALERT"},
    {"coherence": "Medium (0.3 < Cₛ < 0.6)",  "auth": "Valid",   "action": "ACCEPT + FLAG"},
    {"coherence": "Medium (0.3 < Cₛ < 0.6)",  "auth": "Invalid", "action": "REJECT + ALERT"},
    {"coherence": "Low (Cₛ < 0.3)",           "auth": "Any",     "action": "REJECT + CRITICAL"},
]

# ──────────────────────────────────────────────
# Scale-Frequency Data
# ──────────────────────────────────────────────

FREQUENCY_BANDS = [
    {"band": "High gamma", "freq_range": "60-100 Hz", "freq_mid": 80,   "spatial_extent": "0.3-5 mm",    "spatial_mid_m": 0.0025,  "fxs": "~0.08-0.4",  "source": "Jia et al. 2011"},
    {"band": "Low gamma",  "freq_range": "30-60 Hz",  "freq_mid": 45,   "spatial_extent": "1-10 mm",     "spatial_mid_m": 0.005,   "fxs": "~0.04-0.4",  "source": "ECoG studies"},
    {"band": "Alpha",      "freq_range": "8-12 Hz",   "freq_mid": 10,   "spatial_extent": "10-20 cm",    "spatial_mid_m": 0.15,    "fxs": "1-2",        "source": "Srinivasan 1999"},
    {"band": "Theta",      "freq_range": "4-8 Hz",    "freq_mid": 6,    "spatial_extent": "4-5 cm",      "spatial_mid_m": 0.045,   "fxs": "0.24-0.40",  "source": "Patel et al. 2012"},
    {"band": "Delta",      "freq_range": "0.5-4 Hz",  "freq_mid": 2,    "spatial_extent": "15-20 cm",    "spatial_mid_m": 0.175,   "fxs": "0.15-0.20",  "source": "Massimini 2004"},
]

CONDUCTION_VELOCITIES = [
    {"fiber_type": "Unmyelinated intracortical", "velocity": "0.1-0.5 m/s"},
    {"fiber_type": "Myelinated corticocortical", "velocity": "5-30 m/s"},
    {"fiber_type": "Nunez canonical model",      "velocity": "~7 m/s"},
]

BRAIN_MAX_DIMENSION_CM = 20  # Human brain max ~15-20 cm
BRAIN_MAX_DIMENSION_M = 0.20  # Same, in meters (for equations)

# ──────────────────────────────────────────────
# Quantum Computing Threats
# ──────────────────────────────────────────────

QUANTUM_THREATS = [
    {"claim": "Shor's breaks RSA-2048",    "value": "~8 hours / 20M noisy qubits",          "source": "Gidney & Ekerå 2019, arXiv:1905.09749"},
    {"claim": "Revised qubit estimate",     "value": "<1M noisy qubits / <1 week",           "source": "Gidney 2025, arXiv:2505.15917"},
    {"claim": "Classical RSA-2048 time",    "value": "Hundreds of trillions of years",        "source": "GNFS complexity"},
    {"claim": "AES-256 quantum resistance", "value": "Theoretically halved; practically safe", "source": "NIST guidance"},
    {"claim": "Grover's optimality",        "value": "O(√N) provably optimal",                "source": "Bennett et al. 1997, Zalka 1999"},
]

# ──────────────────────────────────────────────
# Neuralink N1 Specs
# ──────────────────────────────────────────────

NEURALINK_N1 = {
    "electrodes": 1024,
    "threads": 64,
    "sampling_rate_khz": "19.3-20",
    "wireless": "Bluetooth Low Energy (BLE)",
    "power_mw": 24.7,
    "soc_area_mm": "5×4",
}

# ──────────────────────────────────────────────
# Neuroscience Constants
# ──────────────────────────────────────────────

NEURO_CONSTANTS = [
    {"claim": "Retinal output",             "value": "~10 Mbps",              "source": "Koch et al. 2006"},
    {"claim": "Conscious visual bandwidth",  "value": "~20-50 bits/sec",       "source": "Nørretranders 1998"},
    {"claim": "Compression ratio",           "value": "~200,000:1 to 500,000:1", "source": "Derived"},
    {"claim": "STDP LTP window",             "value": "Pre leads post by 0-20 ms", "source": "Markram 1997, Bi & Poo 1998"},
    {"claim": "Cortical synaptic Pr (in vivo)", "value": "~0.1-0.5",           "source": "Borst 2010"},
    {"claim": "Human brain max dimension",   "value": "~15-20 cm",             "source": "Anatomy"},
]

# ──────────────────────────────────────────────
# Decoherence Timescales
# ──────────────────────────────────────────────

DECOHERENCE_CAMPS = [
    {"camp": "Tegmark (skeptic)",    "tau_d": 1e-13,  "label": "10⁻¹³ s", "implication": "Quantum effects impossible in biology"},
    {"camp": "Recent experimental",  "tau_d": 1e-5,   "label": "10⁻⁵ s",  "implication": "Possible microsecond quantum window"},
    {"camp": "Fisher (optimist)",    "tau_d": 3600.0,  "label": "Hours",    "implication": "Nuclear spin coherence in Posner molecules"},
]

# ──────────────────────────────────────────────
# Default QI Equation Parameters
# ──────────────────────────────────────────────

DEFAULT_C1_PARAMS = {
    "alpha": 1.0,
    "beta": 1.0,
    "gamma": 0.5,
    "delta": 0.5,
    "tau_d": 1e-5,
}

DEFAULT_C2_PARAMS = {
    "lam": 1.0,
    "mu": 1.0,
}

# ──────────────────────────────────────────────
# Threat Model
# ──────────────────────────────────────────────

THREAT_MODEL = [
    {"attack": "Signal injection",            "bands": "I0–N1",  "classical": "Yes",     "quantum": "Enhanced (coherence metric)"},
    {"attack": "Neural ransomware",           "bands": "N3",     "classical": "Partial",  "quantum": "Yes (QI score drop)"},
    {"attack": "Eavesdropping",               "bands": "I0–N1",  "classical": "No",       "quantum": "Yes (Heisenberg disturbance)"},
    {"attack": "Man-in-the-middle",           "bands": "I0",     "classical": "Partial",  "quantum": "Yes (no-cloning + Bell test)"},
    {"attack": "Quantum tunneling exploit",   "bands": "I0–N1",  "classical": "No",       "quantum": "Yes (tunneling profile anomaly)"},
    {"attack": "Davydov soliton attack",      "bands": "I0–N1",  "classical": "No",       "quantum": "Yes (tunneling term Qtunnel)"},
    {"attack": "Harvest-now-decrypt-later",   "bands": "S3",     "classical": "No",       "quantum": "Prevented (QKD)"},
    {"attack": "Identity spoofing",           "bands": "N4",     "classical": "Partial",  "quantum": "Yes (quantum biometric)"},
]
