import streamlit as st
import streamlit.components.v1 as components

# Streamlit secrets에서 불러오기
CLIENT_KEY = st.secrets["DID_CLIENT_KEY"]
AGENT_ID = st.secrets["DID_AGENT_ID"]

st.title("D-ID AI Agent")

html_code = f"""
<div id="did-agent-container" style="width: 80%; height: 600px;"></div>
<script type="module"
    src="https://agent.d-id.com/v2/index.js"
    data-mode="fabio"
    data-client-key="{CLIENT_KEY}"
    data-agent-id="{AGENT_ID}"
    data-name="did-agent"
    data-monitor="true"
    data-target-id="did-agent-container">
</script>
"""

components.html(html_code, height=650)
