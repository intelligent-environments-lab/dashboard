import json
import traceback

import pandas as pd
import streamlit as st
from pdf2image import convert_from_bytes


def _st_image(image_path=None, caption=None, title=None, toc=None):
    # NOTE: the order of title and data['title'] results in behavior that may not
    # be expected by other api users
    title = (
        title
        or json.loads(
            open(
                image_path[: image_path.rfind(".") + 1].format(plot_type="line_plot") + "json", "r"
            ).read()
        )["title"]
    )
    toc = toc or st
    try:
        toc.subheader(title)
    except:
        pass
    # Tells streamlit to create subheader with the given title followed by an
    # image from the provided url
    if "{plot_type}" in image_path:
        labels = {"Heatmap": "heat_map", "Line": "line_plot"}
        plot_type = labels[st.selectbox("Plot type:", ["Heatmap", "Line"], key=image_path)]
        image_path = image_path.format(plot_type=plot_type)
        if "road_intersection_traffic_volume_change_line_plot" in image_path:
            image_path = image_path.replace("change", "distribution")
        if "public_transit_ridership_distribution_heat_map" in image_path:
            image_path = image_path.replace("distribution", "change")

    @st.cache(persist=False, allow_output_mutation=True, show_spinner=False, ttl=180)
    def download(image_url):
        try:
            data = json.loads(open(image_url[: image_url.rfind(".") + 1] + "json", "r").read())
        except:
            data = None
        image = open(image_url, "rb").read()
        if image_url.endswith(".pdf"):
            image = convert_from_bytes(image)[0]
        return image, data

    image, data = download(image_path)
    st.image(image, use_column_width=True, output_format="png")
    st.markdown(caption or data["caption"] or image_path[image_path.rfind("/") + 1 :])
    try:
        st.markdown(" \n\n**Insights:**" + ''.join([f"\n- {item}" for item in data["insights"]]))
    except:
        pass
    try:
        st.markdown(f' \n\n**Data source:** [{data["source"]["name"]}]({data["source"]["url"]})')
    except:
        pass

class Section:
    @classmethod
    def show(cls, items=None, toc=None):
        items=items or cls.PLOTS.keys()
        if type(items)==str:
            items=[items]
        for item in items:
            path = cls.PLOTS[item]
            try:
                _st_image(image_path=cls.PLOTS[item],toc=toc)
            except Exception as e:
                message = f"""An error occured while processing the plot 
                associated with: {path} \n\n {"".join(traceback.format_exception(None, e, e.__traceback__))}"""
                st.error(message)


class AirQuality(Section):
    ROOT = "figures/air_quality"
    PLOTS = {
        'no2':f"{ROOT}/no2_heat_map.pdf",
        'ozone':f"{ROOT}/ozone_heat_map.pdf",
        'pm2p5':f"{ROOT}/pm2_5_heat_map.pdf",
    }


class Economy(Section):
    ROOT = "figures/economy"
    PLOTS = {
        'consumer_spending':f"{ROOT}/consumer_spending/card_spending_change_{{plot_type}}.pdf",
        #'employment':f"{ROOT}/employment/active_employees_change_{{plot_type}}.pdf",
        'job_postings':f"{ROOT}/job_postings/new_job_postings_change_by_sector_{{plot_type}}.pdf",
        'real_estate_activity':f"{ROOT}/real_estate_activity/real_estate_activity_change_{{plot_type}}.pdf",
        'small_business_openings':f"{ROOT}/small_business_opening/open_small_businesses_change_{{plot_type}}.pdf",
        'small_business_revenue':f"{ROOT}/small_business_revenue/small_business_revenue_change_{{plot_type}}.pdf"
    }

class PublicHealth(Section):
    ROOT = "figures/public_health"
    PLOTS = {
        'case_count_by_city':f"{ROOT}/covid_19_case/case_count_by_city_line_plot.pdf",
        'case_count_by_zip':f"{ROOT}/covid_19_case/case_count_by_zip_code_line_plot.pdf",
        'vaccination':f"{ROOT}/covid_19_vaccination/vaccination_line_plot.pdf"
    }

    @staticmethod
    def covid_19_policy(toc=None):
        file = json.loads(
            open(
                f"{PublicHealth.ROOT}/covid_19_policy/covid19_policies_unknown_figure_type.json", "r",
            ).read()
        )
        df = pd.DataFrame(file["data"]["data"], index=file["data"]["index"], columns=file["data"]["columns"])
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%B %d, %Y")
        try:
            toc.subheader(file["title"])
        except:
            st.subheader(file["title"])

        st.markdown(df.set_index("Date").to_markdown())
        caption = f'{file["caption"]} \n\n**Data source:** [{file["source"]["name"]}]({file["source"]["url"]})'
        st.write(caption)


class Transport(Section):
    ROOT = "figures/transport_and_mobility"
    PLOTS = {
        'place_stay':f"{ROOT}/place_stay/time_spent_and_visit_change_{{plot_type}}.pdf",
        'public_transit_ridership':f"{ROOT}/public_transit_ridership/public_transit_ridership_distribution_{{plot_type}}.pdf",
        'road_traffic':f"{ROOT}/road_traffic/road_intersection_traffic_volume_change_{{plot_type}}.pdf",
        'transit_mode':f"{ROOT}/transit_mode/direction_request_change_{{plot_type}}.pdf",
        'flight_departures_city':f"{ROOT}/flight_departure/departures_destination_city_line_plot.pdf",
        'flight_departures_airline':f"{ROOT}/flight_departure/departures_airline_line_plot.pdf",
        'passenger_traffic':f'{ROOT}/flight_passenger_traffic/flight_passenger_traffic_line_plot.pdf'
    }


class CivilInfrastructure(Section):
    ROOT = "figures/energy_and_water"
    PLOTS={'water_energy_demand':f"{ROOT}/water_energy_demand/water_and_wastewater_treatment_energy_change_line_plot.pdf"}


class SocialWelfare(Section):
    ROOT = "figures/community_needs"
    PLOTS={'citizen_need':f"{ROOT}/community_needs/need_related_call_count_{{plot_type}}.pdf"}

