"""
NeuroSim Web UI

Streamlit-based web interface for running neural simulations
without writing code. Designed for non-technical users.

To run the UI:
    streamlit run -m neurosim.ui.app

Or use the CLI:
    neurosim ui
"""

from .app import main

__all__ = ["main"]
