# -*- coding: utf-8 -*-
import contextlib

import streamlit as st
import plotly.express as px
import pandas as pd

from categories import Economy, PublicHealth, Transport


def economy(plot_type=None, use_expanders=False):
    st.header('Economy')

    container = (
        st.beta_expander("Expand or collapse")
        if use_expanders
        else contextlib.nullcontext()
    )
    with container:
        Economy.consumer_spending(plot_type)
        Economy.employment(plot_type)
        Economy.job_postings(plot_type)
        Economy.small_business_openings(plot_type)
        Economy.small_business_revenue(plot_type)


def public_health(plot_type=None, use_expanders=False):
    st.header('Public Health')

    container = (
        st.beta_expander("Expand or collapse")
        if use_expanders
        else contextlib.nullcontext()
    )

    with container:
        PublicHealth.covid_19_case(plot_type)
        PublicHealth.covid_19_policy()


def transport(plot_type=None, use_expanders=False):
    st.header('Transport & Mobility')

    container = (
        st.beta_expander("Expand or collapse")
        if use_expanders
        else contextlib.nullcontext()
    )

    with container:
        Transport.place_stay(plot_type)
        Transport.road_traffic(plot_type)
        Transport.transit_mode(plot_type)


def main():
    st.set_page_config(layout="wide")
    st.title('IEL Covid-19 Dashboard')
    st.sidebar.header('Sidebar')
    plot_type = st.sidebar.selectbox('Plot Type', ['Heatmap', 'Line'])

    plot_type = 'heat_map' if plot_type == 'Heatmap' else 'line_plot'

    expanders = not st.sidebar.checkbox("Hide expanders", True)
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        public_health(plot_type, expanders)
    with col2:
        transport(plot_type, expanders)
    with col3:
        economy(plot_type, expanders)


main()
