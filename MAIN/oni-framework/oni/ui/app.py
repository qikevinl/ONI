"""
ONI Academy - Interactive Learning Platform
============================================

A clean, minimal, futuristic interface for learning neural security.
Designed to make BCI security concepts accessible to everyone.

Launch with:
    oni ui
    # or
    streamlit run oni/ui/app.py
"""

import streamlit as st
from pathlib import Path

# Page configuration - must be first
st.set_page_config(
    page_title="ONI Academy",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Import styles
try:
    from .styles import inject_styles, hero_section, section_header, feature_card, metric_card, info_box
except ImportError:
    from styles import inject_styles, hero_section, section_header, feature_card, metric_card, info_box

# Inject global CSS
inject_styles()


def main():
    """Main application entry point."""
    # Initialize session state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"
    if "learning_progress" not in st.session_state:
        st.session_state.learning_progress = {}

    # Render sidebar
    render_sidebar()

    # Route to current page
    pages = {
        "Home": render_home,
        "What is ONI?": render_what_is_oni,
        "The 14 Layers": render_layers,
        "Signal Trust": render_coherence,
        "Neural Firewall": render_firewall,
        "Privacy": render_privacy,
        "Threat Detection": render_threats,
        "Interactive Lab": render_interactive_lab,
        "Code Examples": render_code_lab,
        "Research": render_research,
        "Glossary": render_glossary,
    }

    page_func = pages.get(st.session_state.current_page, render_home)
    page_func()


def render_sidebar():
    """Render the navigation sidebar - clean, no emojis."""
    with st.sidebar:
        # Logo and title
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <div style="font-size: 1.5rem; font-weight: 700; background: linear-gradient(135deg, #3b82f6, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">ONI Academy</div>
            <div style="font-size: 0.75rem; color: #64748b; margin-top: 0.25rem;">Neural Security Learning</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Learning Path section
        st.markdown('<p style="font-size: 0.75rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">Learning Path</p>', unsafe_allow_html=True)

        nav_items = [
            "Home",
            "What is ONI?",
            "The 14 Layers",
            "Signal Trust",
            "Neural Firewall",
            "Privacy",
            "Threat Detection",
        ]

        for page in nav_items:
            is_active = st.session_state.current_page == page
            if st.button(
                page,
                key=f"nav_{page}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.current_page = page
                st.rerun()

        st.markdown("---")

        # Resources section
        st.markdown('<p style="font-size: 0.75rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">Resources</p>', unsafe_allow_html=True)

        resource_items = [
            "Interactive Lab",
            "Code Examples",
            "Research",
            "Glossary",
        ]

        for page in resource_items:
            is_active = st.session_state.current_page == page
            if st.button(
                page,
                key=f"nav_{page}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.current_page = page
                st.rerun()

        st.markdown("---")

        # Version and links
        try:
            from oni import __version__
            version = __version__
        except:
            version = "0.2.1"

        st.markdown(f"""
        <div style="text-align: center; font-size: 0.7rem; color: #94a3b8;">
            <div>v{version}</div>
            <div style="margin-top: 0.5rem;">
                <a href="https://github.com/qikevinl/ONI" style="color: #64748b; text-decoration: none;">GitHub</a> ·
                <a href="https://pypi.org/project/oni-framework/" style="color: #64748b; text-decoration: none;">PyPI</a>
            </div>
        </div>
        """, unsafe_allow_html=True)


def navigate_to(page):
    """Helper function to navigate to a page."""
    st.session_state.current_page = page
    st.rerun()


def render_home():
    """Home page - the landing experience with clickable cards."""
    hero_section(
        "ONI Academy",
        "Master Neural Security",
        "Learn to protect brain-computer interfaces with the world's first comprehensive BCI security framework."
    )

    # What is ONI - improved intro box
    st.markdown("""
    <div class="oni-info-box" style="margin: 1.5rem 0;">
        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem;">
            <span style="font-size: 1.5rem;">🧠</span>
            <span style="font-size: 1.1rem; font-weight: 600; color: #f8fafc;">What is ONI?</span>
        </div>
        <div style="color: #94a3b8; line-height: 1.7;">
            <strong style="color: #6366f1;">ONI (Open Neurosecurity Interoperability)</strong> is a 14-layer security framework that extends
            the OSI networking model into the biological domain. It provides the first comprehensive
            standard for securing brain-computer interfaces against attacks on confidentiality, integrity,
            and availability of neural signals.
        </div>
    </div>
    """, unsafe_allow_html=True)

    section_header("Start Learning", "Click any topic to begin")

    # Card grid - build complete HTML in one call
    st.markdown("""
    <div class="oni-card-grid">
        <div class="oni-card">
            <div class="oni-card-icon">🔷</div>
            <div class="oni-card-title">The 14-Layer Model</div>
            <div class="oni-card-text">Understand how ONI extends the OSI networking model into the biological domain.</div>
        </div>
        <div class="oni-card">
            <div class="oni-card-icon">📊</div>
            <div class="oni-card-title">Signal Trust Scoring</div>
            <div class="oni-card-text">Learn to calculate coherence scores that measure how trustworthy a neural signal is.</div>
        </div>
        <div class="oni-card">
            <div class="oni-card-icon">🛡️</div>
            <div class="oni-card-title">Neural Firewall</div>
            <div class="oni-card-text">Discover how to filter signals at the brain-computer boundary using L8 Gateway.</div>
        </div>
        <div class="oni-card">
            <div class="oni-card-icon">🔒</div>
            <div class="oni-card-title">Privacy Protection</div>
            <div class="oni-card-text">Master techniques to anonymize neural data and prevent extraction of private info.</div>
        </div>
        <div class="oni-card">
            <div class="oni-card-icon">⚡</div>
            <div class="oni-card-title">Threat Detection</div>
            <div class="oni-card-text">Apply the Kohno threat model to classify and defend against BCI attacks.</div>
        </div>
        <div class="oni-card">
            <div class="oni-card-icon">🧪</div>
            <div class="oni-card-title">Interactive Lab</div>
            <div class="oni-card-text">Explore live visualizations and simulations to see ONI concepts in action.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation buttons - 2 rows of 3
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Learn Layers", key="go_layers", use_container_width=True):
            navigate_to("The 14 Layers")
    with col2:
        if st.button("Learn Trust", key="go_coherence", use_container_width=True):
            navigate_to("Signal Trust")
    with col3:
        if st.button("Learn Firewall", key="go_firewall", use_container_width=True):
            navigate_to("Neural Firewall")

    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("Learn Privacy", key="go_privacy", use_container_width=True):
            navigate_to("Privacy")
    with col5:
        if st.button("Learn Threats", key="go_threats", use_container_width=True):
            navigate_to("Threat Detection")
    with col6:
        if st.button("Open Lab", key="go_lab", use_container_width=True, type="primary"):
            navigate_to("Interactive Lab")

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # Quick stats
    section_header("Framework at a Glance")

    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin: 1rem 0;">
        <div class="oni-metric">
            <div class="oni-metric-value">14</div>
            <div class="oni-metric-label">Security Layers</div>
        </div>
        <div class="oni-metric">
            <div class="oni-metric-value">0</div>
            <div class="oni-metric-label">Dependencies</div>
        </div>
        <div class="oni-metric">
            <div class="oni-metric-value">12+</div>
            <div class="oni-metric-label">Research Papers</div>
        </div>
        <div class="oni-metric">
            <div class="oni-metric-value">3</div>
            <div class="oni-metric-label">Threat Classes</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # Quick start code
    section_header("Quick Start")

    st.code("""pip install oni-framework

# In Python:
from oni import CoherenceMetric, NeuralFirewall

# Calculate signal trust
metric = CoherenceMetric(reference_freq=40.0)
trust = metric.calculate([0.0, 0.025, 0.050], [100, 98, 102])
print(f"Signal trust: {trust:.2f}")""", language="python")


def render_what_is_oni():
    """Detailed explanation of what ONI is."""
    st.markdown("## What is ONI?")
    st.markdown("*The first comprehensive security framework for brain-computer interfaces*")

    st.markdown("---")

    # The Problem
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.08) 0%, rgba(249, 115, 22, 0.08) 100%);
                border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 16px; padding: 1.5rem; margin: 1rem 0;">
        <div style="font-size: 1.1rem; color: #991b1b; font-weight: 600; margin-bottom: 0.75rem;">
            The Problem
        </div>
        <div style="color: #475569; line-height: 1.7;">
            Brain-computer interfaces are being implanted in humans <strong>today</strong>, but there is no
            security standard. The brain evolved no mechanism to distinguish real signals from injected ones.
            Any signal that "looks biological" will be processed as real.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Current BCI Landscape")
        st.markdown("""
        - **Neuralink** — First human implant January 2024
        - **Synchron** — FDA clinical trials with Stentrode
        - **Blackrock Neurotech** — In human brains since 2004
        - **Paradromics** — High-bandwidth neural interfaces

        These devices can read thoughts, control movement, and restore sensation.
        But what happens when an attacker gains access?
        """)

    with col2:
        st.markdown("### Attack Possibilities")
        st.markdown("""
        Without proper security, an attacker could:

        - **Inject** false sensations or perceptions
        - **Extract** private memories or thoughts
        - **Cause** involuntary movements
        - **Block** legitimate neural signals
        - **Override** conscious decisions
        """)

    st.markdown("---")

    # The Solution
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%);
                border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 16px; padding: 1.5rem; margin: 1rem 0;">
        <div style="font-size: 1.1rem; color: #047857; font-weight: 600; margin-bottom: 0.75rem;">
            The Solution: ONI Framework
        </div>
        <div style="color: #475569; line-height: 1.7;">
            <strong>ONI (Open Neurosecurity Interoperability)</strong> extends the familiar OSI networking model
            into the biological domain, creating a unified 14-layer security model from silicon to synapse.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Layer summary table
    st.markdown("### The 14-Layer Architecture")

    st.markdown("""
    | Layers | Domain | Question Answered | Examples |
    |--------|--------|-------------------|----------|
    | **L1-L7** | Silicon | How does data move? | TCP/IP, encryption, protocols |
    | **L8** | Bridge | Should it cross the boundary? | Neural Firewall, validation |
    | **L9-L14** | Biology | Can it be trusted? What does it mean? | Coherence, semantics, identity |
    """)

    st.markdown("""
    The key insight is that **Layer 8 (Neural Gateway)** is where electrodes meet neurons.
    This is the only place where we can inspect, validate, and filter signals before they
    enter or leave the brain.
    """)

    st.markdown("---")

    # Key Components
    section_header("Core Components")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Coherence Metric (Cₛ)**

        Measures signal trustworthiness from 0-1 based on:
        - Timing variance
        - Amplitude stability
        - Pathway reliability

        `Cₛ = e^(-σ²_total)`
        """)

    with col2:
        st.markdown("""
        **Neural Firewall**

        Operates at L8 to make real-time decisions:
        - ACCEPT trusted signals
        - REJECT suspicious signals
        - FLAG uncertain signals

        Uses coherence + authentication.
        """)

    with col3:
        st.markdown("""
        **Kohno Threat Model**

        Classifies BCI attacks by CIA triad:
        - **Alteration** (Integrity)
        - **Blocking** (Availability)
        - **Eavesdropping** (Confidentiality)
        """)

    st.markdown("---")

    # Who uses ONI
    section_header("Who Uses ONI?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        **Researchers**

        Academic teams studying BCI security and neuroethics.
        """)

    with col2:
        st.markdown("""
        **Developers**

        Engineers building neural interfaces who need security primitives.
        """)

    with col3:
        st.markdown("""
        **Regulators**

        FDA, EU, and policy makers developing BCI safety standards.
        """)

    with col4:
        st.markdown("""
        **Security Teams**

        Red teams validating neural device security.
        """)


def render_layers():
    """Interactive 14-layer model visualization."""
    st.markdown("## The 14-Layer ONI Model")
    st.markdown("*A unified security model from silicon to synapse*")

    st.markdown("---")

    # Key insight box
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
                border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 16px; padding: 1.5rem; margin: 1rem 0;">
        <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 200px;">
                <div style="font-weight: 600; color: #1e40af;">OSI (L1-L7)</div>
                <div style="color: #3b82f6;">How does data move?</div>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <div style="font-weight: 600; color: #7c3aed;">ONI (L8-L14)</div>
                <div style="color: #8b5cf6;">Should it move? Can it be trusted?</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive layer explorer
    try:
        from oni import ONIStack
        stack = ONIStack()

        # Create tabs for different views
        tab1, tab2 = st.tabs(["Layer Details", "Interactive Explorer"])

        with tab1:
            # Biology layers
            st.markdown("### Biology Domain (L9-L14)")
            st.caption("Neural and cognitive processing layers")

            for layer in reversed(list(stack.biological_layers())):
                with st.expander(f"**L{layer.number}** — {layer.name}", expanded=layer.number == 14):
                    st.markdown(f"**Function:** {layer.function}")
                    if hasattr(layer, 'attack_surfaces') and layer.attack_surfaces:
                        st.markdown(f"**Attack Surfaces:** `{', '.join(layer.attack_surfaces)}`")

            # Bridge layer
            st.markdown("### Bridge Layer (L8)")
            gateway = stack.layer(8)
            with st.expander(f"**L8** — {gateway.name} — FIREWALL LAYER", expanded=True):
                st.markdown(f"**Function:** {gateway.function}")
                st.warning("This is where the Neural Firewall operates — the critical trust boundary between silicon and biology.")

            # Silicon layers
            st.markdown("### Silicon Domain (L1-L7)")
            st.caption("Traditional OSI networking layers")

            for layer in reversed(list(stack.silicon_layers())):
                with st.expander(f"**L{layer.number}** — {layer.name}"):
                    st.markdown(f"**Function:** {layer.function}")

        with tab2:
            st.markdown("### Interactive Layer Selection")

            selected_layer = st.slider("Select Layer", 1, 14, 8)
            layer = stack.layer(selected_layer)

            # Domain indicator
            if selected_layer <= 7:
                domain = "Silicon"
                color = "#3b82f6"
            elif selected_layer == 8:
                domain = "Bridge"
                color = "#f59e0b"
            else:
                domain = "Biology"
                color = "#10b981"

            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15 0%, {color}08 100%);
                        border-left: 4px solid {color}; border-radius: 0 16px 16px 0;
                        padding: 1.5rem; margin: 1rem 0;">
                <div style="font-size: 0.875rem; color: {color}; text-transform: uppercase; letter-spacing: 0.1em;">
                    {domain} Domain
                </div>
                <div style="font-size: 1.5rem; font-weight: 700; color: #1e293b; margin-top: 0.5rem;">
                    L{layer.number}: {layer.name}
                </div>
                <div style="color: #475569; margin-top: 0.5rem;">
                    {layer.function}
                </div>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error loading layers: {e}")


def render_coherence():
    """Coherence metric interactive page."""
    st.markdown("## Signal Trust (Coherence Metric)")
    st.markdown("*Measuring how trustworthy a neural signal is*")

    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    with col1:
        section_header("The Concept")

        st.markdown("""
        The **Coherence Score (Cₛ)** measures signal trustworthiness by analyzing three variance components:

        | Component | Symbol | Question |
        |-----------|--------|----------|
        | Phase Variance | σ²φ | Is the signal arriving on time? |
        | Transport Variance | σ²τ | Is the pathway reliable? |
        | Gain Variance | σ²γ | Is the amplitude stable? |

        **Formula:** `Cₛ = e^(-σ²_total)`

        Low variance → High coherence → Trusted signal
        """)

        st.markdown("### Interpretation Guide")

        st.markdown("""
        | Score | Level | Action |
        |-------|-------|--------|
        | 0.8 - 1.0 | HIGH | Accept signal |
        | 0.5 - 0.8 | MEDIUM | Flag for review |
        | 0.0 - 0.5 | LOW | Reject signal |
        """)

    with col2:
        section_header("Try It", "Adjust parameters and see the result")

        ref_freq = st.slider("Reference Frequency (Hz)", 1, 100, 40, help="The expected signal frequency")
        timing_jitter = st.slider("Timing Jitter", 0.0, 1.0, 0.1, help="How much timing varies (0 = perfect)")
        amp_variance = st.slider("Amplitude Variance", 0.0, 1.0, 0.1, help="How much amplitude varies (0 = perfect)")

        try:
            from oni import CoherenceMetric
            import random

            # Generate signal with specified variance
            base_interval = 1.0 / ref_freq
            times = [0.0]
            amps = [100.0]

            random.seed(42)
            for i in range(4):
                jitter = (random.random() - 0.5) * 2 * timing_jitter * base_interval
                times.append(times[-1] + base_interval + jitter)

                amp_jitter = (random.random() - 0.5) * 2 * amp_variance * 50
                amps.append(100 + amp_jitter)

            metric = CoherenceMetric(reference_freq=float(ref_freq))
            cs = metric.calculate(times, amps)
            level, description = metric.interpret(cs)

            # Result display
            if cs >= 0.8:
                color = "#059669"
                bg = "rgba(16, 185, 129, 0.15)"
            elif cs >= 0.5:
                color = "#d97706"
                bg = "rgba(245, 158, 11, 0.15)"
            else:
                color = "#dc2626"
                bg = "rgba(239, 68, 68, 0.15)"

            st.markdown(f"""
            <div style="background: {bg}; border: 1px solid {color}33; border-radius: 16px; padding: 1.5rem; text-align: center; margin-top: 1rem;">
                <div style="font-size: 3rem; font-weight: 700; color: {color};">
                    {cs:.3f}
                </div>
                <div style="font-size: 1rem; font-weight: 600; color: {color}; text-transform: uppercase;">
                    {level}
                </div>
                <div style="font-size: 0.875rem; color: #475569; margin-top: 0.5rem;">
                    {description}
                </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")


def render_firewall():
    """Neural firewall interactive page."""
    st.markdown("## Neural Firewall")
    st.markdown("*Protecting the brain-computer boundary*")

    st.markdown("---")

    section_header("How It Works")

    st.markdown("""
    The Neural Firewall operates at **Layer 8 (Neural Gateway)** — the critical boundary
    where silicon meets biology. It makes real-time decisions about whether to allow
    signals to pass.

    ### Decision Matrix

    | Coherence | Authenticated | Decision |
    |-----------|---------------|----------|
    | High (>0.6) | Yes | **ACCEPT** |
    | High (>0.6) | No | **REJECT** |
    | Medium (0.3-0.6) | Yes | **ACCEPT + FLAG** |
    | Medium (0.3-0.6) | No | **REJECT** |
    | Low (<0.3) | Any | **REJECT** |
    """)

    st.markdown("---")

    section_header("Interactive Simulator")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Configure Firewall**")
        threshold_high = st.slider("High Threshold", 0.5, 0.9, 0.6)
        threshold_low = st.slider("Low Threshold", 0.1, 0.5, 0.3)

        st.markdown("**Configure Signal**")
        authenticated = st.checkbox("Signal Authenticated", value=True)
        quality = st.select_slider(
            "Signal Quality",
            options=["Very Low", "Low", "Medium", "High", "Very High"],
            value="High"
        )

    with col2:
        st.markdown("**Result**")

        quality_map = {
            "Very Low": ([0.0, 0.1, 0.15], [100, 30, 180]),
            "Low": ([0.0, 0.03, 0.07], [100, 70, 130]),
            "Medium": ([0.0, 0.026, 0.052], [100, 85, 115]),
            "High": ([0.0, 0.025, 0.050], [100, 95, 105]),
            "Very High": ([0.0, 0.025, 0.050], [100, 99, 101]),
        }

        times, amps = quality_map[quality]

        try:
            from oni import NeuralFirewall
            from oni.firewall import Signal

            firewall = NeuralFirewall(
                threshold_high=threshold_high,
                threshold_low=threshold_low,
            )

            signal = Signal(
                arrival_times=times,
                amplitudes=amps,
                authenticated=authenticated,
            )

            result = firewall.filter(signal)

            # Visual result
            decision_styles = {
                "ACCEPT": ("#059669", "rgba(16, 185, 129, 0.15)", "ACCEPT"),
                "REJECT": ("#dc2626", "rgba(239, 68, 68, 0.15)", "REJECT"),
                "ACCEPT_FLAG": ("#d97706", "rgba(245, 158, 11, 0.15)", "FLAGGED"),
            }

            color, bg, label = decision_styles.get(result.decision.name, ("#64748b", "rgba(100, 116, 139, 0.15)", "UNKNOWN"))

            st.markdown(f"""
            <div style="background: {bg}; border: 1px solid {color}33; border-radius: 16px; padding: 1.5rem; text-align: center;">
                <div style="font-size: 1.75rem; font-weight: 700; color: {color}; margin-top: 0.5rem;">
                    {label}
                </div>
                <div style="color: #475569; margin-top: 0.5rem;">
                    Coherence: {result.coherence:.3f}
                </div>
                <div style="font-size: 0.875rem; color: #64748b; margin-top: 0.5rem;">
                    {result.reason}
                </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")


def render_privacy():
    """Privacy tools page."""
    st.markdown("## Privacy Protection")
    st.markdown("*Preventing unauthorized extraction of private information*")

    st.markdown("---")

    section_header("The Threat", "Neural signals can reveal private information")

    st.markdown("""
    Research has shown that BCI applications can extract private information without user awareness:

    | ERP Component | Latency | What It Reveals | Privacy Risk |
    |---------------|---------|-----------------|--------------|
    | **P300** | ~300ms | Recognition, secrets, PINs | Critical |
    | **N170** | ~170ms | Known faces | Critical |
    | **N400** | ~400ms | Semantic knowledge | High |
    | **ERN** | ~100ms | Error awareness | Medium |

    An attacker could flash images or ask questions, then analyze your brain's
    response to extract information you never intended to share.
    """)

    section_header("Privacy Score Calculator")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Detected ERPs**")
        has_p300 = st.checkbox("P300 (Recognition)", value=True)
        has_n170 = st.checkbox("N170 (Faces)", value=False)
        has_n400 = st.checkbox("N400 (Semantic)", value=False)

    with col2:
        try:
            from oni import PrivacyScoreCalculator

            erps = []
            if has_p300:
                erps.append("P300")
            if has_n170:
                erps.append("N170")
            if has_n400:
                erps.append("N400")

            calc = PrivacyScoreCalculator()
            sample_signal = [0.1 * i for i in range(100)]
            result = calc.calculate(signal_data=sample_signal, detected_erps=erps)

            if result.score < 0.3:
                color, bg = "#059669", "rgba(16, 185, 129, 0.15)"
                level = "LOW RISK"
            elif result.score < 0.6:
                color, bg = "#d97706", "rgba(245, 158, 11, 0.15)"
                level = "MEDIUM RISK"
            else:
                color, bg = "#dc2626", "rgba(239, 68, 68, 0.15)"
                level = "HIGH RISK"

            st.markdown(f"""
            <div style="background: {bg}; border: 1px solid {color}33; border-radius: 16px; padding: 1.5rem; text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 700; color: {color};">
                    {result.score:.2f}
                </div>
                <div style="font-size: 1rem; font-weight: 600; color: {color};">
                    {level}
                </div>
                <div style="color: #475569; margin-top: 0.5rem; font-size: 0.875rem;">
                    {result.interpretation}
                </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")

    section_header("BCI Anonymizer", "Strip privacy-sensitive components before sharing")

    st.markdown("""
    The **BCI Anonymizer** (based on Chizeck & Bonaci, 2014) filters out privacy-sensitive
    ERPs while preserving motor commands needed for BCI operation:

    ```
    Raw Signal → [Anonymizer] → Safe Signal
                      │
                      ├─ BLOCK: P300, N170, N400
                      └─ ALLOW: LRP, CNV (motor only)
    ```

    *Note: The original patent (US20140228701A1) was abandoned — concepts freely available.*
    """)


def render_threats():
    """Threat detection page."""
    st.markdown("## Threat Detection")
    st.markdown("*Classifying and defending against BCI attacks*")

    st.markdown("---")

    section_header("The Kohno Threat Model", "The foundational taxonomy for BCI security (2009)")

    st.markdown("""
    > "Neurosecurity is protection of the confidentiality, integrity, and availability of neural
    > devices from malicious parties with the goal of preserving the safety of a person's neural
    > mechanisms, neural computation, and free will."
    > — Denning, Matsuoka & Kohno (2009)
    """)

    st.markdown("### CIA Triad for BCIs")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 16px; padding: 1.5rem; height: 100%;">
            <div style="font-weight: 700; color: #991b1b;">ALTERATION</div>
            <div style="font-size: 0.875rem; color: #7f1d1d; margin-top: 0.25rem;">Integrity</div>
            <div style="font-size: 0.875rem; color: #475569; margin-top: 0.5rem;">
                Modifying neural signals to cause false perceptions, forced movements, or altered decisions.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 16px; padding: 1.5rem; height: 100%;">
            <div style="font-weight: 700; color: #92400e;">BLOCKING</div>
            <div style="font-size: 0.875rem; color: #78350f; margin-top: 0.25rem;">Availability</div>
            <div style="font-size: 0.875rem; color: #475569; margin-top: 0.5rem;">
                Preventing signals from reaching their destination, causing loss of motor control or sensation.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 16px; padding: 1.5rem; height: 100%;">
            <div style="font-weight: 700; color: #1e40af;">EAVESDROPPING</div>
            <div style="font-size: 0.875rem; color: #1e3a8a; margin-top: 0.25rem;">Confidentiality</div>
            <div style="font-size: 0.875rem; color: #475569; margin-top: 0.5rem;">
                Unauthorized extraction of cognitive states, memories, or identity information.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    section_header("Attack Examples")

    attacks = [
        ("Signal Injection", "Alteration", "L8-L9", "Injecting false signals that the brain processes as real"),
        ("Neural DoS", "Blocking", "L8", "Flooding the interface to prevent legitimate signals"),
        ("P300 Probing", "Eavesdropping", "L13", "Extracting recognition responses to reveal secrets"),
        ("Motor Lockout", "Blocking", "L13", "Suppressing motor signals to prevent movement"),
        ("Memory Extraction", "Eavesdropping", "L11", "Using N400 responses to probe semantic memory"),
    ]

    for name, category, layers, description in attacks:
        cat_color = {"Alteration": "#dc2626", "Blocking": "#d97706", "Eavesdropping": "#2563eb"}[category]
        st.markdown(f"""
        <div style="border-left: 4px solid {cat_color}; padding: 0.75rem 1rem; margin: 0.5rem 0; background: rgba(248, 250, 252, 0.8); border-radius: 0 8px 8px 0;">
            <div style="font-weight: 600; color: #1e293b;">{name}</div>
            <div style="font-size: 0.875rem; color: #64748b;">
                <span style="color: {cat_color}; font-weight: 500;">{category}</span> · {layers} · {description}
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_interactive_lab():
    """Interactive visualizations page - moved from TARA."""
    st.markdown("## Interactive Lab")
    st.markdown("*Explore ONI concepts through live visualizations*")

    st.markdown("---")

    # Check for visualization files
    viz_path = Path(__file__).parent.parent.parent.parent / "tara-nsec-platform" / "visualizations"

    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
                border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 16px; padding: 1.5rem; margin: 1rem 0;">
        <div style="font-size: 1.1rem; color: #1e293b; font-weight: 600; margin-bottom: 0.75rem;">
            Interactive Visualizations
        </div>
        <div style="color: #475569; line-height: 1.7;">
            These visualizations help you understand ONI concepts through hands-on exploration.
            Select a visualization below to launch it.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Available visualizations
    visualizations = [
        {
            "name": "Coherence Playground",
            "description": "Experiment with signal parameters and see how they affect the coherence score in real-time.",
            "concepts": ["Coherence Metric", "Signal Trust", "Variance"],
        },
        {
            "name": "Layer Explorer",
            "description": "Navigate through all 14 layers of the ONI model with interactive details and attack surfaces.",
            "concepts": ["14-Layer Model", "OSI Extension", "Domains"],
        },
        {
            "name": "Scale-Frequency Navigator",
            "description": "Explore the f × S ≈ k invariant across temporal scales from femtoseconds to hours.",
            "concepts": ["Scale Invariance", "Temporal Dynamics", "Neural Timescales"],
        },
        {
            "name": "NSAM Checkpoint Simulator",
            "description": "Practice validating signals through the Neural Signal Assurance Monitoring pipeline.",
            "concepts": ["Signal Validation", "Checkpoints", "Real-time Monitoring"],
        },
        {
            "name": "Kill Chain Visualizer",
            "description": "See how attacks propagate through ONI layers and where defenses can intervene.",
            "concepts": ["Attack Patterns", "Defense Points", "Threat Modeling"],
        },
    ]

    for viz in visualizations:
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.9); border: 1px solid rgba(226, 232, 240, 0.8);
                    border-radius: 12px; padding: 1.25rem; margin: 0.75rem 0;">
            <div style="font-weight: 600; color: #1e293b; font-size: 1.1rem;">{viz['name']}</div>
            <div style="color: #475569; font-size: 0.9rem; margin-top: 0.5rem;">{viz['description']}</div>
            <div style="margin-top: 0.75rem;">
                {' '.join([f'<span style="background: rgba(59, 130, 246, 0.1); color: #2563eb; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.75rem; margin-right: 0.5rem;">{c}</span>' for c in viz['concepts']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Live coherence demo embedded
    section_header("Quick Demo: Coherence Calculator")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Adjust Signal Parameters**")
        demo_timing = st.slider("Timing Stability", 0.0, 1.0, 0.9, key="lab_timing")
        demo_amplitude = st.slider("Amplitude Stability", 0.0, 1.0, 0.9, key="lab_amp")

    with col2:
        # Calculate approximate coherence
        variance = (1 - demo_timing) * 0.5 + (1 - demo_amplitude) * 0.5
        coherence = max(0, min(1, 1 - variance))

        if coherence >= 0.8:
            color, level = "#059669", "HIGH TRUST"
        elif coherence >= 0.5:
            color, level = "#d97706", "MEDIUM TRUST"
        else:
            color, level = "#dc2626", "LOW TRUST"

        st.markdown(f"""
        <div style="background: {color}15; border: 1px solid {color}33; border-radius: 16px; padding: 2rem; text-align: center;">
            <div style="font-size: 3rem; font-weight: 700; color: {color};">
                {coherence:.2f}
            </div>
            <div style="font-size: 1rem; font-weight: 600; color: {color};">
                {level}
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_code_lab():
    """Interactive code examples."""
    st.markdown("## Code Examples")
    st.markdown("*Hands-on examples with the ONI library*")

    st.markdown("---")

    examples = {
        "Calculate Coherence": '''from oni import CoherenceMetric

# Create metric with 40Hz gamma reference
metric = CoherenceMetric(reference_freq=40.0)

# Your signal data
arrival_times = [0.0, 0.025, 0.050, 0.075, 0.100]
amplitudes = [100, 98, 102, 99, 101]

# Calculate trust score
cs = metric.calculate(arrival_times, amplitudes)
level, desc = metric.interpret(cs)

print(f"Coherence: {cs:.3f}")
print(f"Level: {level}")
print(f"Description: {desc}")''',

        "Filter with Firewall": '''from oni import NeuralFirewall
from oni.firewall import Signal

# Create firewall
firewall = NeuralFirewall(
    threshold_high=0.6,
    threshold_low=0.3,
)

# Create a signal
signal = Signal(
    arrival_times=[0.0, 0.025, 0.050],
    amplitudes=[100, 98, 102],
    authenticated=True,
)

# Filter it
result = firewall.filter(signal)

print(f"Decision: {result.decision.name}")
print(f"Coherence: {result.coherence:.3f}")
print(f"Reason: {result.reason}")''',

        "Explore 14 Layers": '''from oni import ONIStack

stack = ONIStack()

# Get firewall layer
gateway = stack.layer(8)
print(f"L8: {gateway.name}")
print(f"Function: {gateway.function}")

print("\\n--- Biological Layers ---")
for layer in stack.biological_layers():
    print(f"L{layer.number}: {layer.name}")

print("\\n--- Silicon Layers ---")
for layer in stack.silicon_layers():
    print(f"L{layer.number}: {layer.name}")''',

        "Threat Classification": '''from oni import KohnoThreatModel, ThreatType

model = KohnoThreatModel()

# Map threats to CIA properties
for threat in ThreatType:
    cia = model.security_properties[threat]
    print(f"{threat.name}: {cia}")

# Get defenses
print("\\nDefenses:")
defenses = model.get_defenses(ThreatType.ALTERATION)
for d in defenses:
    print(f"  - {d}")''',
    }

    selected = st.selectbox("Choose an example:", list(examples.keys()))

    st.code(examples[selected], language="python")

    if st.button("Run Example", type="primary"):
        try:
            exec_globals = {}
            exec(examples[selected], exec_globals)
        except Exception as e:
            st.error(f"Error: {e}")


def render_research():
    """Research papers and resources."""
    st.markdown("## Research Foundation")
    st.markdown("*The academic papers behind ONI*")

    st.markdown("---")

    papers = [
        {
            "title": "Neurosecurity: Security and Privacy for Neural Devices",
            "authors": "Denning, Matsuoka & Kohno",
            "year": "2009",
            "venue": "Neurosurgical Focus",
            "key": "Founded the field of neurosecurity; CIA threat model for BCIs",
            "doi": "10.3171/2009.4.FOCUS0985"
        },
        {
            "title": "App Stores for the Brain: Privacy & Security in BCIs",
            "authors": "Bonaci, Calo & Chizeck",
            "year": "2015",
            "venue": "IEEE Technology and Society",
            "key": "BCI Anonymizer concept; demonstrated P300 attacks",
            "doi": "10.1109/MTS.2015.2425551"
        },
        {
            "title": "Four Ethical Priorities for Neurotechnologies and AI",
            "authors": "Yuste et al.",
            "year": "2017",
            "venue": "Nature",
            "key": "Neurorights framework; identity protection principles",
            "doi": "10.1038/551159a"
        },
        {
            "title": "Towards New Human Rights in the Age of Neuroscience",
            "authors": "Ienca & Andorno",
            "year": "2017",
            "venue": "Life Sciences, Society and Policy",
            "key": "Cognitive liberty; mental privacy; psychological continuity",
            "doi": "10.1186/s40504-017-0050-1"
        },
    ]

    for paper in papers:
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.9); border: 1px solid rgba(226, 232, 240, 0.8); border-radius: 12px; padding: 1.25rem; margin: 1rem 0;">
            <div style="font-weight: 600; color: #1e293b; font-size: 1.1rem;">{paper['title']}</div>
            <div style="color: #64748b; font-size: 0.875rem; margin-top: 0.25rem;">
                {paper['authors']} ({paper['year']}) · {paper['venue']}
            </div>
            <div style="color: #475569; font-size: 0.875rem; margin-top: 0.5rem;">
                <strong>Key contribution:</strong> {paper['key']}
            </div>
            <div style="margin-top: 0.5rem;">
                <a href="https://doi.org/{paper['doi']}" style="font-size: 0.75rem; color: #3b82f6;">
                    DOI: {paper['doi']}
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_glossary():
    """Searchable glossary."""
    st.markdown("## Glossary")
    st.markdown("*Key terms and definitions*")

    st.markdown("---")

    terms = {
        "BCI (Brain-Computer Interface)": "A direct communication pathway between the brain and an external device, allowing neural signals to control computers or receive stimulation.",
        "Coherence Score (Cₛ)": "A metric from 0-1 measuring signal trustworthiness based on timing, amplitude, and pathway variance.",
        "Neural Gateway (L8)": "The critical security boundary in the ONI model where electrodes meet neurons; location of the Neural Firewall.",
        "ERP (Event-Related Potential)": "A measured brain response to a specific stimulus. Different ERPs reveal different cognitive processes.",
        "P300": "An ERP component appearing ~300ms after a recognized stimulus. Can reveal what a user recognizes.",
        "N170": "An ERP component for face recognition. Can reveal known individuals.",
        "Kohno Threat Model": "The foundational BCI security taxonomy defining three threat types: Alteration, Blocking, and Eavesdropping.",
        "Neurosecurity": "The protection of neural devices from malicious parties, preserving safety of neural mechanisms, computation, and free will.",
        "BCI Anonymizer": "A privacy-preserving filter that strips sensitive ERPs from neural data while allowing motor commands.",
        "CIA Triad": "Confidentiality, Integrity, and Availability — the three core security properties applied to BCI protection.",
        "ONI (Open Neurosecurity Interoperability)": "A 14-layer security framework extending OSI into the biological domain for comprehensive BCI protection.",
        "Neural Firewall": "A security component at L8 that validates and filters signals crossing the silicon-biology boundary.",
    }

    search = st.text_input("Search terms...", "")

    filtered = {k: v for k, v in terms.items() if search.lower() in k.lower() or search.lower() in v.lower()}

    for term, definition in filtered.items():
        with st.expander(f"**{term}**"):
            st.markdown(definition)


if __name__ == "__main__":
    main()
