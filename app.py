# -*- coding: utf-8 -*-
import streamlit as st

st.title("IEL Covid-19 Dashboard")
st.image("https://raw.githubusercontent.com/intelligent-environments-lab/covid19/master/plots/air_quality/Austin%20Air%20Quality%20Mean%20Concentration%20from%202015-2020.png?token=AN5AK2C2JPCCDXOI4JEXUQTAAIF2C",\
         caption="This is a caption. The above image is a png.", width=600)

st.header("Examples and References")
st.write("API Reference here: https://docs.streamlit.io/en/stable/api.html")
st.latex("This\ is\ latex: y=mx+b")
st.markdown("Github *Flavored* __markdown__?")
st.header("Header")
st.subheader("Subheader")
st.subheader("This is the code for this dashboard.")
st.code("""import streamlit as st

st.title("IEL Covid-19 Dashboard")
st.image("https://raw.githubusercontent.com/intelligent-environments-lab/covid19/master/plots/air_quality/Austin%20Air%20Quality%20Mean%20Concentration%20from%202015-2020.png?token=AN5AK2C2JPCCDXOI4JEXUQTAAIF2C",\
         caption="This is a caption. The above image is a png.", width=600)

st.header("Examples and References")
st.write("API Reference here: https://docs.streamlit.io/en/stable/api.html")
st.latex("This\ is\ latex: y=mx+b")
st.markdown("Github *Flavored* __markdown__?")
st.header("Header")
st.subheader("Subheader")
st.subheader("This is the code for this dashboard.")"""
)