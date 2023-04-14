"""
# Deephaven crypto example
"""

import streamlit as st
from streamlit_deephaven import start_server, display_dh

start_server()

st.subheader("Deephaven Crypto Demo")

@st.cache_resource
def get_source():
    from deephaven import read_csv
    return read_csv("https://media.githubusercontent.com/media/deephaven/examples/main/CryptoCurrencyHistory/CSV/FakeCryptoTrades_20230209.csv")

crypto = get_source()

# Cache the instruments from the source
@st.cache_resource
def get_instruments(_source):
    from deephaven import pandas as dhpd
    return dhpd.to_pandas(_source.select_distinct("Instrument"))

# Cache the exchanges from the source
@st.cache_resource
def get_exchanges(_source):
    from deephaven import pandas as dhpd
    return dhpd.to_pandas(_source.select_distinct("Exchange"))

# Show a radio selection for instruments and exchanges
instrument_selected = st.radio("Instrument", get_instruments(crypto))
exchange_selected = st.radio("Exchange", get_exchanges(crypto))

# Filter the tables based on the selection
result = crypto.where(["Instrument == instrument_selected", "Exchange == exchange_selected"])
display_dh(result)