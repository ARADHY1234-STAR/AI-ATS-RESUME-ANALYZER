from textwrap import dedent
from typing import Any, Dict
import streamlit as st
from frontend.components._helpers import get_score_color, get_score_emoji

COMPONENTS = [
    ("Formatting",        "formatting",        20, "📐"),
    ("Keywords & Skills", "keywords",          25, "🔑"),
    ("Content Quality",   "content",           25, "📝"),
    ("Skill Validation",  "skill_validation",  15, "🧠"),
    ("ATS Compatibility", "ats_compatibility", 15, "🤖"),
]


def display_overall_score(analysis: Dict[str, Any]) -> None:
    score = float(analysis.get("ATS_score", analysis.get("ats_score", 0)))
    interpretation = analysis.get("interpretation", "")
    emoji = get_score_emoji(score)

    if score >= 80:
        accent = "#ff3333"
        label = "EXCELLENT"
    elif score >= 60:
        accent = "#ff6600"
        label = "GOOD"
    else:
        accent = "#cc0000"
        label = "NEEDS WORK"

    st.markdown(dedent(f"""\
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&family=Instrument+Serif:ital@0;1&display=swap');
    .score-wrap {{
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 56px 48px;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin-bottom: 8px;
    }}
    .score-wrap::before {{
        content: '';
        position: absolute;
        top: -100px; left: 50%;
        transform: translateX(-50%);
        width: 500px; height: 300px;
        background: radial-gradient(ellipse, rgba(200,0,0,0.12) 0%, transparent 70%);
        pointer-events: none;
    }}
    .score-tag {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: {accent};
        border: 1px solid {accent}44;
        padding: 5px 14px;
        margin-bottom: 28px;
    }}
    .score-number {{
        font-family: 'Instrument Serif', serif;
        font-size: 112px;
        font-weight: 400;
        line-height: 0.9;
        color: #fff;
        display: block;
    }}
    .score-denom {{
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        color: #333;
        letter-spacing: 0.1em;
        display: block;
        margin-top: 8px;
        margin-bottom: 16px;
    }}
    .score-interp {{
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #555;
        max-width: 400px;
        margin: 0 auto;
        line-height: 1.7;
    }}
    .score-line {{
        width: 60px;
        height: 2px;
        background: {accent};
        margin: 20px auto;
        opacity: 0.6;
    }}
    </style>
    """)
    + f'<div class="score-wrap">'
      f'<div class="score-tag">// ATS Score \u00b7 {label}</div>'
      f'<span class="score-number" style="color:{accent}">{score:.0f}</span>'
      f'<span class="score-denom">OUT OF 100</span>'
      f'<div class="score-line"></div>'
      f'<p class="score-interp">{interpretation}</p>'
      f'</div>',
    unsafe_allow_html=True)


def display_score_breakdown(analysis: Dict[str, Any]) -> None:
    component_scores = analysis.get("component_scores") or {}

    st.markdown(dedent("""\
    <style>
    .breakdown-wrap {
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px;
        margin-bottom: 8px;
    }
    .breakdown-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #cc0000;
        margin-bottom: 8px;
        display: block;
    }
    .breakdown-title {
        font-family: 'Instrument Serif', serif;
        font-size: 36px;
        color: #f0f0f0;
        margin-bottom: 36px;
        line-height: 1;
    }
    .comp-row {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 20px;
    }
    .comp-name {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #888;
        min-width: 160px;
    }
    .comp-bar-wrap {
        flex: 1;
        height: 3px;
        background: rgba(255,255,255,0.05);
        position: relative;
    }
    .comp-bar {
        height: 3px;
        background: linear-gradient(90deg, #cc0000, #ff3333);
        transition: width 0.6s ease;
        position: relative;
    }
    .comp-bar::after {
        content: '';
        position: absolute;
        right: 0; top: 50%;
        transform: translateY(-50%);
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #ff3333;
        box-shadow: 0 0 8px rgba(255,51,51,0.6);
    }
    .comp-score {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 700;
        color: #ff3333;
        min-width: 48px;
        text-align: right;
    }
    .comp-max {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        color: #333;
        min-width: 32px;
    }
    </style>
    """)
    + '<div class="breakdown-wrap"><span class="breakdown-label">// Dimensions</span><div class="breakdown-title">Score breakdown.</div>',
    unsafe_allow_html=True)

    rows_html = ""
    for label, key, max_score, icon in COMPONENTS:
        value = float(component_scores.get(key, 0))
        pct = (value / max_score * 100) if max_score else 0
        rows_html += (
            f'<div class="comp-row">'
            f'<div class="comp-name">{icon} {label}</div>'
            f'<div class="comp-bar-wrap"><div class="comp-bar" style="width:{pct}%"></div></div>'
            f'<div class="comp-score">{value:.0f}</div>'
            f'<div class="comp-max">/ {max_score}</div>'
            f'</div>'
        )

    st.markdown(rows_html + "</div>", unsafe_allow_html=True)