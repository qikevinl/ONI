# Shared Data — Classical-Quantum Bridge

This folder contains **shared data structures** that both the Classical (ONI 14-Layer) and Quantum (QIF 7-Band Hourglass) models read from.

## As-Code Principle

Changes to files in this folder propagate to both models. This is the single source of truth for cross-model data.

| File | Purpose |
|------|---------|
| `threat-matrix.json` | Shared threat matrix — every threat maps to BOTH models |
| `bridge.py` | Validation script — ensures consistency between models |

## How It Works

```
threat-matrix.json (source of truth)
    │
    ├── config.py THREAT_MODEL    ← computed from JSON at import time
    ├── bridge.py --validate      ← checks layer↔band translations
    ├── bridge.py --model classical  ← classical-only view
    └── bridge.py --model quantum    ← quantum-only view
```

## Validation

```bash
python bridge.py --validate    # Check consistency (0 errors = pass)
python bridge.py --diff        # Show where models diverge
```

## Layer-to-Band Migration

The `V2_TO_V3_MIGRATION` map in `config.py` defines the canonical translation between Classical layers (L1-L14) and Quantum bands (S1-S3, I0, N1-N3). The bridge validation script checks that all `threat-matrix.json` entries are consistent with this mapping.
