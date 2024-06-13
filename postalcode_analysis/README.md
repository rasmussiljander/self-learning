# Finnish postal code area analysis


one point of the notebooks is to review and prepare the data so that it can be used in the clustering task.

i did this in parts because it was a lot easier to get a better understanding of feature sets when evaluating them by smaller groups + the columns were already divided into groups by theme. 

To improve: Bring timeframe into question, a.k.a calculate changes in these values
- yoy change
- 5 year change

To improve: bring in migration figures? 
- i dont know what to do with this though, because i will probably only be able to get municipality-level migration figures --> postcodes in municipality will get same values --> data will force algorithm to group same-municipality postcodes together. 


## Project Description

This project aims to explore Finnish postal code areas using Paavo data. Paavo is a comprehensive dataset provided by Statistics Finland, which contains various socio-economic and demographic information at the postal code level.

The main objectives of this project are:

1. Data Collection: Retrieve the Paavo dataset for Finnish postal code areas.
2. Data Preprocessing: Clean and transform the raw data into a suitable format for analysis.
3. Exploratory Data Analysis: Perform descriptive statistics, visualizations, and uncover insights about the postal code areas.
4. Geospatial Analysis: Utilize geospatial techniques to visualize the distribution of variables across different postal code areas.
5. Statistical Modeling: Apply statistical models to identify patterns, correlations, and potential predictors within the dataset.
6. Interpretation and Reporting: Summarize the findings, draw conclusions, and present the results in a clear and concise manner.

By conducting this analysis, we aim to gain a deeper understanding of the socio-economic and demographic characteristics of Finnish postal code areas. This information can be valuable for various purposes, such as urban planning, market research, and resource allocation.

## Data Sources

The primary data source for this project is the Paavo dataset provided by Statistics Finland. The dataset includes variables such as population, age distribution, education level, income, and more at the postal code level.

## Tools and Technologies

The following tools and technologies will be used for this project:

- Programming Language: Python
- Data Manipulation and Analysis: Pandas, NumPy
- Data Visualization: Matplotlib, Seaborn
- Geospatial Analysis: GeoPandas, Folium
- Statistical Modeling: Scikit-learn, Statsmodels
add dep management with poetry

## Project Structure

The project will be organized into the following directory structure:



Write note somewhere: also found this project half-way through and used some of its implementations


also instruct how to use poetry
- python install 
- brew install of poetry
- project init
- poetry install
- profit



pyenv install, etc


https://pxdata.stat.fi/PxWeb/pxweb/en/Postinumeroalueittainen_avoin_tieto/Postinumeroalueittainen_avoin_tieto__uusin/paavo_pxt_12f7.px/

I loaded only 2022 to begin with, maybe include other stuff later. I also did not load `A - X `-prefixed columns since I knew that I would no be needing them. I also pivoted it manually so that `Rows` were only `Postal Code` and rest were columnar information. This returned a table what had one row for each postal code area, showing its important columns. Then I saved it to a comma separated file without headings, and saved the name `paavo_2022.csv`.

https://www.reaktor.com/articles/creating-an-interactive-geoplotting-demo-experiences-with-geopandas-and-plotly
^somewhat similar to what i found here ^


(install python 3.10.8)
with e.g. pyenv install 3.10 

(choice of python was arbitrary. I could have used e.g. 3.11 but i know that newer versions wouldn't necessary be better. plus it is stable for at least the next two years.

https://devguide.python.org/versions/and 


pyenv global


if you have problems with pyenv this might help ensure that it starts up properly with MAC

```
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```


Note that I did quivkly try using poetry for this project but since it was a bit tricky, especially with multiple projets in-repo, I just defaulted back to the simple old method of using venvs manually.


# Create a virtual environment named "myenv"
python3.10 -m venv postalcode_analysis

# Activate the virtual environment
source postalcode_analysis/bin/activate


# Install packages 
pip install -r requirements.txt



You can use the API to load the data if you want: https://geo.stat.fi/geoserver/postialue/wfs

https://pxdata.stat.fi/api1.html

However API is not so good because you can only fetch 100 000 at a time