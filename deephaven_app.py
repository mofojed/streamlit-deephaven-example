"""
# Deephaven example app
"""

import streamlit as st
import __main__
from streamlit_deephaven import display_dh

@st.cache_resource
def init_server(port=8899):
  """Initialize the Deephaven server"""
  from deephaven_server import Server
  server_id = f"__deephaven_server_{port}"
  if __main__.__dict__.get(server_id) is None:
    print("Initializing Deephaven Server...")
    s = Server(port=port)
    s.start()
    __main__.__dict__[server_id] = s

  return __main__.__dict__[server_id]
init_server()

@st.cache_resource
def init_ctx():
  from deephaven.execution_context import get_exec_ctx
  context_id = "__deephaven_context"
  if __main__.__dict__.get(context_id) is None:
    print("Getting Deephaven Context...")
    __main__.__dict__[context_id] = get_exec_ctx()
  return get_exec_ctx()
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
  display_dh(tt, height=200)

  f = Figure()
  f = f.plot_xy(series_name="Sine", t=tt, x="x", y="y")
  f = f.plot_xy(series_name="Cosine", t=tt, x="x", y="z")
  f = f.show()
  display_dh(f, height=300)
   
