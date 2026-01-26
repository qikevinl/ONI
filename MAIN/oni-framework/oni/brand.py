"""
ONI Framework Brand Constants

Single source of truth for project naming, slogans, and mission statements.
Import from here to ensure consistency across all documentation and code.

Usage:
    from oni.brand import ONI, TARA
    print(ONI.name)  # "ONI Framework"
    print(TARA.slogan)  # "Protection for the neural frontier"
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ProjectBrand:
    """Immutable brand identity for a project."""
    acronym: str
    full_name: str
    name: str
    slogan: str
    mission: str
    tagline: Optional[str] = None
    description: Optional[str] = None


# =============================================================================
# ONI Framework
# =============================================================================

ONI = ProjectBrand(
    acronym="ONI",
    full_name="Open Neurocomputing Interface",
    name="ONI Framework",
    tagline="The OSI of Mind",
    slogan="Our minds. Our rules. Our future.",
    mission=(
        "The mind is the last frontier. We're making sure it's protected "
        "from day one — with a universal, open standard that leaves no brain behind."
    ),
    description=(
        "A unified 14-layer model extending OSI into the biological domain. "
        "One framework to understand, build, and secure brain-computer interfaces. "
        "Open. Extensible. Universal."
    ),
)


# =============================================================================
# TARA Platform
# =============================================================================

TARA = ProjectBrand(
    acronym="TARA",
    full_name="Telemetry Analysis and Response Automation",
    name="TARA Platform",
    tagline="Protection for the neural frontier",
    slogan="Named after the Buddhist goddess of protection.",
    mission=(
        "Provide real-time neural security monitoring, attack simulation, "
        "and response automation aligned with the ONI 14-layer model."
    ),
    description=(
        "A neural security platform for BCI monitoring, simulation, and attack testing. "
        "Real-time security analysis for brain-computer interfaces."
    ),
)


# =============================================================================
# Combined Export
# =============================================================================

BRANDS = {
    "oni": ONI,
    "tara": TARA,
}


def get_brand(name: str) -> ProjectBrand:
    """Get brand by name (case-insensitive)."""
    return BRANDS[name.lower()]


# =============================================================================
# Version Info (updated with releases)
# =============================================================================

ONI_VERSION = "0.2.0"
TARA_VERSION = "0.8.0"


# =============================================================================
# Quick Access Strings
# =============================================================================

# For documentation headers
ONI_HEADER = f"{ONI.name} — {ONI.tagline}"
TARA_HEADER = f"{TARA.name} — {TARA.tagline}"

# For footers/credits
ONI_FOOTER = f"{ONI.name} | {ONI.slogan}"
TARA_FOOTER = f"{TARA.name} | {TARA.slogan}"
