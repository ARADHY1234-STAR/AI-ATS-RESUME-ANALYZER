from textwrap import dedent
from typing import Any, Dict
import streamlit as st


def display_skill_validation(analysis: Dict[str, Any]) -> None:
    details = analysis.get("skill_validation_details") or {}
    validated = details.get("validated", [])
    unvalidated = details.get("unvalidated", [])
    total = details.get("total", len(validated) + len(unvalidated))
    pct = details.get("validation_pct", 0.0)

    st.markdown(dedent("""\
    <style>
    .sv-wrap {
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px;
        margin-bottom: 8px;
    }
    .sv-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #cc0000;
        margin-bottom: 8px;
        display: block;
    }
    .sv-title {
        font-family: 'Instrument Serif', serif;
        font-size: 36px;
        color: #f0f0f0;
        margin-bottom: 28px;
        line-height: 1;
    }
    .sv-stats {
        display: flex;
        gap: 1px;
        border: 1px solid rgba(255,255,255,0.07);
        margin-bottom: 28px;
        overflow: hidden;
    }
    .sv-stat {
        flex: 1;
        padding: 20px 16px;
        background: #111;
        text-align: center;
        border-right: 1px solid rgba(255,255,255,0.07);
    }
    .sv-stat:last-child { border-right: none; }
    .sv-stat-val {
        font-family: 'Instrument Serif', serif;
        font-size: 40px;
        color: #cc0000;
        line-height: 1;
        display: block;
    }
    .sv-stat-lbl {
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #444;
        margin-top: 4px;
        display: block;
    }
    .sv-bar-wrap {
        height: 3px;
        background: rgba(255,255,255,0.05);
        margin-bottom: 32px;
        position: relative;
    }
    .sv-bar {
        height: 3px;
        background: linear-gradient(90deg, #cc0000, #ff3333);
        position: relative;
    }
    .sv-bar::after {
        content: '';
        position: absolute;
        right: 0; top: 50%;
        transform: translateY(-50%);
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #ff3333;
        box-shadow: 0 0 8px rgba(255,51,51,0.6);
    }
    .sv-skill-item {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.04);
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #888;
        line-height: 1.6;
    }
    .sv-skill-item:last-child { border-bottom: none; }
    .sv-dot-green {
        width: 6px; height: 6px; border-radius: 50%;
        background: #22c55e; flex-shrink: 0; margin-top: 6px;
        box-shadow: 0 0 8px rgba(34,197,94,0.5);
    }
    .sv-dot-red {
        width: 6px; height: 6px; border-radius: 50%;
        background: #cc0000; flex-shrink: 0; margin-top: 6px;
        box-shadow: 0 0 8px rgba(204,0,0,0.5);
    }
    .sv-skill-name { color: #f0f0f0; font-weight: 600; }
    .sv-skill-meta { color: #444; font-size: 11px; margin-top: 2px; }
    .sv-section-title {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #333;
        margin-bottom: 12px;
        display: block;
    }
    .sv-empty {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #444;
        padding: 20px 0;
    }
    </style>
    """), unsafe_allow_html=True)

    if total == 0:
        st.markdown(
            '<div class="sv-wrap">'
            '<span class="sv-label">// Skill Validation</span>'
            '<div class="sv-title">Skills.</div>'
            '<div class="sv-empty">No skills detected on the resume.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        return

    pct_clamped = min(max(pct, 0), 100)

    st.markdown(
        f'<div class="sv-wrap">'
        f'<span class="sv-label">// Skill Validation</span>'
        f'<div class="sv-title">Skills.</div>'
        f'<div class="sv-stats">'
        f'<div class="sv-stat"><span class="sv-stat-val">{total}</span><span class="sv-stat-lbl">Total Skills</span></div>'
        f'<div class="sv-stat"><span class="sv-stat-val">{len(validated)}</span><span class="sv-stat-lbl">Validated</span></div>'
        f'<div class="sv-stat"><span class="sv-stat-val">{pct:.0f}<span style="font-size:20px;color:#444">%</span></span><span class="sv-stat-lbl">Match Rate</span></div>'
        f'</div>'
        f'<div class="sv-bar-wrap"><div class="sv-bar" style="width:{pct_clamped}%"></div></div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    if validated:
        with st.expander(f"Validated skills ({len(validated)})", expanded=False):
            st.markdown('<span class="sv-section-title">// Demonstrated in your experience</span>', unsafe_allow_html=True)
            items_html = ""
            for entry in validated:
                skill = entry.get("skill", "?")
                projects = entry.get("projects", []) or []
                similarity = entry.get("similarity")
                project_text = ", ".join(projects[:3]) if projects else "experience section"
                sim_text = f" · {similarity * 100:.0f}% match" if isinstance(similarity, (int, float)) else ""
                items_html += (
                    f'<div class="sv-skill-item">'
                    f'<div class="sv-dot-green"></div>'
                    f'<div>'
                    f'<div class="sv-skill-name">{skill}{sim_text}</div>'
                    f'<div class="sv-skill-meta">Found in: {project_text}</div>'
                    f'</div>'
                    f'</div>'
                )
            st.markdown(items_html, unsafe_allow_html=True)

    if unvalidated:
        with st.expander(f"Unvalidated skills ({len(unvalidated)})", expanded=False):
            st.markdown('<span class="sv-section-title">// Not tied to any project or experience</span>', unsafe_allow_html=True)
            items_html = ""
            for skill in unvalidated:
                items_html += (
                    f'<div class="sv-skill-item">'
                    f'<div class="sv-dot-red"></div>'
                    f'<div class="sv-skill-name">{skill}</div>'
                    f'</div>'
                )
            st.markdown(items_html, unsafe_allow_html=True)