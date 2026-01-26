"""
TARA UI Design System
======================

Dark, futuristic, cyberpunk aesthetic for the Neural Security Operations Center.
"""

# Color Palette - Cyberpunk Neon
COLORS = {
    "bg": "#0a0a0f",
    "bg_alt": "#0d0d14",
    "surface": "#12121a",
    "surface_alt": "#1a1a24",
    "border": "#2a2a3a",
    "border_light": "#3a3a4a",
    "text": "#e2e8f0",
    "text_secondary": "#94a3b8",
    "text_muted": "#64748b",
    "primary": "#00f0ff",       # Cyan neon
    "primary_dim": "#00a8b3",
    "secondary": "#ff00ff",     # Magenta neon
    "secondary_dim": "#b300b3",
    "accent": "#00ff88",        # Green neon
    "accent_dim": "#00b35f",
    "warning": "#ffaa00",       # Orange
    "error": "#ff4444",         # Red
    "safe": "#00ff88",          # Green
}

# CSS Styles
GLOBAL_CSS = """
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

    /* Root variables */
    :root {
        --tara-bg: #0a0a0f;
        --tara-surface: #12121a;
        --tara-surface-alt: #1a1a24;
        --tara-border: #2a2a3a;
        --tara-text: #e2e8f0;
        --tara-text-muted: #64748b;
        --tara-primary: #00f0ff;
        --tara-secondary: #ff00ff;
        --tara-accent: #00ff88;
        --tara-glow-cyan: 0 0 20px rgba(0, 240, 255, 0.5);
        --tara-glow-magenta: 0 0 20px rgba(255, 0, 255, 0.5);
        --tara-glow-green: 0 0 20px rgba(0, 255, 136, 0.5);
    }

    /* Global dark theme */
    .stApp {
        font-family: 'Fira Code', 'JetBrains Mono', monospace;
        background: linear-gradient(180deg, #0a0a0f 0%, #0d0d14 50%, #0a0a0f 100%);
        background-attachment: fixed;
    }

    /* Scanline overlay effect */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(0, 0, 0, 0.1) 2px,
            rgba(0, 0, 0, 0.1) 4px
        );
        pointer-events: none;
        z-index: 9999;
        opacity: 0.3;
    }

    /* Main content styling */
    .main .block-container {
        background: rgba(18, 18, 26, 0.95);
        border: 1px solid rgba(0, 240, 255, 0.1);
        border-radius: 12px;
        padding: 2rem;
        margin: 0.5rem;
    }

    /* Override text colors */
    .stApp, .stApp p, .stApp span, .stApp div {
        color: #e2e8f0 !important;
    }

    .stApp h1, .stApp h2, .stApp h3 {
        font-family: 'Orbitron', sans-serif;
        color: #00f0ff !important;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d0d14 0%, #12121a 100%);
        border-right: 1px solid rgba(0, 240, 255, 0.2);
    }

    [data-testid="stSidebar"] .stMarkdown {
        color: #e2e8f0;
    }

    /* TARA specific components */
    .tara-header {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.05) 0%, rgba(255, 0, 255, 0.05) 100%);
        border: 1px solid rgba(0, 240, 255, 0.2);
        border-radius: 16px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .tara-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #00f0ff, #ff00ff, #00ff88);
        animation: scan 3s linear infinite;
    }

    @keyframes scan {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    .tara-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00f0ff 0%, #ff00ff 50%, #00ff88 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        text-shadow: 0 0 30px rgba(0, 240, 255, 0.5);
    }

    .tara-subtitle {
        font-size: 1rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-top: 0.5rem;
    }

    /* Status cards */
    .tara-card {
        background: rgba(18, 18, 26, 0.8);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 240, 255, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .tara-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00f0ff, transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .tara-card:hover {
        border-color: rgba(0, 240, 255, 0.5);
        box-shadow: 0 0 30px rgba(0, 240, 255, 0.15);
    }

    .tara-card:hover::before {
        opacity: 1;
    }

    .tara-card-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #64748b;
        margin-bottom: 0.5rem;
    }

    .tara-card-value {
        font-family: 'Fira Code', monospace;
        font-size: 2rem;
        font-weight: 600;
        color: #00f0ff;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
    }

    .tara-card-value.success {
        color: #00ff88;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
    }

    .tara-card-value.warning {
        color: #ffaa00;
        text-shadow: 0 0 10px rgba(255, 170, 0, 0.3);
    }

    .tara-card-value.error {
        color: #ff4444;
        text-shadow: 0 0 10px rgba(255, 68, 68, 0.3);
    }

    /* Metric displays */
    .tara-metric {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 1.5rem;
        background: rgba(18, 18, 26, 0.6);
        border: 1px solid rgba(0, 240, 255, 0.15);
        border-radius: 12px;
    }

    .tara-metric-value {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: #00f0ff;
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
    }

    .tara-metric-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        color: #64748b;
        margin-top: 0.5rem;
    }

    /* Alert styles */
    .tara-alert {
        background: rgba(255, 68, 68, 0.1);
        border: 1px solid rgba(255, 68, 68, 0.3);
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }

    .tara-alert.warning {
        background: rgba(255, 170, 0, 0.1);
        border-color: rgba(255, 170, 0, 0.3);
    }

    .tara-alert.info {
        background: rgba(0, 240, 255, 0.1);
        border-color: rgba(0, 240, 255, 0.3);
    }

    .tara-alert.success {
        background: rgba(0, 255, 136, 0.1);
        border-color: rgba(0, 255, 136, 0.3);
    }

    /* Console/terminal style */
    .tara-console {
        background: #0a0a0f;
        border: 1px solid #2a2a3a;
        border-radius: 8px;
        padding: 1rem;
        font-family: 'Fira Code', monospace;
        font-size: 0.875rem;
        color: #00ff88;
        line-height: 1.6;
        overflow-x: auto;
    }

    .tara-console .prompt {
        color: #00f0ff;
    }

    .tara-console .output {
        color: #e2e8f0;
    }

    .tara-console .error {
        color: #ff4444;
    }

    /* Layer visualization */
    .tara-layer {
        display: flex;
        align-items: center;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 8px;
        background: rgba(18, 18, 26, 0.6);
        border: 1px solid transparent;
        transition: all 0.2s ease;
    }

    .tara-layer:hover {
        border-color: rgba(0, 240, 255, 0.3);
        transform: translateX(4px);
    }

    .tara-layer-silicon {
        border-left: 3px solid #00f0ff;
    }

    .tara-layer-bridge {
        border-left: 3px solid #ffaa00;
    }

    .tara-layer-biology {
        border-left: 3px solid #00ff88;
    }

    .tara-layer-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 0.75rem;
        color: #64748b;
        width: 40px;
    }

    .tara-layer-name {
        font-weight: 600;
        color: #e2e8f0;
        flex: 1;
    }

    .tara-layer-status {
        font-size: 0.75rem;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        background: rgba(0, 255, 136, 0.2);
        color: #00ff88;
    }

    .tara-layer-status.warning {
        background: rgba(255, 170, 0, 0.2);
        color: #ffaa00;
    }

    .tara-layer-status.error {
        background: rgba(255, 68, 68, 0.2);
        color: #ff4444;
    }

    /* Progress bars */
    .tara-progress {
        background: rgba(42, 42, 58, 0.8);
        border-radius: 4px;
        height: 8px;
        overflow: hidden;
    }

    .tara-progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #00f0ff, #00ff88);
        border-radius: 4px;
        transition: width 0.3s ease;
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.1), rgba(255, 0, 255, 0.1)) !important;
        border: 1px solid rgba(0, 240, 255, 0.3) !important;
        color: #00f0ff !important;
        font-family: 'Orbitron', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(0, 240, 255, 0.2), rgba(255, 0, 255, 0.2)) !important;
        border-color: rgba(0, 240, 255, 0.6) !important;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.3) !important;
    }

    /* Select boxes and inputs */
    .stSelectbox > div > div {
        background: rgba(18, 18, 26, 0.8) !important;
        border: 1px solid rgba(0, 240, 255, 0.2) !important;
        color: #e2e8f0 !important;
    }

    .stTextInput > div > div > input {
        background: rgba(18, 18, 26, 0.8) !important;
        border: 1px solid rgba(0, 240, 255, 0.2) !important;
        color: #e2e8f0 !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(18, 18, 26, 0.6) !important;
        border: 1px solid rgba(0, 240, 255, 0.15) !important;
        border-radius: 8px !important;
        color: #e2e8f0 !important;
    }

    /* DataFrames */
    .stDataFrame {
        background: rgba(18, 18, 26, 0.8) !important;
    }

    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Animated grid background */
    .tara-grid-bg {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image:
            linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: -1;
    }
</style>
"""


def inject_styles():
    """Inject global CSS styles into the Streamlit app."""
    import streamlit as st
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def header_section(title: str = "TARA", subtitle: str = "Neural Security Operations Center"):
    """Create a cyberpunk header section."""
    import streamlit as st
    html = f"""
    <div class="tara-header">
        <h1 class="tara-title">{title}</h1>
        <p class="tara-subtitle">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def status_card(title: str, value: str, status: str = "normal"):
    """Create a status card with neon styling."""
    import streamlit as st
    status_class = ""
    if status == "success":
        status_class = " success"
    elif status == "warning":
        status_class = " warning"
    elif status == "error":
        status_class = " error"

    html = f"""
    <div class="tara-card">
        <div class="tara-card-title">{title}</div>
        <div class="tara-card-value{status_class}">{value}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def metric_display(value: str, label: str):
    """Create a large metric display."""
    import streamlit as st
    html = f"""
    <div class="tara-metric">
        <div class="tara-metric-value">{value}</div>
        <div class="tara-metric-label">{label}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def layer_item(number: int, name: str, status: str = "active", domain: str = "silicon"):
    """Create a layer visualization item."""
    import streamlit as st
    domain_class = f"tara-layer-{domain}"
    status_class = ""
    if status == "warning":
        status_class = " warning"
    elif status == "error":
        status_class = " error"

    html = f"""
    <div class="tara-layer {domain_class}">
        <span class="tara-layer-number">L{number}</span>
        <span class="tara-layer-name">{name}</span>
        <span class="tara-layer-status{status_class}">{status.upper()}</span>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def console_output(lines: list):
    """Create a terminal/console style output."""
    import streamlit as st
    formatted_lines = []
    for line in lines:
        if line.startswith(">"):
            formatted_lines.append(f'<span class="prompt">{line}</span>')
        elif line.startswith("ERROR"):
            formatted_lines.append(f'<span class="error">{line}</span>')
        else:
            formatted_lines.append(f'<span class="output">{line}</span>')

    content = "<br>".join(formatted_lines)
    html = f'<div class="tara-console">{content}</div>'
    st.markdown(html, unsafe_allow_html=True)


def alert_box(message: str, alert_type: str = "error"):
    """Create an alert box."""
    import streamlit as st
    html = f'<div class="tara-alert {alert_type}">{message}</div>'
    st.markdown(html, unsafe_allow_html=True)
