"""
# Deephaven example app
"""

import streamlit as st
from streamlit_deephaven import start_server, display_dh

# Start the Deephaven server. You must start the server before running any Deephaven operations.
start_server()

st.subheader("Streamlit Deephaven")

# Create a simple table.
from deephaven import empty_table
t = empty_table(1000).update(["x=i", "y=x * x"])

# Display the table.
display_dh(t)