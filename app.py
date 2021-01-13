# -*- coding: utf-8 -*-
import streamlit as st
from pdf2image import convert_from_path,convert_from_bytes
import requests
import plotly.express as px
import pandas as pd

repo = "https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main"

def pdf2img(url):
    pdf = convert_from_bytes(requests.get(url).content)[0]
    return pdf

def economy(plot_type=None):
    dir = f'{repo}/figures/economy'
    st.header('Economy')
    expander = st.beta_expander("View plots")
    with expander:
        st.subheader('Consumer Spending')
        st.image(pdf2img(f'{dir}/consumer_spending/card_spending_change_{plot_type}.pdf'), use_column_width=True,caption=f"card_spending_change_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/consumer_spending/card_spending_change_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/consumer_spending/card_spending_change_line_plot.pdf'), use_column_width=True)

        st.subheader('Employment')
        st.image(pdf2img(f'{dir}/employment/active_employees_change_{plot_type}.pdf'), use_column_width=True,caption=f"active_employees_change_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/employment/active_employees_change_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/employment/active_employees_change_line_plot.pdf'), use_column_width=True)

        st.subheader('Job Postings')
        st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_job_zone_{plot_type}.pdf'), use_column_width=True,caption=f"new_job_postings_change_by_job_zone_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_job_zone_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_job_zone_line_plot.pdf'), use_column_width=True)
        st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_sector_{plot_type}.pdf'), use_column_width=True,caption=f"new_job_postings_change_by_sector_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_sector_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_sector_line_plot.pdf'), use_column_width=True)

        st.subheader('Small Business Openings')
        st.image(pdf2img(f'{dir}/small_business_opening/open_small_businesses_change_{plot_type}.pdf'), use_column_width=True,caption=f"open_small_businesses_change_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/small_business_opening/open_small_businesses_change_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/small_business_opening/open_small_businesses_change_line_plot.pdf'), use_column_width=True)

        st.subheader('Small Business Revenue')
        st.image(pdf2img(f'{dir}/small_business_revenue/small_business_revenue_change_{plot_type}.pdf'), use_column_width=True,caption=f"small_business_revenue_change_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/small_business_revenue/small_business_revenue_change_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/small_business_revenue/small_business_revenue_change_line_plot.pdf'), use_column_width=True)

def transport(plot_type=None):
    dir = f'{repo}/figures/transport_and_mobility'
    st.header('Transport & Mobility')
    expander = st.beta_expander("View plots")
    with expander:
        st.subheader('Place Stay')
        st.image(pdf2img(f'{dir}/place_stay/time_spent_and_visit_change_{plot_type}.pdf'), use_column_width=True,caption=f"time_spent_and_visit_change_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/place_stay/time_spent_and_visit_change_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/place_stay/time_spent_and_visit_change_line_plot.pdf'), use_column_width=True)

        st.subheader('Transit Mode')
        st.image(pdf2img(f'{dir}/transit_mode/direction_request_change_{plot_type}.pdf'), use_column_width=True,caption="direction_request_change_{plot_type}.pdf")
        # st.image(pdf2img(f'{dir}/transit_mode/direction_request_change_heat_map.pdf'), use_column_width=True)
        # st.image(pdf2img(f'{dir}/transit_mode/direction_request_change_line_plot.pdf'), use_column_width=True)

def main():
    #st.set_page_config(layout="wide")
    st.title('IEL Covid-19 Dashboard')
    st.sidebar.header('Sidebar')
    plot_type = st.sidebar.selectbox('Plot Type',['Heatmap', 'Line'])

    if plot_type == 'Heatmap':
        plot_type = 'heat_map'
    else:
        plot_type = 'line_plot'
    economy(plot_type)
    transport(plot_type)

main()

st.header("Examples and References")
examples_expander = st.beta_expander("Expand")
with examples_expander:
    st.write("As the plots below show, traffic demand decreased during the pandemic.")
    st.image("plots/Average Combined commute Vehicle Traffic across all Locations.png", caption="Average Combined commute Vehicle Traffic across all Locations.png")
    st.image("plots/Combined commute Vehicle Traffic Data Heat Map.png",width=600)
    # st.image(f"{covid19}/plots/air_quality/Austin%20Air%20Quality%20Mean%20Concentration%20from%202015-2020.png?token=AN5AK2C2JPCCDXOI4JEXUQTAAIF2C",\
    #          caption="This is a caption. The above image is a png.", width=800)




    st.markdown("""
    <embed src="https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main/figures/transport_and_mobility/transit_mode/direction_request_change_heat_map.pdf" width="400" height="400">
    """, unsafe_allow_html=True)
    
    st.write("API Reference here: https://docs.streamlit.io/en/stable/api.html")
    st.latex("This\ is\ latex: y=mx+b")
    st.markdown("Github *Flavored* __markdown__?")
    us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
    st.write(us_cities)
    px.set_mapbox_access_token('pk.eyJ1IjoiY2xpbjI2NSIsImEiOiJja2NuaXpkZjMwMnEyMnJxcGQ4YTM2aTY5In0.4mHf-EjuvLGnivDWEr4uKA')
    fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    #Note: only mapbox styles that require a token will work, so no "open-street-map" and the like
    fig.update_layout()#mapbox_style="dark")

    st.plotly_chart(fig)
    st.header("Header")
    st.subheader("Subheader")
    st.subheader("Example code")
    st.code("""
    # -*- coding: utf-8 -*-
    import streamlit as st
    from pdf2image import convert_from_path,convert_from_bytes
    import requests

    repo = "https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main"

    def pdf2img(url):
        pdf = convert_from_bytes(requests.get(url).content)[0]
        return pdf

    def economy(plot_type=None):
        dir = f'{repo}/figures/economy'
        st.header('Economy')
        expander = st.beta_expander("View plots")
        with expander:
            st.subheader('Consumer Spending')
            st.image(pdf2img(f'{dir}/consumer_spending/card_spending_change_{plot_type}.pdf'), use_column_width=True)

            st.subheader('Employment')
            st.image(pdf2img(f'{dir}/employment/active_employees_change_{plot_type}.pdf'), use_column_width=True)

            st.subheader('Job Postings')
            st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_job_zone_{plot_type}.pdf'), use_column_width=True)
            st.image(pdf2img(f'{dir}/job_postings/new_job_postings_change_by_sector_{plot_type}.pdf'), use_column_width=True)


            st.subheader('Small Business Openings')
            st.image(pdf2img(f'{dir}/small_business_opening/open_small_businesses_change_{plot_type}.pdf'), use_column_width=True)

            st.subheader('Small Business Revenue')
            st.image(pdf2img(f'{dir}/small_business_revenue/small_business_revenue_change_{plot_type}.pdf'), use_column_width=True)

    def transport(plot_type=None):
        dir = f'{repo}/figures/transport_and_mobility'
        st.header('Transport & Mobility')
        expander = st.beta_expander("View plots")
        with expander:
            st.subheader('Place Stay')
            st.image(pdf2img(f'{dir}/place_stay/time_spent_and_visit_change_{plot_type}.pdf'), use_column_width=True)

            st.subheader('Transit Mode')
            st.image(pdf2img(f'{dir}/transit_mode/direction_request_change_{plot_type}.pdf'), use_column_width=True)

    def main():
        #st.set_page_config(layout="wide")
        st.title('IEL Covid-19 Dashboard')
        st.sidebar.header('Sidebar')
        plot_type = st.sidebar.selectbox('Plot Type',['Heatmap', 'Line'])

        if plot_type == 'Heatmap':
            plot_type = 'heat_map'
        else:
            plot_type = 'line_plot'
        economy(plot_type)
        transport(plot_type)
        
    main()

    examples_expander = st.beta_expander("Examples and references")
    with examples_expander:
        st.write("As the plots below show, traffic demand decreased during the pandemic.")
        st.image("plots/Average Combined commute Vehicle Traffic across all Locations.png", caption="Average Combined commute Vehicle Traffic across all Locations.png")
        st.image("plots/Combined commute Vehicle Traffic Data Heat Map.png",width=600)
        # st.image(f"{covid19}/plots/air_quality/Austin%20Air%20Quality%20Mean%20Concentration%20from%202015-2020.png?token=AN5AK2C2JPCCDXOI4JEXUQTAAIF2C",\
        #          caption="This is a caption. The above image is a png.", width=800)

        st.markdown(\"""
        <embed src="https://raw.githubusercontent.com/intelligent-environments-lab/dashboard/main/figures/transport_and_mobility/transit_mode/direction_request_change_heat_map.pdf" width="400" height="400">
        \""", unsafe_allow_html=True)
        st.header("Examples and References")
        st.write("API Reference here: https://docs.streamlit.io/en/stable/api.html")
        st.latex("This\ is\ latex: y=mx+b")
        st.markdown("Github *Flavored* __markdown__?")
        st.header("Header")
        st.subheader("Subheader")
        st.subheader("Example code")
    """
    )