# -*- coding: utf-8 -*-
import contextlib

import streamlit as st
import plotly.express as px
import pandas as pd

from categories import (
    Economy,
    PublicHealth,
    Transport,
    CivilInfrastructure,
    SocialWelfare,
    AirQuality,
)


class Toc:
    # TOC class made by https://discuss.streamlit.io/u/synode
    # Taken from https://discuss.streamlit.io/t/table-of-contents-widget/3470/7
    def __init__(self):
        self._items = []
        self._placeholder = None

    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=False):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

    def _markdown(self, text, level, space=""):
        key = "".join(filter(str.isalnum, text)).lower()

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


toc = Toc()


def container(use_expanders):
    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )
    return container


def economy(use_expanders=False):
    toc.header("Economy")

    with container(use_expanders):
        Economy.consumer_spending(toc=toc)
        # Economy.employment()
        Economy.job_postings(toc=toc)
        Economy.real_estate_activity(toc=toc)
        Economy.small_business_openings(toc=toc)
        Economy.small_business_revenue(toc=toc)


def public_health(use_expanders=False):
    toc.header("Public Health")

    with container(use_expanders):
        PublicHealth.covid_19_policy(toc=toc)
        PublicHealth.covid_19_case(toc=toc)


def transport(use_expanders=False):
    toc.header("Transport & Mobility")

    with container(use_expanders):
        Transport.place_stay(toc=toc)
        Transport.road_traffic(toc=toc)
        Transport.public_transit_ridership(toc=toc)
        Transport.transit_mode(toc=toc)


def civil_infrastructure(use_expanders=True):
    toc.header("Energy & Water")

    with container(use_expanders):
        CivilInfrastructure.water_energy_demand(toc=toc)


def social_welfare(use_expanders=True):
    toc.header("Community Needs")

    with container(use_expanders):
        SocialWelfare.citizen_need(toc=toc)


def air_quality(use_expanders=True):
    toc.header("Air Quality")

    with container(use_expanders):
        AirQuality.show(toc=toc)


def main():
    st.set_page_config(
        layout="centered", page_title="IEL Covid-19 Dashboard", page_icon="images/favicon.png"
    )
    st.title("IEL Covid-19 Dashboard")

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
    public_health(expanders)
    economy(expanders)

    # with col2:
    transport(expanders)
    civil_infrastructure(expanders)
    social_welfare(expanders)
    air_quality(expanders)

    with open("assets/disclaimer.txt", "r", encoding="utf-8") as f:
        disclaimer = f.read()

    with st.sidebar.beta_expander("DISCLAIMER"):
        st.markdown(disclaimer)
    toc.generate()


main()
