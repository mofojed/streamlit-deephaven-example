"""
# Deephaven plot app
"""

import streamlit as st
from deephaven_app import init_server, init_ctx
from streamlit_deephaven import display_dh

init_server()
main_exec_ctx = init_ctx()

st.subheader("Deephaven Component Demo")

st.subheader(__name__)

a = st.slider('Amplitude', min_value=-100.0, max_value=100.0, value=1.0)
f = st.slider('Frequency', min_value=-100.0, max_value=100.0, value=1.0)
p = 0

with main_exec_ctx:
  from deephaven import time_table
  from deephaven.plot.figure import Figure
  tt = time_table("00:00:01").update(["x=i", "y=a * Math.sin(f*x + p)", "z=a * Math.cos(f*x + p)"])

  f = Figure()
  f = f.plot_xy(series_name="Sine", t=tt, x="x", y="y")
  f = f.plot_xy(series_name="Cosine", t=tt, x="x", y="z")
  f = f.show()
  display_dh(f, height=500)
   
