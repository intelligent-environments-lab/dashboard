# -*- coding: utf-8 -*-
import contextlib

import streamlit as st
import streamlit_analytics
import plotly.express as px
import pandas as pd

from table_of_contents import Toc
from categories import (
    Economy,
    PublicHealth,
    Transport,
    CivilInfrastructure,
    SocialWelfare,
    AirQuality,
)

toc = Toc()

def container(name,use_expanders=False):
    toc.header(name)
    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )
    return container

def st_markdown_image(image_path, hyperlink, alt_text=""):
        image_folder = (
            "https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main"
        )
        try:
            st.sidebar.markdown(
                f"""<a href="{hyperlink}" target="_blank" rel="noreferrer noopener"><img src="{image_folder}/{image_path}"
                alt="{alt_text}" width="280"></a>""",
                unsafe_allow_html=True,
            )
        except:
            st.sidebar.image(image_path, use_column_width=True)

def main():
    st.set_page_config(
        layout="centered", page_title="IEL Covid-19 Dashboard", page_icon="images/favicon.png"
    )
    streamlit_analytics.start_tracking(firestore_key_file="assets/firebase-key.json", firestore_collection_name="counts")
    st.title("IEL Covid-19 Dashboard")

    with open("assets/introduction.txt", "r", encoding="utf-8") as f:
        intro = f.read()
    st.markdown(intro)

    st.sidebar.subheader("Affiliations")
    st_markdown_image("images/IELLogoAnimated.gif", "https://nagy.caee.utexas.edu", "IEL Logo")
    st_markdown_image(
        "images/RGB_WCWH_wordmark_3-line_w-tag.png",
        "https://bridgingbarriers.utexas.edu/whole-communities-whole-health/",
        "WCWH Logo",
    )
    st_markdown_image("images/Cockrell_RGB_formal_CAEE.png", "https://caee.utexas.edu", "CAEE Logo")
    st.sidebar.markdown("**Contact Email:** [nagy@utexas.edu](mailto:nagy@utexas.edu)")

    with st.sidebar.beta_expander("Outline"):
        toc.placeholder()

    with st.sidebar.beta_expander("Options"):
        expanders = not st.checkbox("Hide expanders", True)
        st.markdown(
            '<font color="green">Note: plots can be enlarged to fullscreen if the expanders are turned off!</font>',
            unsafe_allow_html=True,
        )

    # col1, _, col2 = st.beta_columns([20, 1, 20])
    # with col1:
    with container('Public Health', expanders):
        PublicHealth.covid_19_policy(toc=toc)
        PublicHealth.show(toc=toc)
    with container('Economy', expanders):
        Economy.show(toc=toc)

    # with col2:
    with container("Transport & Mobility", expanders):
        Transport.show(toc=toc)
    with container("Energy & Water", expanders):
        CivilInfrastructure.show('water_energy_demand',toc=toc)
    with container("Community Needs", expanders):
        SocialWelfare.show(['citizen_need'],toc=toc)
    with container("Air Quality", expanders):
        AirQuality.show(toc=toc)


    with st.sidebar.beta_expander("DISCLAIMER"):
        with open("assets/disclaimer.txt", "r", encoding="utf-8") as f:
            disclaimer = f.read()

        st.markdown(disclaimer)

    toc.generate()
    streamlit_analytics.stop_tracking(firestore_key_file="assets/firebase-key.json", firestore_collection_name="counts")


main()
