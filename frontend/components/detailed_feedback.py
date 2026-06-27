from typing import Any, Dict, List
import streamlit as st
from frontend.components._helpers import get_severity_style

SEVERITY_ORDER = ["critical", "high", "medium", "low"]

SEVERITY_CONFIG = {
    "critical": {"color": "#cc0000", "glow": "rgba(204,0,0,0.4)", "label": "CRITICAL"},
    "high":     {"color": "#ff3333", "glow": "rgba(255,51,51,0.3)", "label": "HIGH"},
    "medium":   {"color": "#f97316", "glow": "rgba(249,115,22,0.3)", "label": "MEDIUM"},
    "low":      {"color": "#888888", "glow": "rgba(136,136,136,0.2)", "label": "LOW"},
}


def _group_by_severity(issues: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {level: [] for level in SEVERITY_ORDER}
    for issue in issues:
        level = (issue.get("severity_level") or "low").lower()
        grouped.setdefault(level, []).append(issue)
    return grouped


def _render_issue(issue: Dict[str, Any], idx: int) -> None:
    level = (issue.get("severity_level") or "low").lower()
    cfg = SEVERITY_CONFIG.get(level, SEVERITY_CONFIG["low"])
    color = cfg["color"]
    glow = cfg["glow"]
    label = cfg["label"]

    title = issue.get("issue_title", "Untitled issue")
    impact = issue.get("ats_impact", "")
    explanation = issue.get("explanation", "")
    where = issue.get("where_it_appears", "")
    how_to_fix = issue.get("how_to_fix", "")
    action_items = issue.get("action_items") or []
    example = issue.get("example_improvement", "")

    st.markdown(f"""
    <div style="
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.06);
        border-left: 3px solid {color};
        padding: 18px 20px;
        margin-bottom: 4px;
        position: relative;
    ">
        <div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">
            <div style="
                font-family:'Inter',sans-serif;
                font-size:13px;
                font-weight:600;
                color:#f0f0f0;
                letter-spacing:0.02em;
            ">{title}</div>
            <div style="
                font-family:'Inter',sans-serif;
                font-size:9px;
                font-weight:700;
                letter-spacing:0.15em;
                color:{color};
                border:1px solid {color}44;
                padding:3px 8px;
                flex-shrink:0;
            ">{label}</div>
        </div>
        {f'<div style="font-family:Inter,sans-serif;font-size:12px;color:#444;margin-top:6px;">{impact}</div>' if impact else ''}
    </div>
    """, unsafe_allow_html=True)

    with st.expander("View details", expanded=False):
        st.markdown(f"""
        <style>
        .df-detail-block {{
            background: #0a0a0a;
            border: 1px solid rgba(255,255,255,0.05);
            padding: 20px 24px;
        }}
        .df-field-label {{
            font-family: 'Inter', sans-serif;
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: {color};
            margin-bottom: 6px;
            display: block;
        }}
        .df-field-body {{
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #888;
            line-height: 1.7;
            margin-bottom: 20px;
        }}
        .df-action-item {{
            display: flex;
            align-items: flex-start;
            gap: 10px;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.04);
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #888;
        }}
        .df-action-item:last-child {{ border-bottom: none; }}
        .df-action-dot {{
            width: 5px; height: 5px;
            border-radius: 50%;
            background: {color};
            flex-shrink: 0;
            margin-top: 7px;
        }}
        </style>
        <div class="df-detail-block">
        """, unsafe_allow_html=True)

        blocks = ""
        if explanation:
            blocks += f'<span class="df-field-label">// What\'s happening</span><div class="df-field-body">{explanation}</div>'
        if where:
            blocks += f'<span class="df-field-label">// Where it appears</span><div class="df-field-body">{where}</div>'
        if how_to_fix:
            blocks += f'<span class="df-field-label">// How to fix</span><div class="df-field-body">{how_to_fix}</div>'

        if blocks:
            st.markdown(blocks + "</div>", unsafe_allow_html=True)

        if action_items:
            st.markdown('<span class="df-field-label">// Action items</span>', unsafe_allow_html=True)
            items_html = ""
            for item in action_items:
                items_html += f'<div class="df-action-item"><div class="df-action-dot"></div><span>{item}</span></div>'
            st.markdown(items_html, unsafe_allow_html=True)

        if example:
            st.markdown('<span class="df-field-label">// Example improvement</span>', unsafe_allow_html=True)
            st.code(example, language="text")


def display_detailed_feedback(analysis: Dict[str, Any]) -> None:
    issues = analysis.get("detailed_feedback") or []
    if not issues:
        return

    st.markdown("""
    <div style="
        background: #0d0d0d;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 40px 36px 24px;
        margin-bottom: 4px;
    ">
        <span style="
            font-family:'Inter',sans-serif;
            font-size:10px;
            font-weight:700;
            letter-spacing:0.2em;
            text-transform:uppercase;
            color:#cc0000;
            display:block;
            margin-bottom:8px;
        ">// Detailed Feedback</span>
        <div style="
            font-family:'Instrument Serif',serif;
            font-size:36px;
            color:#f0f0f0;
            line-height:1;
            margin-bottom:8px;
        ">Issue breakdown.</div>
        <div style="
            font-family:'Inter',sans-serif;
            font-size:13px;
            color:#444;
            margin-bottom:0;
        ">{} issue(s) flagged — grouped by severity.</div>
    </div>
    """.format(len(issues)), unsafe_allow_html=True)

    grouped = _group_by_severity(issues)
    for level in SEVERITY_ORDER:
        items = grouped.get(level, [])
        if not items:
            continue
        cfg = SEVERITY_CONFIG.get(level, SEVERITY_CONFIG["low"])
        st.markdown(f"""
        <div style="
            font-family:'Inter',sans-serif;
            font-size:9px;
            font-weight:700;
            letter-spacing:0.2em;
            text-transform:uppercase;
            color:{cfg['color']};
            padding: 20px 0 8px;
            border-bottom: 1px solid rgba(255,255,255,0.04);
            margin-bottom:8px;
        ">{cfg['label']} · {len(items)} issue{'s' if len(items) > 1 else ''}</div>
        """, unsafe_allow_html=True)
        for idx, issue in enumerate(items):
            _render_issue(issue, idx)