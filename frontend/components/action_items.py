from re import escape
from textwrap import dedent
from typing import Any, Dict, List, Tuple
import streamlit as st
from html import escape

SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}

SEVERITY_CONFIG = {
    "critical": {"color": "#cc0000", "label": "CRITICAL"},
    "high":     {"color": "#ff3333", "label": "HIGH"},
    "medium":   {"color": "#f97316", "label": "MEDIUM"},
    "low":      {"color": "#555555", "label": "LOW"},
}


def _collect_action_items(analysis: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    items: List[Tuple[str, str, str]] = []
    for issue in analysis.get("detailed_feedback") or []:
        level = (issue.get("severity_level") or "low").lower()
        title = issue.get("issue_title", "")
        for action in issue.get("action_items") or []:
            items.append((level, title, action))
    if not items:
        for suggestion in analysis.get("suggestions") or []:
            items.append(("medium", "General", suggestion))
    items.sort(key=lambda row: SEVERITY_RANK.get(row[0], 99))
    return items


def display_action_items(analysis: Dict[str, Any]) -> None:
    items = _collect_action_items(analysis)
    if not items:
        return

    st.markdown(dedent("""\
    <style>
    .ai-wrap {
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px;
        margin-bottom: 8px;
    }
    .ai-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #cc0000;
        margin-bottom: 8px;
        display: block;
    }
    .ai-title {
        font-family: 'Instrument Serif', serif;
        font-size: 36px;
        color: #f0f0f0;
        margin-bottom: 8px;
        line-height: 1;
    }
    .ai-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #444;
        margin-bottom: 32px;
    }
    .ai-item {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        padding: 16px 0;
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }
    .ai-item:last-child { border-bottom: none; }
    .ai-left {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
        flex-shrink: 0;
        padding-top: 2px;
    }
    .ai-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        flex-shrink: 0;
    }
    .ai-sev {
        font-family: 'Inter', sans-serif;
        font-size: 8px;
        font-weight: 700;
        letter-spacing: 0.12em;
        writing-mode: vertical-lr;
        transform: rotate(180deg);
    }
    .ai-body { flex: 1; }
    .ai-source {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .ai-text {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #888;
        line-height: 1.6;
    }
    .ai-counter {
        font-family: 'Instrument Serif', serif;
        font-size: 11px;
        color: #333;
        flex-shrink: 0;
        padding-top: 2px;
    }
    </style>
    """), unsafe_allow_html=True)

    items_html = ""
    for i, (level, source, action) in enumerate(items):
        cfg = SEVERITY_CONFIG.get(level, SEVERITY_CONFIG["low"])
        color = cfg["color"]
        sev_label = cfg["label"]
        items_html += (
            f'<div class="ai-item">'
            f'<div class="ai-left">'
            f'<div class="ai-dot" style="background:{color}; box-shadow:0 0 6px {color}88;"></div>'
            f'<div class="ai-sev" style="color:{color};">{sev_label}</div>'
            f'</div>'
            f'<div class="ai-body">'
            f'<div class="ai-source" style="color:{color};">{source}</div>'
            f'<div class="ai-text">{escape(str(action))}</div>'
            f'</div>'
            f'<div class="ai-counter">{str(i + 1).zfill(2)}</div>'
            f'</div>'
        )
    st.write(items_html)
    st.markdown(
        f'<div class="ai-wrap">'
        f'<span class="ai-label">// What to fix</span>'
        f'<div class="ai-title">Action items.</div>'
        f'<div class="ai-subtitle">Sorted by urgency — fix critical items first.</div>'
        f'{items_html}'
        f'</div>',
        unsafe_allow_html=True,
    )