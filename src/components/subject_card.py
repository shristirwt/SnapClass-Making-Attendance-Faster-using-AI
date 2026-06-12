import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""<style>
.stat-badge {{
    background: #EB459E20 !important;
    border: 1px solid #EB459E50 !important;
    padding: 5px 12px !important;
    border-radius: 12px !important;
    font-size: 0.9rem !important;
    color: black !important;
}}
.stat-badge b, .stat-badge span {{
    color: black !important;
}}
</style>
<div style="background:white; border-left:8px solid #EB459E; padding:25px; border-radius:20px; border: 1px solid black; margin-bottom:20px;">
    <h3 style="margin:0; color:#1e293b; font-size:1.2rem;">{name}</h3>
    <p style="color:#64748b; margin:10px 0;"> Code : <span style="background:#E0E3FF; color:#5865F2; padding: 2px 8px; border-radius:5px;">{code}</span> | Section : {section}</p>
"""
        
    if stats:
        html += """<div style="display:flex; gap:8px; flex-wrap:wrap;">"""
        
        for icon, label, value in stats:
            html += f'<div class="stat-badge">{icon} <b>{value}</b> <span>{label}</span></div>'
            
        html += "</div>"
        
    html += "</div>"
        
    st.markdown(html, unsafe_allow_html=True)
    
    if footer_callback:
        footer_callback()