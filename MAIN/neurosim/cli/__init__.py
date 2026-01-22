"""
NeuroSim Command-Line Interface

Provides command-line access to NeuroSim functionality:
- Run simulations from configuration files
- Launch the web UI
- Export simulation data
"""

from .main import main, cli

__all__ = ["main", "cli"]
