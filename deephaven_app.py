"""
# Deephaven example app
"""

import streamlit as st
import __main__
from streamlit_deephaven import start_server, display_dh

start_server()

st.subheader("Deephaven Component Demo")

st.subheader(__name__)

from deephaven import empty_table
t = empty_table(1000).update(["x=i", "y=x * x"])
display_dh(t)

