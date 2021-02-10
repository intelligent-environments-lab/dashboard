import json

import pandas as pd
import streamlit as st
from pdf2image import convert_from_bytes


def _st_image(image_path=None, caption=None, title=None, toc=None):
    # NOTE: the order of title and data['title'] results in behavior that may not
    # be expected by other api users
    title = title or json.loads(
        open(
            image_path[: image_path.rfind('.') + 1].format(plot_type='line_plot') + 'json', 'r'
        ).read()
    )['title']
    if title is not None:
        try:
            toc.subheader(title)
        except:
            st.subheader(title)

    # Tells streamlit to create subheader with the given title followed by an
    # image from the provided url
    if '{plot_type}' in image_path:
        labels = {'Heatmap': 'heat_map', 'Line': 'line_plot'}
        plot_type = labels[st.selectbox('Plot type:', ['Heatmap', 'Line'], key=image_path)]
        image_path = image_path.format(plot_type=plot_type)
        if ('road_intersection_traffic_volume_change_line_plot' in image_path):
            image_path = image_path.replace('change','distribution')
        if 'public_transit_ridership_distribution_heat_map' in image_path:
            image_path = image_path.replace('distribution','change')

    @st.cache(persist=False, allow_output_mutation=True, show_spinner=False, ttl=180)
    def download(image_url):
        try:
            data = json.loads(
                open(image_url[: image_url.rfind('.') + 1] + 'json', 'r').read()
            )
        except:
            data=None
        image = open(image_url, 'rb').read()
        if image_url.endswith('.pdf'):
            image = convert_from_bytes(image)[0]
        return image, data

    image, data = download(image_path)

    caption = caption or data['caption'] or image_path[image_path.rfind('/') + 1 :]
    try:
        insights = ' \n\n**Insights:**'
        for item in data["insights"]:
            insights +=f'\n- {item}'
        caption += f'{insights}'
    except:
        pass
    try:
        caption += f' \n\n**Data source:** [{data["source"]["name"]}]({data["source"]["url"]})'
    except:
        pass
    st.image(image, use_column_width=True, output_format='png')
    st.markdown(caption)

class AirQuality:
    ROOT = 'figures/air_quality'

    @staticmethod
    def all(toc=None):
        _st_image(
            image_path=f'{AirQuality.ROOT}/no2_heat_map.pdf',toc=toc
            # title='Nitrogen dioxide',
            # caption='  '
        )
        _st_image(
            image_path=f'{AirQuality.ROOT}/ozone_heat_map.pdf',toc=toc
            # title='Ozone',
            # caption='  '
        )
        _st_image(
            image_path=f'{AirQuality.ROOT}/pm2_5_heat_map.pdf',toc=toc
            # title='PM2.5',
            # caption='  '
        )
        
        
class Economy:
    ROOT = 'figures/economy'

    @staticmethod
    def consumer_spending(plot_type, toc=None):
        # plot_type = st.selectbox('', ['heat_map', 'line_plot'], key='dsfasf')
        _st_image(
            image_path=f'{Economy.ROOT}/consumer_spending/card_spending_change_{{plot_type}}.pdf',toc=toc
        )

    @staticmethod
    def employment(plot_type, toc=None):
        _st_image(
            image_path=f'{Economy.ROOT}/employment/active_employees_change_{{plot_type}}.pdf',toc=toc
        )

    @staticmethod
    def job_postings(plot_type, toc=None):
        # _st_image(
        #     image_path=f'{Economy.ROOT}/job_postings/new_job_postings_change_by_job_zone_{{plot_type}}.pdf',
        # )
        _st_image(
            image_path=f'{Economy.ROOT}/job_postings/new_job_postings_change_by_sector_{{plot_type}}.pdf',toc=toc
        )

    @staticmethod
    def real_estate_activity(plot_type, toc=None):
        _st_image(
            image_path=f'{Economy.ROOT}/real_estate_activity/real_estate_activity_change_line_plot.pdf',toc=toc
        )
    
    @staticmethod
    def small_business_openings(plot_type, toc=None):
        _st_image(
            image_path=f'{Economy.ROOT}/small_business_opening/open_small_businesses_change_{{plot_type}}.pdf',toc=toc
        )

    @staticmethod
    def small_business_revenue(plot_type, toc=None):
        _st_image(
            image_path=f'{Economy.ROOT}/small_business_revenue/small_business_revenue_change_{{plot_type}}.pdf',toc=toc
        )


class PublicHealth:
    ROOT = 'figures/public_health'

    @staticmethod
    def covid_19_case(plot_type=None, toc=None):
        # st.subheader('Covid-19 Cases')
        _st_image(image_path=f'{PublicHealth.ROOT}/covid_19_case/case_count_by_city_line_plot.pdf')
        _st_image(
            image_path=f'{PublicHealth.ROOT}/covid_19_case/case_count_by_zip_code_line_plot.pdf',toc=toc
        )

    @staticmethod
    def covid_19_policy(toc=None):
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
        try:
            toc.subheader(file['title'])
        except:
            st.subheader(file['title'])
        st.markdown(df.set_index('Date').to_markdown())
        
        caption = f'{file["caption"]} \n\n**Data source:** [{file["source"]["name"]}]({file["source"]["url"]})'
        st.write(caption)

class Transport:
    ROOT = 'figures/transport_and_mobility'

    @staticmethod
    def place_stay(plot_type, toc=None):
        _st_image(
            image_path=f'{Transport.ROOT}/place_stay/time_spent_and_visit_change_{{plot_type}}.pdf',toc=toc
        )

    @staticmethod
    def public_transit_ridership(plot_type, toc=None):
        _st_image(
            image_path=f'{Transport.ROOT}/public_transit_ridership/public_transit_ridership_distribution_{{plot_type}}.pdf',toc=toc
        )
        # _st_image(
        #     image_path=f'{Transport.ROOT}/public_transit_ridership/public_transit_ridership_distribution_line_plot.pdf'
        # )

    @staticmethod
    def road_traffic(plot_type, toc=None):
        _st_image(
            image_path=f'{Transport.ROOT}/road_traffic/road_intersection_traffic_volume_change_{{plot_type}}.pdf',toc=toc
        )
        # _st_image(
        #     image_path=f'{Transport.ROOT}/road_traffic/road_intersection_traffic_volume_distribution_line_plot.pdf',
        # )

    @staticmethod
    def transit_mode(plot_type, toc=None):
        _st_image(
            image_path=f'{Transport.ROOT}/transit_mode/direction_request_change_{{plot_type}}.pdf',toc=toc
        )

class CivilInfrastructure:
    ROOT = 'figures/energy_and_water'

    @staticmethod
    def water_energy_demand(plot_type, toc=None):
        _st_image(image_path=f'{CivilInfrastructure.ROOT}/water_energy_demand/water_and_wastewater_treatment_energy_change_line_plot.pdf',toc=toc)

class SocialWelfare:
    ROOT = 'figures/social_welfare'

    @staticmethod
    def citizen_need(plot_type, toc=None):
        _st_image(image_path=f'{SocialWelfare.ROOT}/citizen_need/need_related_call_count_{{plot_type}}.pdf',toc=toc)
