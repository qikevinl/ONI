# ONI Academy

> Educational Platform for Neural Security

**Coming Soon** - Interactive learning resources for the ONI Framework and neural security concepts.

## Overview

ONI Academy provides structured learning paths for:

- **14-Layer Model** - Understanding the ONI architecture
- **Coherence Metric** - Signal trust and validation
- **Neural Firewall** - Security decision making
- **Attack Patterns** - Threat modeling for BCIs
- **NSAM Monitoring** - Real-time security assurance

## Installation

```bash
pip install oni-academy  # Coming soon
```

## Quick Start

```python
from oni_academy import list_modules, get_course

# See available modules
modules = list_modules()

# Get course content
intro = get_course("introduction")
```

## Brand Integration

ONI Academy uses shared brand constants from `brand.json`:

```python
from oni_academy._brand import ONI, TARA

print(ONI.full_name)  # "Open Neurosecurity Interoperability"
print(ONI.tagline)    # "The OSI of Mind"
```

## Related Projects

- **[ONI Framework](../oni-framework/)** - Core security library
- **[TARA Platform](../tara-nsec-platform/)** - Security monitoring platform

## License

Apache 2.0
