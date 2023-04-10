"""
# Deephaven ticking table example
"""

import streamlit as st
from streamlit_deephaven import start_server, display_dh

start_server()

st.subheader("Deephaven Ticking Plot Demo")

st.subheader(__name__)

from deephaven import time_table
tt = time_table("00:00:01").update(["x=i"])
display_dh(tt)