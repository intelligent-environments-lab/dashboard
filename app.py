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


def economy(plot_type=None, use_expanders=False):
    st.header('Economy')

    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )
    with container:
        Economy.consumer_spending(plot_type)
        #Economy.employment(plot_type)
        Economy.job_postings(plot_type)
        Economy.real_estate_activity(plot_type)
        Economy.small_business_openings(plot_type)
        Economy.small_business_revenue(plot_type)


def public_health(plot_type=None, use_expanders=False):
    st.header('Public Health')

    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )

    with container:
        PublicHealth.covid_19_policy()
        PublicHealth.covid_19_case(plot_type)


def transport(plot_type=None, use_expanders=False):
    st.header('Transport & Mobility')

    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )

    with container:
        Transport.place_stay(plot_type)
        Transport.road_traffic(plot_type)
        Transport.public_transit_ridership(plot_type)
        Transport.transit_mode(plot_type)


def civil_infrastructure(plot_type=None, use_expanders=True):
    st.header('Energy & Water')

    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )
    with container:
        CivilInfrastructure.water_energy_demand(plot_type)


def social_welfare(plot_type=None, use_expanders=True):
    st.header('Community Needs')

    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )
    with container:
        SocialWelfare.citizen_need(plot_type)


def air_quality(plot_type=None, use_expanders=True):
    st.header('Air Quality')

    container = (
        st.beta_expander("Expand or collapse") if use_expanders else contextlib.nullcontext()
    )
    with container:
        AirQuality.all()


def main():
    st.set_page_config(
        layout="wide", page_title="IEL Covid-19 Dashboard", page_icon="images/favicon.png"
    )
    st.title('IEL Covid-19 Dashboard')

    # plot_type = st.sidebar.selectbox('Plot Type', ['Heatmap', 'Line'])
    # plot_type = 'heat_map' if plot_type == 'Heatmap' else 'line_plot'
    def st_markdown_image(image_path,hyperlink,alt_text=''):
        image_folder = (
            'https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main'
        )
        try:
            st.sidebar.markdown(
                f'''<a href="{hyperlink}" target="_blank" rel="noreferrer noopener"><img src="{image_folder}/{image_path}"
                alt="{alt_text}" width="280"></a>''',
                unsafe_allow_html=True,
            )
        except:
            st.sidebar.image(image_path, use_column_width=True)
    st.sidebar.subheader("Affiliations")
    st_markdown_image("images/IELLogoAnimated.gif","https://nagy.caee.utexas.edu","IEL Logo")
    st_markdown_image("images/RGB_WCWH_wordmark_3-line_w-tag.png","https://bridgingbarriers.utexas.edu/whole-communities-whole-health/","WCWH Logo")
    st_markdown_image("images/Cockrell_RGB_formal_CAEE.png","https://caee.utexas.edu","CAEE Logo")
    st.sidebar.markdown('**Contact Email:** [nagy@utexas.edu](mailto:nagy@utexas.edu)')
    
    with st.sidebar.beta_expander("Options"):
        expanders = not st.checkbox("Hide expanders", True)
        st.markdown(
            '<font color="green">Note: plots can be enlarged to fullscreen if the expanders are turned off!</font>',
            unsafe_allow_html=True,
        )

    col1, col2, col3 = st.beta_columns(3)
    # with col1:
    #     public_health(plot_type, expanders)
    # with col2:
    #     transport(plot_type, expanders)
    # with col3:
    #     economy(plot_type, expanders)

    col1, col2 = st.beta_columns(2)
    with col1:
        public_health(plot_type=None, use_expanders=expanders)
        economy(plot_type=None, use_expanders=expanders)

    with col2:
        transport(plot_type=None, use_expanders=expanders)
        civil_infrastructure(plot_type=None, use_expanders=expanders)
        social_welfare(plot_type=None, use_expanders=expanders)
        air_quality(use_expanders=expanders)

    with open("assets/disclaimer.txt",'r',encoding='utf-8') as f:
        disclaimer = f.read()
        print(disclaimer)
    
    with st.sidebar.beta_expander("DISCLAIMER"):
        st.markdown(disclaimer)
main()
