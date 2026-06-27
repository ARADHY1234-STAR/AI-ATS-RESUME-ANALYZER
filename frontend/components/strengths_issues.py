from textwrap import dedent
from typing import Any, Dict, List
import streamlit as st


def display_strengths(strengths: List[str]) -> None:
    st.markdown(dedent("""\
    <style>
    .str-wrap {
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px;
        margin-bottom: 8px;
    }
    .str-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #cc0000;
        margin-bottom: 8px;
        display: block;
    }
    .str-title {
        font-family: 'Instrument Serif', serif;
        font-size: 36px;
        color: #f0f0f0;
        margin-bottom: 28px;
        line-height: 1;
    }
    .str-item {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 14px 0;
        border-bottom: 1px solid rgba(255,255,255,0.04);
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #888;
        line-height: 1.6;
    }
    .str-item:last-child { border-bottom: none; }
    .str-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #22c55e;
        flex-shrink: 0;
        margin-top: 7px;
        box-shadow: 0 0 8px rgba(34,197,94,0.5);
    }
    .str-empty {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #444;
        padding: 20px 0;
    }
    </style>
    """) + '<div class="str-wrap"><span class="str-label">// What\'s working</span><div class="str-title">Strengths.</div>', unsafe_allow_html=True)

    if not strengths:
        st.markdown('<div class="str-empty">Keep improving your resume to unlock strengths.</div>', unsafe_allow_html=True)
    else:
        items_html = ""
        for item in strengths:
            items_html += f'<div class="str-item"><div class="str-dot"></div><span>{item}</span></div>'
        st.markdown(items_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def display_critical_issues(analysis: Dict[str, Any]) -> None:
    critical = analysis.get("critical_issues") or []
    summary = analysis.get("issues_summary") or []

    st.markdown(dedent("""\
    <style>
    .iss-wrap {
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px;
        margin-bottom: 8px;
        position: relative;
        overflow: hidden;
    }
    .iss-wrap::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 3px; height: 100%;
        background: #cc0000;
    }
    .iss-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #cc0000;
        margin-bottom: 8px;
        display: block;
    }
    .iss-title {
        font-family: 'Instrument Serif', serif;
        font-size: 36px;
        color: #f0f0f0;
        margin-bottom: 8px;
        line-height: 1;
    }
    .iss-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #444;
        margin-bottom: 28px;
    }
    .iss-item {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        padding: 14px 0;
        border-bottom: 1px solid rgba(255,255,255,0.04);
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #888;
        line-height: 1.6;
    }
    .iss-item:last-child { border-bottom: none; }
    .iss-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #cc0000;
        flex-shrink: 0;
        margin-top: 7px;
        box-shadow: 0 0 8px rgba(204,0,0,0.5);
    }
    .iss-success {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #22c55e;
        padding: 20px 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    </style>
    """), unsafe_allow_html=True)

    if not critical and not summary:
        st.markdown(
            '<div class="iss-wrap">'
            '<span class="iss-label">// Issues</span>'
            '<div class="iss-title">Critical Issues.</div>'
            '<div class="iss-success">\u2713 No critical issues found \u2014 your resume looks clean.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        return

    items_html = ""
    for item in critical:
        items_html += f'<div class="iss-item"><div class="iss-dot"></div><span>{item}</span></div>'

    st.markdown(
        f'<div class="iss-wrap">'
        f'<span class="iss-label">// Fix these first</span>'
        f'<div class="iss-title">Critical Issues.</div>'
        f'<div class="iss-subtitle">Address these before applying \u2014 they hurt your ATS score the most.</div>'
        f'{items_html}'
        f'</div>',
        unsafe_allow_html=True,
    )

    extra = [s for s in summary if s not in critical]
    if extra:
        with st.expander("Additional flagged items", expanded=False):
            for item in extra:
                st.markdown(
                    f'<div class="iss-item"><div class="iss-dot"></div><span>{item}</span></div>',
                    unsafe_allow_html=True,
                )