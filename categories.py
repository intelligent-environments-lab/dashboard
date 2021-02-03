import json

import pandas as pd
import streamlit as st
from pdf2image import convert_from_bytes


def _st_image(image_path=None, caption=None):
    # NOTE: the order of title and data['title'] results in behavior that may not
    # be expected by other api users
    title = json.loads(
        open(
            image_path[: image_path.rfind('.') + 1].format(plot_type='line_plot') + 'json', 'r'
        ).read()
    )['title']
    if title is not None:
        st.subheader(title)

    # Tells streamlit to create subheader with the given title followed by an
    # image from the provided url
    if '{plot_type}' in image_path:
        labels = {'Heatmap': 'heat_map', 'Line': 'line_plot'}
        plot_type = labels[st.selectbox('Plot type:', ['Heatmap', 'Line'], key=image_path)]
        image_path = image_path.format(plot_type=plot_type)

    @st.cache(persist=False, allow_output_mutation=True, show_spinner=False, ttl=180)
    def download(image_url):
        data = json.loads(
            open(image_url[: image_url.rfind('.') + 1] + 'json', 'r').read()
        )
        image = open(image_url, 'rb').read()
        if image_url.endswith('.pdf'):
            image = convert_from_bytes(image)[0]
        return image, data

    image, data = download(image_path)

    caption = caption or data['caption'] or image_path[image_path.rfind('/') + 1 :]
    caption += f' \n\n**Data source:** [{data["source"]["name"]}]({data["source"]["url"]})'
    st.image(image, use_column_width=True, output_format='png')
    st.markdown(caption)


class Economy:
    ROOT = 'figures/economy'

    @staticmethod
    def consumer_spending(plot_type):
        # plot_type = st.selectbox('', ['heat_map', 'line_plot'], key='dsfasf')
        _st_image(
            image_path=f'{Economy.ROOT}/consumer_spending/card_spending_change_{{plot_type}}.pdf',
        )

    @staticmethod
    def employment(plot_type):
        _st_image(
            image_path=f'{Economy.ROOT}/employment/active_employees_change_{{plot_type}}.pdf',
        )

    @staticmethod
    def job_postings(plot_type):
        _st_image(
            image_path=f'{Economy.ROOT}/job_postings/new_job_postings_change_by_job_zone_{{plot_type}}.pdf',
        )
        _st_image(
            image_path=f'{Economy.ROOT}/job_postings/new_job_postings_change_by_sector_{{plot_type}}.pdf'
        )

    @staticmethod
    def small_business_openings(plot_type):
        _st_image(
            image_path=f'{Economy.ROOT}/small_business_opening/open_small_businesses_change_{{plot_type}}.pdf',
        )

    @staticmethod
    def small_business_revenue(plot_type):
        _st_image(
            image_path=f'{Economy.ROOT}/small_business_revenue/small_business_revenue_change_{{plot_type}}.pdf',
        )


class PublicHealth:
    ROOT = 'figures/public_health'

    @staticmethod
    def covid_19_case(plot_type=None):
        # st.subheader('Covid-19 Cases')
        _st_image(image_path=f'{PublicHealth.ROOT}/covid_19_case/case_count_by_city_line_plot.pdf')
        _st_image(
            image_path=f'{PublicHealth.ROOT}/covid_19_case/case_count_by_zip_code_line_plot.pdf'
        )

    @staticmethod
    def covid_19_policy():
        file = json.loads(
            open(
                f'{PublicHealth.ROOT}/covid_19_policy/covid19_policies_unknown_figure_type.json',
                'r',
            ).read()
        )
        data = file['data']
        df = pd.DataFrame(data['data'], index=data['index'])
        df.columns = data['columns']
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%B %d, %Y')
        st.subheader(file['title'])
        ver = st.radio('Version',['new','old'])
        if ver == 'new':
            st.markdown(df.to_markdown())
        else:
            st.table(df)
        st.write(file['caption'])


class Transport:
    ROOT = 'figures/transport_and_mobility'

    @staticmethod
    def place_stay(plot_type):
        _st_image(
            image_path=f'{Transport.ROOT}/place_stay/time_spent_and_visit_change_{{plot_type}}.pdf',
        )

    @staticmethod
    def road_traffic(plot_type):
        _st_image(
            image_path=f'{Transport.ROOT}/road_traffic/road_intersection_traffic_volume_change_{{plot_type}}.pdf',
        )
        if plot_type == 'line_plot':
            _st_image(
                image_path=f'{Transport.ROOT}/road_traffic/road_intersection_traffic_volume_distribution_line_plot.pdf',
            )

    @staticmethod
    def transit_mode(plot_type):
        _st_image(
            image_path=f'{Transport.ROOT}/transit_mode/direction_request_change_{{plot_type}}.pdf',
        )
