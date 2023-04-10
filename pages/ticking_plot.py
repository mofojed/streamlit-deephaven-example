"""
# Deephaven ticking plot example
"""

import streamlit as st
from streamlit_deephaven import start_server, display_dh

start_server()

st.subheader("Deephaven Ticking Plot Demo")

st.subheader(__name__)

a = st.slider('Amplitude', min_value=-100.0, max_value=100.0, value=1.0)
f = st.slider('Frequency', min_value=-100.0, max_value=100.0, value=1.0)
p = 0

from deephaven import time_table
from deephaven.plot.figure import Figure
tt = time_table("00:00:01").update(["x=i", "y=a * Math.sin(f*x + p)", "z=a * Math.cos(f*x + p)"])

f = Figure()
f = f.plot_xy(series_name="Sine", t=tt, x="x", y="y")
f = f.plot_xy(series_name="Cosine", t=tt, x="x", y="z")
f = f.show()
display_dh(f)