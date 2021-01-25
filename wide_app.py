# -*- coding: utf-8 -*-
import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes
import requests
import plotly.express as px
import pandas as pd

REPO = "https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main"


def _pdf2img(url):
    pdf = convert_from_bytes(requests.get(url).content)[0]
    return pdf


def economy(st, plot_type=None):
    dir = f'{REPO}/figures/economy'

    def consumer_spending():
        st.subheader('Consumer Spending')
        st.image(
            _pdf2img(f'{dir}/consumer_spending/card_spending_change_{plot_type}.pdf'),
            use_column_width=True,
            caption=f"card_spending_change_{plot_type}.pdf",
        )

    def employment():
        st.subheader('Employment')
        st.image(
            _pdf2img(f'{dir}/employment/active_employees_change_{plot_type}.pdf'),
            use_column_width=True,
            caption=f"active_employees_change_{plot_type}.pdf",
        )

    def job_postings():
        st.subheader('Job Postings')
        st.image(
            _pdf2img(
                f'{dir}/job_postings/new_job_postings_change_by_job_zone_{plot_type}.pdf'
            ),
            use_column_width=True,
            caption=f"new_job_postings_change_by_job_zone_{plot_type}.pdf",
        )
        st.image(
            _pdf2img(
                f'{dir}/job_postings/new_job_postings_change_by_sector_{plot_type}.pdf'
            ),
            use_column_width=True,
            caption=f"new_job_postings_change_by_sector_{plot_type}.pdf",
        )

    def small_business_openings():
        st.subheader('Small Business Openings')
        st.image(
            _pdf2img(
                f'{dir}/small_business_opening/open_small_businesses_change_{plot_type}.pdf'
            ),
            use_column_width=True,
            caption=f"open_small_businesses_change_{plot_type}.pdf",
        )

    def small_business_revenue():
        st.subheader('Small Business Revenue')
        st.image(
            _pdf2img(
                f'{dir}/small_business_revenue/small_business_revenue_change_{plot_type}.pdf'
            ),
            use_column_width=True,
            caption=f"small_business_revenue_change_{plot_type}.pdf",
        )

    st.header('Economy')
    with st.beta_expander("View plots"):
        consumer_spending()
        employment()
        job_postings()
        small_business_openings()
        small_business_revenue()


def public_health(st, plot_type=None):
    dir = f'{REPO}/figures/public_health'

    def covid_19_case():
        st.subheader('Place Stay')
        if plot_type == 'line_plot':
            st.image(
                _pdf2img(f'{dir}/covid_19_case/case_count_by_city_line_plot.pdf'),
                use_column_width=True,
                caption=f"case_count_by_city_{plot_type}.pdf",
            )
        st.image(
            _pdf2img(f'{dir}/covid_19_case/case_count_by_zip_code_{plot_type}.pdf'),
            use_column_width=True,
            caption=f"case_count_by_zip_code_{plot_type}.pdf",
        )

    st.header('Public Health')
    with st.beta_expander("View plots"):
        covid_19_case()


def transport(st, plot_type=None):
    dir = f'{REPO}/figures/transport_and_mobility'

    def place_stay():
        st.subheader('Place Stay')
        st.image(
            _pdf2img(f'{dir}/place_stay/time_spent_and_visit_change_{plot_type}.pdf'),
            use_column_width=True,
            caption=f"time_spent_and_visit_change_{plot_type}.pdf",
        )

    def road_traffic():
        st.subheader('Road Traffic')
        st.image(
            _pdf2img(
                f'{dir}/road_traffic/road_intersection_traffic_volume_change_{plot_type}.pdf'
            ),
            use_column_width=True,
            caption=f"road_intersection_traffic_volume_change_{plot_type}.pdf",
        )
        if plot_type == 'line_plot':
            st.image(
                _pdf2img(
                    f'{dir}/road_traffic/road_intersection_traffic_volume_distribution_line_plot.pdf'
                ),
                use_column_width=True,
                caption=f"road_intersection_traffic_volume_distribution_line_plot.pdf",
            )

    def transit_mode():
        st.subheader('Transit Mode')
        st.image(
            _pdf2img(f'{dir}/transit_mode/direction_request_change_{plot_type}.pdf'),
            use_column_width=True,
            caption=f"direction_request_change_{plot_type}.pdf",
        )

    st.header('Transport & Mobility')
    with st.beta_expander("View plots"):
        place_stay()
        road_traffic()
        transit_mode()


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
    economy(col1, plot_type)
    public_health(col2,plot_type)
    transport(col3, plot_type)
main()
