"""
# Deephaven ticking plot example
"""

import streamlit as st
from streamlit_deephaven import start_server, display_dh

start_server()

st.subheader("Deephaven Ticking Plot Demo")

a = st.slider('Amplitude', min_value=-100.0, max_value=100.0, value=1.0)
f = st.slider('Frequency', min_value=-100.0, max_value=100.0, value=1.0)
p = 0

@st.cache_resource
def init_time_table():
    from deephaven import time_table
    return time_table("00:00:01").update(["x=i"])

tt = init_time_table()

from deephaven.plot.figure import Figure
t = tt.update(["y=a * Math.sin(f*x + p)", "z=a * Math.cos(f*x + p)"])

f = Figure()
f = f.plot_xy(series_name="Sine", t=t, x="x", y="y")
f = f.plot_xy(series_name="Cosine", t=t, x="x", y="z")
f = f.show()
display_dh(f)