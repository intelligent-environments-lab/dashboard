# -*- coding: utf-8 -*-
import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes
import requests
import plotly.express as px
import pandas as pd

from categories import Economy, PublicHealth, Transport



def economy(plot_type=None):
    st.header('Economy')
    # with st.beta_expander("View plots"):
    Economy.consumer_spending(plot_type)
    Economy.employment(plot_type)
    Economy.job_postings(plot_type)
    Economy.small_business_openings(plot_type)
    Economy.small_business_revenue(plot_type)



def public_health(plot_type=None):
    st.header('Public Health')
    # with st.beta_expander("View plots"):
    PublicHealth.covid_19_case(plot_type)


def transport(plot_type=None):
    st.header('Transport & Mobility')
    # with st.beta_expander("View plots"):
    Transport.place_stay(plot_type)
    Transport.road_traffic(plot_type)
    Transport.transit_mode(plot_type)


def main():
    st.set_page_config(layout="wide")
    st.title('IEL Covid-19 Dashboard')
    st.sidebar.header('Sidebar')
    plot_type = st.sidebar.selectbox('Plot Type', ['Heatmap', 'Line'])

    if plot_type == 'Heatmap':
        plot_type = 'heat_map'
    else:
        plot_type = 'line_plot'

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        economy(plot_type)
    with col2:
        public_health(plot_type)
    with col3:
        transport(plot_type)
main()
