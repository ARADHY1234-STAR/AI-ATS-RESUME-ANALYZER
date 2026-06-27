from typing import Any, Dict, Optional
import streamlit as st


def display_jd_comparison(jd_comparison: Optional[Dict[str, Any]]) -> None:
    if not jd_comparison:
        return

    match_pct = float(jd_comparison.get("match_percentage", 0))
    semantic = float(jd_comparison.get("semantic_similarity", 0))
    matched = jd_comparison.get("matched_keywords", []) or []
    missing = jd_comparison.get("missing_keywords", []) or []
    gap = jd_comparison.get("skills_gap", []) or []

    match_clamped = min(max(match_pct, 0), 100)
    sem_clamped = min(max(semantic * 100, 0), 100)

    # matched keywords pills
    matched_html = ""
    if matched:
        for kw in matched[:15]:
            matched_html += f"""
            <span style="
                display:inline-flex;
                align-items:center;
                font-family:'Inter',sans-serif;
                font-size:11px;
                font-weight:600;
                color:#22c55e;
                border:1px solid rgba(34,197,94,0.25);
                background:rgba(34,197,94,0.06);
                padding:3px 10px;
                margin:3px 4px 3px 0;
            ">{kw}</span>"""
    else:
        matched_html = '<span style="font-family:Inter,sans-serif;font-size:13px;color:#333;">None matched yet</span>'

    # missing keywords
    missing_html = ""
    if missing:
        for kw in missing[:10]:
            missing_html += f"""
            <div style="
                display:flex;
                align-items:center;
                gap:10px;
                padding:10px 0;
                border-bottom:1px solid rgba(255,255,255,0.04);
                font-family:'Inter',sans-serif;
                font-size:13px;
                color:#888;
            ">
                <div style="width:5px;height:5px;border-radius:50%;background:#cc0000;
                    box-shadow:0 0 6px rgba(204,0,0,0.5);flex-shrink:0;"></div>
                {kw}
            </div>"""
    else:
        missing_html = '<div style="font-family:Inter,sans-serif;font-size:13px;color:#22c55e;padding:10px 0;">✓ All key terms present</div>'

    # skills gap
    gap_html = ""
    if gap:
        for skill in gap[:10]:
            gap_html += f"""
            <div style="
                display:flex;
                align-items:center;
                gap:10px;
                padding:10px 0;
                border-bottom:1px solid rgba(255,255,255,0.04);
                font-family:'Inter',sans-serif;
                font-size:13px;
                color:#888;
            ">
                <div style="width:5px;height:5px;border-radius:50%;background:#f97316;
                    box-shadow:0 0 6px rgba(249,115,22,0.4);flex-shrink:0;"></div>
                {skill}
            </div>"""
    else:
        gap_html = '<div style="font-family:Inter,sans-serif;font-size:13px;color:#22c55e;padding:10px 0;">✓ No significant gap detected</div>'

    st.markdown(f"""
    <style>
    .jd-wrap {{
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px;
        margin-bottom: 8px;
    }}
    .jd-label {{
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #cc0000;
        margin-bottom: 8px;
        display: block;
    }}
    .jd-title {{
        font-family: 'Instrument Serif', serif;
        font-size: 36px;
        color: #f0f0f0;
        margin-bottom: 32px;
        line-height: 1;
    }}
    .jd-meters {{
        display: flex;
        gap: 1px;
        border: 1px solid rgba(255,255,255,0.07);
        margin-bottom: 32px;
        overflow: hidden;
    }}
    .jd-meter {{
        flex: 1;
        background: #111;
        padding: 24px 20px;
        border-right: 1px solid rgba(255,255,255,0.07);
    }}
    .jd-meter:last-child {{ border-right: none; }}
    .jd-meter-val {{
        font-family: 'Instrument Serif', serif;
        font-size: 48px;
        color: #cc0000;
        line-height: 1;
        display: block;
        margin-bottom: 8px;
    }}
    .jd-meter-lbl {{
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #333;
        display: block;
        margin-bottom: 10px;
    }}
    .jd-bar-wrap {{
        height: 2px;
        background: rgba(255,255,255,0.05);
    }}
    .jd-bar {{
        height: 2px;
        background: linear-gradient(90deg, #cc0000, #ff3333);
    }}
    .jd-section-title {{
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #333;
        display: block;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }}
    .jd-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 32px;
        margin-top: 8px;
    }}
    </style>

    <div class="jd-wrap">
        <span class="jd-label">// JD Match</span>
        <div class="jd-title">Job description analysis.</div>

        <div class="jd-meters">
            <div class="jd-meter">
                <span class="jd-meter-val">{match_pct:.0f}<span style="font-size:20px;color:#333">%</span></span>
                <span class="jd-meter-lbl">Keyword Match</span>
                <div class="jd-bar-wrap"><div class="jd-bar" style="width:{match_clamped}%"></div></div>
            </div>
            <div class="jd-meter">
                <span class="jd-meter-val">{semantic * 100:.0f}<span style="font-size:20px;color:#333">%</span></span>
                <span class="jd-meter-lbl">Semantic Similarity</span>
                <div class="jd-bar-wrap"><div class="jd-bar" style="width:{sem_clamped}%"></div></div>
            </div>
        </div>

        <span class="jd-section-title">// Matched keywords</span>
        <div style="margin-bottom:28px;">{matched_html}</div>

        <div class="jd-grid">
            <div>
                <span class="jd-section-title">// Missing keywords</span>
                {missing_html}
            </div>
            <div>
                <span class="jd-section-title">// Skills gap</span>
                {gap_html}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)