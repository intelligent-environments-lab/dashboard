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
st.code("""# -*- coding: utf-8 -*-
import streamlit as st

st.title("IEL Covid-19 Dashboard")
st.image("https://raw.githubusercontent.com/intelligent-environments-lab/covid19/master/plots/air_quality/Austin%20Air%20Quality%20Mean%20Concentration%20from%202015-2020.png?token=AN5AK2C2JPCCDXOI4JEXUQTAAIF2C",\
         caption="combined_airline_departed_heatmap.png", width=600)
st.image("https://raw.githubusercontent.com/intelligent-environments-lab/covid19/master/plots/air_quality/2020%20Austin%20Air%20Quality.png?token=AN5AK2BSFASKP4YOR5NJRYC762DLS",
         caption="2020 Austin Air Quality.png", width=600)"""
)