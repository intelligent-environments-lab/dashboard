# dashboard
 Experimental covid dashboard

## Dependencies 
Install streamlit from conda forge:

``` conda install -c conda-forge streamlit ```

## Running it locally 
In anaconda prompt, run the following command in the repo's folder:

``` streamlit run app.py```

A browser window will automatically start.

View it here: https://share.streamlit.io/intelligent-environments-lab/dashboard/main/app.py

## Next Steps
Content creators need to decide on content/features...

  - Which graphs and what to talk about?
  - What kind of interactive elements do we want to provide the users (buttons, sliders, pan/zoom, multiple pages)?
  
  - Pngs will probably be replaced with figure objects passed directly through code to streamlit
  - Do we keep seaborn plots or replaced them with ones created by graphing libraries that support more interaction (plotly, bokeh, etc)?
  

## Resources

https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4

https://medium.com/swlh/building-interactive-dashboard-with-plotly-and-streamlit-2c390bcfd41a
