import json

import requests
import pandas as pd
import streamlit as st
from pdf2image import convert_from_bytes

REPO = "https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main"


def _st_image(image_url=None, title=None, caption=None):
    # Tells streamlit to create subheader with the given title followed by an
    # image from the provided url
    data = json.loads(
        requests.get(image_url[: image_url.rfind('.') + 1] + 'json').content
    )

    image = requests.get(image_url).content
    if image_url.endswith('.pdf'):
        image = convert_from_bytes(image)[0]

    # NOTE: the order of title and data['title'] results in behavior that may not
    # be expected by other api users
    title = data['title'] or title or None
    if title is not None:
        st.subheader(title)

    caption = caption or data['caption'] or image_url[image_url.rfind('/') + 1 :]
    st.image(image, use_column_width=True, caption=caption, output_format='png')


class Economy:
    ROOT = f'{REPO}/figures/economy'

    @staticmethod
    def consumer_spending(plot_type):
        _st_image(
            image_url=f'{Economy.ROOT}/consumer_spending/card_spending_change_{plot_type}.pdf',
            title='Consumer Spending',
        )

    @staticmethod
    def employment(plot_type):
        _st_image(
            image_url=f'{Economy.ROOT}/employment/active_employees_change_{plot_type}.pdf',
            title='Employment',
        )

    @staticmethod
    def job_postings(plot_type):
        _st_image(
            image_url=f'{Economy.ROOT}/job_postings/new_job_postings_change_by_job_zone_{plot_type}.pdf',
            title='Job Postings',
        )
        _st_image(
            image_url=f'{Economy.ROOT}/job_postings/new_job_postings_change_by_sector_{plot_type}.pdf'
        )

    @staticmethod
    def small_business_openings(plot_type):
        _st_image(
            image_url=f'{Economy.ROOT}/small_business_opening/open_small_businesses_change_{plot_type}.pdf',
            title='Small Business Openings',
        )

    @staticmethod
    def small_business_revenue(plot_type):
        _st_image(
            image_url=f'{Economy.ROOT}/small_business_revenue/small_business_revenue_change_{plot_type}.pdf',
            title='Small Business Revenue',
        )


class PublicHealth:
    ROOT = f'{REPO}/figures/public_health'

    @staticmethod
    def covid_19_case(plot_type):
        # st.subheader('Covid-19 Cases')
        if plot_type == 'line_plot':
            _st_image(
                image_url=f'{PublicHealth.ROOT}/covid_19_case/case_count_by_city_line_plot.pdf'
            )
        # if plot_type == 'heat_map':
        #     st.write('\nKingsley mentioned on Monday that we should use the line plot instead of this one.')
        # _st_image(
        #     image_url=f'{PublicHealth.ROOT}/covid_19_case/case_count_by_zip_code_{plot_type}.pdf'
        # )
    
    def covid_19_policy():
        file = json.loads(requests.get(f'{PublicHealth.ROOT}/covid_19_policy/covid19_policies_unknown_figure_type.json').content)
        data = file['data']
        df = pd.DataFrame(data['data'], index=data['index'])
        df.columns = data['columns']
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%B %d, %Y')
        st.subheader(file['title'])
        st.table(df)
        st.write(file['caption']+' (Table version)')



class Transport:
    ROOT = f'{REPO}/figures/transport_and_mobility'

    @staticmethod
    def place_stay(plot_type):
        _st_image(
            image_url=f'{Transport.ROOT}/place_stay/time_spent_and_visit_change_{plot_type}.pdf',
            title='Place Stay',
        )

    @staticmethod
    def road_traffic(plot_type):
        _st_image(
            image_url=f'{Transport.ROOT}/road_traffic/road_intersection_traffic_volume_change_{plot_type}.pdf',
            title='Road Traffic',
        )
        if plot_type == 'line_plot':
            _st_image(
                image_url=f'{Transport.ROOT}/road_traffic/road_intersection_traffic_volume_distribution_line_plot.pdf',
            )

    @staticmethod
    def transit_mode(plot_type):
        _st_image(
            image_url=f'{Transport.ROOT}/transit_mode/direction_request_change_{plot_type}.pdf',
            title='Transit Mode',
        )
