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

    st.markdown(
        f'<div style="'
        f'background: #0d0d0d;'
        f'border: 1px solid rgba(255,255,255,0.06);'
        f'border-left: 3px solid {color};'
        f'padding: 18px 20px;'
        f'margin-bottom: 4px;'
        f'position: relative;'
        f'">'
        f'<div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">'
        f'<div style="'
        f"font-family:'Inter',sans-serif;"
        f'font-size:13px;'
        f'font-weight:600;'
        f'color:#f0f0f0;'
        f'letter-spacing:0.02em;'
        f'">{title}</div>'
        f'<div style="'
        f"font-family:'Inter',sans-serif;"
        f'font-size:9px;'
        f'font-weight:700;'
        f'letter-spacing:0.15em;'
        f'color:{color};'
        f'border:1px solid {color}44;'
        f'padding:3px 8px;'
        f'flex-shrink:0;'
        f'">{label}</div>'
        f'</div>'
        + (f'<div style="font-family:Inter,sans-serif;font-size:12px;color:#444;margin-top:6px;">{impact}</div>' if impact else '')
        + '</div>',
        unsafe_allow_html=True,
    )

    with st.expander("View details", expanded=False):
        st.markdown(
            f'<style>'
            f'.df-detail-block {{'
            f'background: #0a0a0a;'
            f'border: 1px solid rgba(255,255,255,0.05);'
            f'padding: 20px 24px;'
            f'}}'
            f'.df-field-label {{'
            f"font-family: 'Inter', sans-serif;"
            f'font-size: 9px;'
            f'font-weight: 700;'
            f'letter-spacing: 0.18em;'
            f'text-transform: uppercase;'
            f'color: {color};'
            f'margin-bottom: 6px;'
            f'display: block;'
            f'}}'
            f'.df-field-body {{'
            f"font-family: 'Inter', sans-serif;"
            f'font-size: 13px;'
            f'color: #888;'
            f'line-height: 1.7;'
            f'margin-bottom: 20px;'
            f'}}'
            f'.df-action-item {{'
            f'display: flex;'
            f'align-items: flex-start;'
            f'gap: 10px;'
            f'padding: 8px 0;'
            f'border-bottom: 1px solid rgba(255,255,255,0.04);'
            f"font-family: 'Inter', sans-serif;"
            f'font-size: 13px;'
            f'color: #888;'
            f'}}'
            f'.df-action-item:last-child {{ border-bottom: none; }}'
            f'.df-action-dot {{'
            f'width: 5px; height: 5px;'
            f'border-radius: 50%;'
            f'background: {color};'
            f'flex-shrink: 0;'
            f'margin-top: 7px;'
            f'}}'
            f'</style>'
            f'<div class="df-detail-block">',
            unsafe_allow_html=True,
        )

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

    st.markdown(
        '<div style="'
        'background: #0d0d0d;'
        'border: 1px solid rgba(255,255,255,0.07);'
        'padding: 40px 36px 24px;'
        'margin-bottom: 4px;'
        '">'
        '<span style="'
        "font-family:'Inter',sans-serif;"
        'font-size:10px;'
        'font-weight:700;'
        'letter-spacing:0.2em;'
        'text-transform:uppercase;'
        'color:#cc0000;'
        'display:block;'
        'margin-bottom:8px;'
        '">// Detailed Feedback</span>'
        '<div style="'
        "font-family:'Instrument Serif',serif;"
        'font-size:36px;'
        'color:#f0f0f0;'
        'line-height:1;'
        'margin-bottom:8px;'
        '">Issue breakdown.</div>'
        '<div style="'
        "font-family:'Inter',sans-serif;"
        'font-size:13px;'
        'color:#444;'
        'margin-bottom:0;'
        '">{} issue(s) flagged \u2014 grouped by severity.</div>'
        '</div>'.format(len(issues)),
        unsafe_allow_html=True,
    )

    grouped = _group_by_severity(issues)
    for level in SEVERITY_ORDER:
        items = grouped.get(level, [])
        if not items:
            continue
        cfg = SEVERITY_CONFIG.get(level, SEVERITY_CONFIG["low"])
        st.markdown(
            f'<div style="'
            f"font-family:'Inter',sans-serif;"
            f'font-size:9px;'
            f'font-weight:700;'
            f'letter-spacing:0.2em;'
            f'text-transform:uppercase;'
            f'color:{cfg["color"]};'
            f'padding: 20px 0 8px;'
            f'border-bottom: 1px solid rgba(255,255,255,0.04);'
            f'margin-bottom:8px;'
            f'">{cfg["label"]} \u00b7 {len(items)} issue{"s" if len(items) > 1 else ""}</div>',
            unsafe_allow_html=True,
        )
        for idx, issue in enumerate(items):
            _render_issue(issue, idx)