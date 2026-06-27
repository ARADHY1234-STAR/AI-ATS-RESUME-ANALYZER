from typing import Any, Dict
import streamlit as st


def display_recommendations(analysis: Dict[str, Any]) -> None:
    suggestions = analysis.get("suggestions") or []
    if not suggestions:
        return

    items_html = ""
    for i, suggestion in enumerate(suggestions):
        items_html += f"""
        <div style="
            display:flex;
            align-items:flex-start;
            gap:16px;
            padding:16px 0;
            border-bottom:1px solid rgba(255,255,255,0.04);
        ">
            <div style="
                font-family:'Instrument Serif',serif;
                font-size:11px;
                color:#222;
                flex-shrink:0;
                padding-top:2px;
                min-width:24px;
            ">{str(i + 1).zfill(2)}</div>
            <div style="
                width:3px;
                height:3px;
                border-radius:50%;
                background:#cc0000;
                flex-shrink:0;
                margin-top:9px;
                box-shadow:0 0 6px rgba(204,0,0,0.5);
            "></div>
            <div style="
                font-family:'Inter',sans-serif;
                font-size:13px;
                color:#888;
                line-height:1.7;
                flex:1;
            ">{suggestion}</div>
        </div>
        """

    st.markdown(f"""
    <div style="
        background:#0d0d0d;
        border:1px solid rgba(255,255,255,0.07);
        padding:40px 36px;
        margin-bottom:8px;
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
        ">// Next steps</span>
        <div style="
            font-family:'Instrument Serif',serif;
            font-size:36px;
            color:#f0f0f0;
            line-height:1;
            margin-bottom:32px;
        ">Recommendations.</div>
        {items_html}
    </div>
    """, unsafe_allow_html=True)