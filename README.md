# Self-learning Projects

This repository serves as a hub for miscellaneous self-learning projects related to data and machine learning. Each project is partitioned into its own directory in the repository root. With this, it is easier for me to see the topics that I have already explored and helps me understand what possible gaps I might still have in my understanding. 
This repository is not designed to contain production-grade code or even be structured in a way that is conducive for easy clone-and-run code, but as mentioned, is meant for collecting all different projects and learning opportunities into one :)


To ease navigation, all projects are collected below in a table showing their theme and code availability. Projects are ordered by their year of completion.

| Project Name | Theme| Language/method of delivery | Code in Repo| Year | 
|-| -| -| -| - |
|[2D Shape Recognition](https://github.com/rasmussiljander/self-learning/tree/main/2D_shape_recognition) | Image Classification | Jupyer Notebooks| Yes | 2024 |
|[[Master's Thesis] Extreme gradient boosting methods for housing market demand forecasting](#masters-thesis-2023-extreme-gradient-boosting-methods-for-housing-market-demand-forecasting) | Time series forecasting | Python | No | 2023 |
|[Capturing Discriminative Attributes From Language](#capturing-discriminative-attributes) | ML in NLP | Python| No | 2023 |
|[Finnish Domestic Migration Analysis](https://github.com/rasmussiljander/self-learning/tree/main/finnish-domestic-migration) | Networks + Data-analysis| Python + Jupyter Notebooks| Yes | 2022 |
|[Forecasting Food Orders](https://github.com/rasmussiljander/self-learning/tree/main/food_orders_forecasting) | Time-series Forecasting | Jupyter Notebooks| Yes | 2021 |
|[cGANs for MRI modality conversion](#cgans-for-mri-modality-conversion) | Image-to-Image translation with DL | Python | No | 2021 |
|[[Bachelor's Thesis] Non-linear regression for autoantibody analysis in type 1 diabetes](#bachelors-thesis-2020-non-linear-regression-for-autoantibody-analysis-in-type-1-diabetes) | Non-linear Regression | Python + R | No | 2020 |
|[Bayesian Binomial-Logit models for basketball shot likelihoods](#modeling-nba-shooting-percentages) | Bayesian Data Analysis | R + Stan (Rmd) | No | 2020 |
|[Herd Simulation](https://github.com/rasmussiljander/self-learning/tree/main/food_orders_forecasting) | Physics Animation | Python | Yes | 2019 |
|[Student Register](https://github.com/rasmussiljander/self-learning/tree/main/student_register) | Beginner Project | C | Yes | 2019 |


Below are short explanations of each project. See also [Future Projects](#future-projects) for ideas and plans for future possible projects.

### 2D Shape Recognition

`2D_shape_recognition/`

A simple deep learning project, training a convolutional neural network from scratch to classify images into circles, squares, or triangles. The project serves as a quick review of CNNs and helps me refresh what I already learned in school and have something similar that I have implemented in my own.

### Finnish Domestic Migration Analysis
`finnish-domestic-migration/`

An analysis into domestic migration flows inside Finland. The project was done as part of a network analysis course. The progress report in `docs/` has interesting images about various migration insights in Finland over 2020 and throughout the past 40 years.



### Food Orders Forecasting

A very simple SARIMA project that was completed as a task part of a summer internship application in 2021. The project was completed locally but migrated to this repo in 2024. 


### Herd Simulation

A fully designed herd simulation program (2019), that executes a random herd-type visual simulation of self-driving 2D cars, using the package `PyQt5`. More information about this old `Python` can be found (in Finnish) in the `docs/` directory. This was also added in the `reports/` directory that contains miscellaneous older school project reports.


### Student Register

`student_register/`

An old (2018) project work for a C programming basics course. 
The project is a simple CLI student register that allows you to add students to a register and dynamically control their information.

### Other projects

#### Bachelor's Thesis (2020): Non-linear regression for autoantibody analysis in type 1 diabetes

I completed my Bachelor's Thesis (B.Sc.) in 2020 with the thesis title of 

```
Non-linear regression methods in open-source platforms for autoantibody analysis in type 1 diabetes
```

Basically I investigated if I could replicate a "4-parameter Logistic Regression" algorithm with open-source software.
This could have helped the acceleration of digitalization in the research group that I completed the thesis in. 
I actually wrote the algorithm with both R and Python: I first wrote the algorithm in R as at the time I was more experienced with it, but later replicated and improved the algorithm in Python in order to make a thesis out of it. 
Unfortunately the code is not available to share, but the full thesis is available for reading in [reports/bsc_thesis_4pl_regression.pdf](https://github.com/self-learning/tree/main/reports/bsc_thesis_4pl_regression.pdf)

Below is an part from the abstract:

*tGADA96-585 can be analyzed with a four-parameter logistic (4PL) regression model. Analysis is usually done with specialized software, but due to the availability of open-source (OS) platforms, it is relevant to evaluate whether OS programs can replicate the analysis. Using details from the MultiCalcTM (Wallac OY, Turku, Finland) product manual, a novel Python program was built and evaluated.*

#### Master's Thesis (2023): Extreme gradient boosting methods for housing market demand forecasting

I completed my Master's Thesis (M.Sc.) in 2020 with the thesis title of 

```
Extreme gradient boosting methods for covariate forecasting of housing market demand in Finnish postal code areas
```

The thesis was a Python-based program that loaded data from various sources, processed them, and fit an extreme-boosted based model that forecasted residential housing market demand into the future.


I wrote the project in collaboration with my employer and hence unfortunately due to business interests, I cannot share the code or the results. 



#### cGANs for MRI modality conversion

A university group project where we designed a Conditional Generative Adversarial Neural Net (cGAN) for converting the modality (weighting) of MRI brain images. The project was written using `TensorFlow`.
   - Project presentation: [reports/mri_modality_conversion](https://github.com/self-learning/tree/main/reports/mri_modality_conversion.pdf)
   - Link to private repo : [link](https://github.com/tonipel/mri-modality-conversion)
   - TensorFlow description of `pix2pix` algorithm that the model is based on: [pix2pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
   - Conditional Adversarial Nets: [research paper](https://arxiv.org/abs/1611.07004)


#### Capturing Discriminative Attributes

A human language engineering group project that tackled the SemEval 2018 Task 10. The task is about being able to model discriminative features between two words, or in other words, be able to model what makes them different from each other. Our approach was testing combining GloVe embeddings with XGBoost classifiers, support vector machines, and Multi-layer perceptrons to be able to predict whether two words are different from each other or not. The project was written with `Python`.

- Project Report: [reports/Report_DiscAttDect.pdf](https://github.com/rasmussiljander/self-learning/blob/main/reports/Report_DiscAttDect.pdf)
- Private Repo: [link](https://github.com/luciaurcelay/Capturing-Discriminative-Attributes)
- Task description: [link](https://aclanthology.org/S18-1117/)


#### Modeling NBA Shooting Percentages

Project work a course Bayesian Data Analysis. Uses Bayesian probabilistic modeling tools, implemented in R and Stan, to construct models for estimating changes in NBA basketball shot success likelihoods, depending on shot distance and shot type. The model was a Bayesian Binomial-Logit model. The report consists of the follwing essential sections:

1. Introduction of the problem, data, and mathematical model
2. Stan model code
3. Model execution and convergence diagnostics (Rhat, ESS)
4. Posterior predictive checks
5. Model Comparison (PSIS-LOO, Pareto k-values)
6. Predictive performance assessment and sensitivity analysis

Only the report (written with RMarkdown in RStudio) is included, found in the folder [reports/bayesian_basketball_model](https://github.com/self-learning/tree/main/reports/bayesian_basketball_model/). The source code available upon request.


### Github Actions

The Github Actions in this repo are mainly used to practice the use of GH Actions. As there is no production code or model maintenance, there will be no model update, automatization, data loading, or other scheduling. 
There are however, some simple checks that are run that help learn Actions. 
There will be more workflows added as needed, but below is the list of current workflows:
- **Jupyter Notebook linting**: The Python code snippets in all repo notebooks are `flake8`, `black` linted using the package `nbqa`. The workflows are supposed to fail if poorly formatted code is detected. The workflows are triggered on all branches for all commmits and pull request activities. There is no separate scheduling for these workflows.
- **Python Documentation**: The existence of Python docstrings in functions and classes is checked by the package `interrogate`. It fails the check if less than 80% of the code base is documented. It does not evaluate the quality of the docs, but focuses on the simple existence of docstring - the quality is left as resposibility of the developer!




## Future Projects

Naturally, theres only so any hours in a day, and there's no way for me to have time to complete all little cool projects that come to mind. Therefore, below are listed some project plans that could be really interesting and useful to do. 


### ML Model + API endpoint 


Hosting some model on with an endpoint. show end-to-end process, including preprocessing, modeling, api, etc.

- data exploration notebooks
- python code for productization
- API + API documentation

#### Data

- description where from
- how to load it
- Use exploration to provide guidelines for preprocessing.
- Will be uploaded/maintained in an S3 bucket, if pricing free --> check the pricing when you get to this.

#### Model

The type of model obviously depends on the problem definition, but from an API-design point-of-view, a good option would be a model, where we can achieve insights with minimal API input. For example, image classifiers are a bit challenging for simple API project, as they require input images to be predicted. In other words, models for which the input features space can be efficiently given should be favored.

Options:
- [Residential area clusters] (#finnish-residential-area-analysis-and-clustering) (classification)
- Football game outcode predictions (classification)
- Forecasting tourism in Helsinki (time series forecasting)
- Regression tasks for any domain: Price, size, quantity, time between events, sucess, probability of an event occuring, etc.


#### Architecture

- All written in Python
- Model: use of packages depending on architecture (+ comparison of options)
- API: either FastAPi or Flask, probably FastAPI better of simple API



Below is a visualization of the approximate file structure that the project should have
```
├── data 
│ ├── raw
│ └── processed
├── notebooks
│ ├── data_exploration
│ └── model_prototyping
├── src
│ ├── preprocessing
│ ├── training
│ ├── validation
│ └── utils
├── app
│ ├── openapi_schema.yml
│ ├── endpoint
│ └── utils
├── models
├── reports
├── environment.yml
├── README.md
```


## Finnish residential area analysis and clustering

Tilastokeskus, HKI Open API offer demographic data + time-series about Finnish residential areas ([link](https://www.avoindata.fi/data/en_GB/dataset/helsingin-seudun-aluesarjat-tilastotietokannan-tiedot-paikkatietona))
--> would it be possible to group these areas together by profile? Find distinct differences, factors that make them unique? Is it possible to find some simple-language profile names for each, e.g. `Family-friendly`, `Fast-growing`, etc.? 

This would require quite a lot of exploration of the data and what is available. The modeling could be done with Python, and maybe it would be a good idea to start off with a simple unsupervised approach such as KNN or equivalent. This could be also coupled with dimension reduction to try to help the modeling a bit.

This would probably mostly be done with Jupyter Notebooks, but if interesting models are found, some endpoints/etc. could be designed. Also, since most of the data is provided with time-series, it would be interesting to introduce some temporal aspect as well --> how have districts changed over time? Can some profile-change be predicted in the future?

### Outcomes

This project was several possible outcomes, and with closer planning and discovery the scope can be specified, but below are possible options

1. **Elaborate data exploration** : Really just get to know the data well. Find interesting things that you didn't imagine you would find!
2. Area profile classifier: For a user-input of a region, a model will output a profile associated with that region.
3. Area profile insights: This is the most elaborate and advanced option of this project. For an area input, the user will not only receive an area profile, but a report of insights associated with that region and profile. This could include Top 3 similar regions, variables that characterize that region, its history, and visualizations on a map.


## Data validation and automation pipelines

Pipelines for validating and ensuring that data is loaded and run in a correct way
This can be done in several ways
- Airflow + Great Expectations
- `dbt`

The important is finding some interesting dataset with which you could do this.


## Other possible project ideas:

- **LLM models**: There are an infinite different possibilities that LLMs can nowadays do, but here's a couple of things that could be interesting to test out.
   - Time series analysis with LLMs
      - There is a parallel between sequential relationships of time series and langauge sentences. Therefore I imagine that LLMs could work quite well with time series data as well, and in fact, there already exists some papers about the topic: [Repo](https://github.com/liaoyuhua/LLM4TS)
   - Data Science Job Application letter analysis
      - Perhaps LLMs could be tought to a) pick up mentions of hard skills; b) understand semantics, mood, and tone. This could help better understand what kind of a person the applicant is, and how they could fit into the team in question. 
      - It would be interesting to also see if the model could learn to valuate different projects and experience, and be able to tell if some features differentiate the applicant better. 
      - This biggest issue would probably be the context that the model would need to learn, as well as the quantification of this applicant value: what makes this person particularly valuable?
- Data Exploration + modeling with `R`
   - Show that you actually have experience with `R`.
   - For example, one that is interesting to me is tourism data in Finland: has tourism increased in Finland, what makes people want to come to Finland?
      - Link to data: [link](https://www.avoindata.fi/data/en_GB/dataset/visit-finland-matkailijamittari/resource/2c326fd2-3437-4d95-a71d-cc713f095e69?view_id=36b0485a-8e59-484a-98e5-9be35085d881)
   - Other intersting dataset: [Weather warnings in Finland](https://www.ilmatieteenlaitos.fi/varoitusten-latauspalvelun-pikaohje)
      - How is climate change happening in Finland? Have weather phenomena gotten more extreme over the past 20 years? What can we expect to happen?



