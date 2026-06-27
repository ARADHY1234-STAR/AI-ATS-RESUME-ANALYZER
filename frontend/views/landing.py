import streamlit as st
st.markdown("""
<style>
.block-container {
    padding-top: 0 !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}
</style>
""", unsafe_allow_html=True)

def render():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=Instrument+Serif:ital@0;1&display=swap');

    /* ── TOKENS ── */
    :root {
        --bg: #080808;
        --surface: #101010;
        --border: rgba(255,255,255,0.07);
        --green: #00e87a;
        --green-glow: rgba(0,232,122,0.15);
        --green-dim: rgba(0,232,122,0.08);
        --white: #f0f0f0;
        --muted: #555;
        --text: #d8d8d8;
    }

    /* ── HIDE DEFAULT STREAMLIT PADDING ── */
    .block-container { padding-top: 1rem !important; }

    /* ── HERO ── */
    .ats-hero {
        position: relative;
        background: var(--bg);
        border: 1px solid var(--border);
        border-radius: 0px;
        padding: 72px 48px 64px;
        text-align: center;
        overflow: hidden;
        margin-bottom: 0;
    }
    .ats-hero::before {
        content: '';
        position: absolute;
        top: -120px; left: 50%;
        transform: translateX(-50%);
        width: 600px; height: 400px;
        background: radial-gradient(ellipse, rgba(0,232,122,0.12) 0%, transparent 70%);
        pointer-events: none;
    }
    .ats-hero-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--green);
        border: 1px solid rgba(0,232,122,0.3);
        padding: 5px 14px;
        margin-bottom: 32px;
    }
    .ats-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: var(--green);
        box-shadow: 0 0 8px var(--green);
        animation: ats-blink 2s ease-in-out infinite;
    }
    @keyframes ats-blink { 0%,100%{opacity:1;} 50%{opacity:0.2;} }

    .ats-hero-title {
        font-family: 'Instrument Serif', serif;
        font-size: clamp(52px, 7vw, 88px);
        font-weight: 400;
        line-height: 0.95;
        letter-spacing: -0.02em;
        color: var(--white);
        display: block;
        margin-bottom: 8px;
    }
    .ats-hero-accent {
        font-family: 'Instrument Serif', serif;
        font-style: italic;
        font-size: clamp(52px, 7vw, 88px);
        font-weight: 400;
        line-height: 0.95;
        background: linear-gradient(135deg, #00e87a 0%, #00d4aa 60%, #00c4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: block;
        margin-bottom: 24px;
    }
    .ats-hero-sub {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        font-weight: 300;
        color: #666;
        max-width: 440px;
        margin: 0 auto;
        line-height: 1.8;
    }

    /* ── SCORE STRIP ── */
    .ats-strip {
        display: flex;
        border: 1px solid var(--border);
        border-top: none;
        overflow: hidden;
        margin-bottom: 48px;
        background: rgba(255,255,255,0.015);
    }
    .ats-stat {
        flex: 1;
        text-align: center;
        padding: 20px 12px;
        border-right: 1px solid var(--border);
        transition: background 0.2s;
    }
    .ats-stat:last-child { border-right: none; }
    .ats-stat:hover { background: var(--green-dim); }
    .ats-stat-val {
        font-family: 'Instrument Serif', serif;
        font-size: 32px;
        color: var(--green);
        line-height: 1;
    }
    .ats-stat-unit { font-size: 14px; color: var(--green); }
    .ats-stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--muted);
        margin-top: 4px;
    }

    /* ── FEATURES ── */
    .ats-section-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--green);
        display: block;
        margin-bottom: 12px;
    }
    .ats-section-title {
        font-family: 'Instrument Serif', serif;
        font-size: clamp(36px, 4vw, 52px);
        font-weight: 400;
        color: var(--white);
        line-height: 1;
        margin-bottom: 48px;
    }

    .ats-feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1px;
        border: 1px solid var(--border);
        margin-bottom: 64px;
        overflow: hidden;
    }
    .ats-feature {
        background: var(--surface);
        padding: 32px 28px;
        transition: background 0.25s;
        position: relative;
    }
    .ats-feature:hover { background: rgba(0,232,122,0.04); }
    .ats-feature::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--green), transparent);
        opacity: 0;
        transition: opacity 0.25s;
    }
    .ats-feature:hover::after { opacity: 1; }
    .ats-feature-icon {
        font-size: 28px;
        margin-bottom: 16px;
        display: block;
    }
    .ats-feature-title {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: var(--white);
        margin-bottom: 12px;
    }
    .ats-feature-body {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #555;
        line-height: 1.7;
    }
    .ats-feature-body strong { color: var(--green); font-weight: 600; }

    /* score breakdown inside feature */
    .ats-scores {
        margin-top: 14px;
        display: flex;
        flex-direction: column;
        gap: 6px;
    }
    .ats-score-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        color: #444;
    }
    .ats-score-bar-wrap {
        flex: 1;
        margin: 0 10px;
        height: 2px;
        background: rgba(255,255,255,0.06);
    }
    .ats-score-bar {
        height: 2px;
        background: var(--green);
        opacity: 0.5;
    }
    .ats-score-pct { color: var(--green); font-weight: 600; min-width: 28px; text-align: right; }

    /* ── HOW IT WORKS ── */
    .ats-steps {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1px;
        border: 1px solid var(--border);
        overflow: hidden;
        margin-bottom: 64px;
    }
    .ats-step {
        background: var(--surface);
        padding: 36px 28px;
        position: relative;
    }
    .ats-step-num {
        font-family: 'Instrument Serif', serif;
        font-size: 64px;
        color: rgba(0,232,122,0.12);
        line-height: 1;
        margin-bottom: 16px;
        display: block;
    }
    .ats-step-title {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--white);
        margin-bottom: 10px;
    }
    .ats-step-body {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #555;
        line-height: 1.7;
    }
    .ats-step-tag {
        display: inline-block;
        margin-top: 16px;
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: var(--green);
        border: 1px solid rgba(0,232,122,0.25);
        padding: 3px 10px;
    }

    /* ── FOOTER CTA ── */
    .ats-footer-cta {
        border: 1px solid rgba(0,232,122,0.2);
        background: rgba(0,232,122,0.03);
        padding: 56px 48px;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 32px;
    }
    .ats-footer-cta::before {
        content: '';
        position: absolute;
        bottom: -80px; left: 50%;
        transform: translateX(-50%);
        width: 400px; height: 200px;
        background: radial-gradient(ellipse, rgba(0,232,122,0.1), transparent 70%);
        pointer-events: none;
    }
    .ats-footer-cta-title {
        font-family: 'Instrument Serif', serif;
        font-size: clamp(32px, 4vw, 48px);
        color: var(--white);
        margin-bottom: 12px;
    }
    .ats-footer-cta-sub {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #555;
        margin-bottom: 32px;
    }

    /* CTA button override */
    div[data-testid="stButton"] button[kind="primary"] {
        background: var(--green) !important;
        color: #000 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 11px !important;
        font-weight: 900 !important;
        letter-spacing: 0.15em !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 0 !important;
        height: 52px !important;
        box-shadow: 0 0 40px rgba(0,232,122,0.25) !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    div[data-testid="stButton"] button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 48px rgba(0,232,122,0.4) !important;
    }
    </style>

    <!-- HERO -->
    <div class="ats-hero">
        <div class="ats-hero-tag"><span class="ats-dot"></span>AI-Powered · Instant · Free</div>
        <span class="ats-hero-title">Beat the</span>
        <span class="ats-hero-accent">Algorithm.</span>
        <p class="ats-hero-sub">Upload your resume. Get a score, a breakdown, and fixes — before any recruiter sees it.</p>
    </div>

    <!-- STAT STRIP -->
    <div class="ats-strip">
        <div class="ats-stat">
            <div class="ats-stat-val">5<span class="ats-stat-unit">+</span></div>
            <div class="ats-stat-label">Score Dimensions</div>
        </div>
        <div class="ats-stat">
            <div class="ats-stat-val">30<span class="ats-stat-unit">s</span></div>
            <div class="ats-stat-label">Avg. Analysis Time</div>
        </div>
        <div class="ats-stat">
            <div class="ats-stat-val">0</div>
            <div class="ats-stat-label">Data Leaves Your Device</div>
        </div>
        <div class="ats-stat">
            <div class="ats-stat-val">100<span class="ats-stat-unit">%</span></div>
            <div class="ats-stat-label">Private & Local</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⚡ Analyze My Resume", use_container_width=True, type="primary"):
            st.session_state.current_view = 'scorer'
            st.rerun()

    st.markdown("""
    <!-- FEATURES -->
    <div style="margin-top:64px;">
        <span class="ats-section-label">// What we check</span>
        <div class="ats-section-title">Five dimensions.<br>One score.</div>
    </div>

    <div class="ats-feature-grid">
        <div class="ats-feature">
            <span class="ats-feature-icon">📐</span>
            <div class="ats-feature-title">Formatting</div>
            <div class="ats-feature-body">Clean structure parsers can read. No tables, columns, or graphics that confuse ATS bots.</div>
            <div class="ats-scores">
                <div class="ats-score-row"><span>Weight</span><div class="ats-score-bar-wrap"><div class="ats-score-bar" style="width:20%"></div></div><span class="ats-score-pct">20%</span></div>
            </div>
        </div>
        <div class="ats-feature">
            <span class="ats-feature-icon">🔑</span>
            <div class="ats-feature-title">Keywords & Skills</div>
            <div class="ats-feature-body">Role-matched keyword density. We check if the right terms appear in the right context.</div>
            <div class="ats-scores">
                <div class="ats-score-row"><span>Weight</span><div class="ats-score-bar-wrap"><div class="ats-score-bar" style="width:25%"></div></div><span class="ats-score-pct">25%</span></div>
            </div>
        </div>
        <div class="ats-feature">
            <span class="ats-feature-icon">📝</span>
            <div class="ats-feature-title">Content Quality</div>
            <div class="ats-feature-body">Impact verbs, quantified achievements, and clear bullet structure — not just word count.</div>
            <div class="ats-scores">
                <div class="ats-score-row"><span>Weight</span><div class="ats-score-bar-wrap"><div class="ats-score-bar" style="width:25%"></div></div><span class="ats-score-pct">25%</span></div>
            </div>
        </div>
        <div class="ats-feature">
            <span class="ats-feature-icon">🧠</span>
            <div class="ats-feature-title">Skill Validation</div>
            <div class="ats-feature-body">AI checks if your listed skills appear in your actual project descriptions. <strong>No empty claims.</strong></div>
            <div class="ats-scores">
                <div class="ats-score-row"><span>Weight</span><div class="ats-score-bar-wrap"><div class="ats-score-bar" style="width:15%"></div></div><span class="ats-score-pct">15%</span></div>
            </div>
        </div>
        <div class="ats-feature">
            <span class="ats-feature-icon">🤖</span>
            <div class="ats-feature-title">ATS Compatibility</div>
            <div class="ats-feature-body">File format, section headers, and parse-ability tested against real ATS behavior patterns.</div>
            <div class="ats-scores">
                <div class="ats-score-row"><span>Weight</span><div class="ats-score-bar-wrap"><div class="ats-score-bar" style="width:15%"></div></div><span class="ats-score-pct">15%</span></div>
            </div>
        </div>
        <div class="ats-feature">
            <span class="ats-feature-icon">🔒</span>
            <div class="ats-feature-title">Privacy First</div>
            <div class="ats-feature-body">All analysis runs locally. Your resume never leaves your device. <strong>Zero external API calls.</strong></div>
        </div>
    </div>

    <!-- HOW IT WORKS -->
    <div style="margin-top:64px; margin-bottom:24px;">
        <span class="ats-section-label">// Process</span>
        <div class="ats-section-title">Three steps.<br>Done.</div>
    </div>

    <div class="ats-steps">
        <div class="ats-step">
            <span class="ats-step-num">01</span>
            <div class="ats-step-title">Upload Resume</div>
            <div class="ats-step-body">PDF, DOC, or DOCX. Drop it in and we handle the rest.</div>
            <span class="ats-step-tag">Instant parse</span>
        </div>
        <div class="ats-step">
            <span class="ats-step-num">02</span>
            <div class="ats-step-title">AI Analysis</div>
            <div class="ats-step-body">Local models score your resume across all five dimensions in under 30 seconds.</div>
            <span class="ats-step-tag">~30 seconds</span>
        </div>
        <div class="ats-step">
            <span class="ats-step-num">03</span>
            <div class="ats-step-title">Fix & Resubmit</div>
            <div class="ats-step-body">Get specific, actionable recommendations. Edit your resume. Re-run. Repeat until green.</div>
            <span class="ats-step-tag">Actionable</span>
        </div>
    </div>

    <!-- FOOTER CTA -->
    <div class="ats-footer-cta">
        <div class="ats-footer-cta-title">Your resume is one upload away.</div>
        <div class="ats-footer-cta-sub">No account needed to get your first score.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⚡ Get My ATS Score", use_container_width=True, type="primary", key="cta2"):
            st.session_state.current_view = 'scorer'
            st.rerun()