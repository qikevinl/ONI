#!/usr/bin/env python3
"""
Generate threat-registry.json from config.py (as-code).

Source of truth: src/config.py → THREAT_MODEL, THREAT_TACTICS
Outputs:
  1. viz/threat-registry.json  — standalone, referenceable from GitHub
  2. Updates qif-architecture-v4.json with "threat_registry" section

Usage:
  python generate_threat_registry.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.config import THREAT_MODEL, THREAT_TACTICS

def build_registry():
    """Build the threat registry JSON structure from config.py."""
    tactics = []
    for t in THREAT_TACTICS:
        tactics.append({
            "id": t["id"],
            "name": t["name"],
            "mitre_native": t["mitre"],
            "description": t["description"],
        })

    techniques = []
    for entry in THREAT_MODEL:
        tech = {
            "id": entry["id"],
            "attack": entry["attack"],
            "category": entry["category"],
            "bands": entry["bands"],
            "band_ids": entry["band_ids"],
            "coupling": entry.get("coupling"),
            "access": entry.get("access"),
            "classical": entry["classical"],
            "quantum": entry["quantum"],
            "mitre": entry.get("mitre", {}),
            "sources": entry.get("sources", []),
            "status": entry["status"],
            "notes": entry["notes"],
            "legacy_ids": entry.get("legacy_ids", []),
        }
        techniques.append(tech)

    # Stats
    by_tactic = {}
    by_status = {}
    for t in techniques:
        cat = t["category"]
        by_tactic[cat] = by_tactic.get(cat, 0) + 1
        st = t["status"]
        by_status[st] = by_status.get(st, 0) + 1

    return {
        "threat_registry": {
            "version": "1.0",
            "generated_from": "qif-lab/src/config.py",
            "framework": "QIF (Quantum Indeterministic Framework for Neural Security)",
            "mitre_compatibility": {
                "id_range": "T2001-T2899 (avoids collision with MITRE ATT&CK T1001-T1659)",
                "tactic_ids": "Standard MITRE TA#### where applicable, TA0050-TA0053 for BCI-specific",
                "note": "Designed for future MITRE collaboration — our IDs can be adopted or cross-referenced without conflict."
            },
            "statistics": {
                "total_techniques": len(techniques),
                "total_tactics": len(tactics),
                "by_tactic": by_tactic,
                "by_status": by_status,
            },
            "tactics": tactics,
            "techniques": techniques,
            "deprecated": [
                {
                    "file": "shared/threat-matrix.json",
                    "reason": "Legacy ONI-era threat matrix (24 techniques, ONI-T### IDs). Superseded by this registry.",
                    "migration": "All ONI-T### techniques merged into T2000+ range. See legacy_ids field on each technique."
                }
            ]
        }
    }


def main():
    registry = build_registry()

    # 1. Write standalone threat-registry.json
    standalone_path = ROOT / "viz" / "threat-registry.json"
    with open(standalone_path, "w") as f:
        json.dump(registry["threat_registry"], f, indent=2, ensure_ascii=False)
    print(f"Wrote {standalone_path} ({len(THREAT_MODEL)} techniques, {len(THREAT_TACTICS)} tactics)")

    # 2. Update qif-architecture-v4.json
    v4_path = ROOT / "qif-architecture-v4.json"
    if v4_path.exists():
        with open(v4_path) as f:
            v4 = json.load(f)

        v4["threat_registry"] = registry["threat_registry"]
        with open(v4_path, "w") as f:
            json.dump(v4, f, indent=2, ensure_ascii=False)
        print(f"Updated {v4_path} with threat_registry section")
    else:
        print(f"Warning: {v4_path} not found, skipping v4 update")

    print("Done.")


if __name__ == "__main__":
    main()
