# dashboard
This repository hosts the code that runs the Intelligent Environments Laboratory(IEL)'s Covid-19 dashboard located at [covid19atx.net](http://covid19atx.net) . The primary motivation for this dashboard was to create an accessible platform for presenting the data-based Covid-19 research performed by IEL, which would normally only be presented in papers published to academic journals. This repository only contains the final results and plots of various different data analyses, and the actual data analysis is handled in another private repository. As noted in the private repo, this dashboard has been featured in articles by [CBS Austin](https://cbsaustin.com/news/local/new-data-from-ut-shows-drop-in-job-postings-traffic-pollution-in-2020), [UT News](https://news.utexas.edu/2021/03/17/data-shows-how-the-pandemic-changed-day-to-day-life/), [The Daily Texan](https://thedailytexan.com/2021/03/30/ut-researchers-release-new-dashboard-displaying-covid-19-effects-on-everyday-trends/) and [Reporting Texas TV](https://reportingtexas.com/austin-small-business-revenue-has-long-term-impacts-after-pandemic-study-shows/).

## Dependencies
This dashboard relies on streamlit, which is a python package that is suitable for rapid dashboard prototyping and allows data scientist to focus on their presenting their data and plots rather than trying to understand how to write html. It can be installed from pip or conda.

Install streamlit from conda forge:

``` conda install -c conda-forge streamlit ```

Additional dependencies can be found in the requirements.txt file.

## Local Usage
Dashboards created with streamlit can be hosted locally or over the internet. The dashboard at covid19atx website is hosted on a streamlit server, using their free sharing feature. However, you can also host and launch the dashboard locally by running the following command.

In anaconda prompt, run the following command in the repo's folder:

``` streamlit run app.py```

A browser window will automatically start.

The covid19atx website actually just points to this: https://share.streamlit.io/intelligent-environments-lab/dashboard/main/app.py

## Resources

https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4

https://medium.com/swlh/building-interactive-dashboard-with-plotly-and-streamlit-2c390bcfd41a
