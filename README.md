# Kaggle's "Web Traffic Time Series Forecasting" Competition

This model is my solution to Kaggle's "Web Traffic Time Series Forecasting" Competition. It makes web traffic predictions using Facebook's [Prophet](https://github.com/facebook/prophet).

## Introduction

The competition asked participants to predict web traffic of 145,000 Wikipedia articles given actual web traffic data from the prior two years.

The competition consisted of two rounds. The first round lasted for several months, and tt was a preliminary round that contestants used for training and testing of models. In this round, the predictions were actually made for a period in the past (i.e., training data from mid 2015 through 2016 was used to make predictions for the first three months in 2017). The second round lasted only a week, and the predictions were made for future dates (i.e., training data from the first round plus additional data from the beginning of 2017 are used to make predictions for September 2017 through November 2017). Final scores and rankings will be based on predictions from the second round only.

For more detailed information including rules and guidelines, please visit the [competition website](https://www.kaggle.com/c/web-traffic-time-series-forecasting).

## Model Analysis

Prophet makes predictions on time series data by combining three distinct components: a linear or logistic trend, a weekly seasonal component, and a yearly seasonal component. 

As an example, web traffic and forecast of Elon Musk's Wikipedia page is shown below. The black dots are the article's actual web traffic and the dark blue line is the prediction.

![Elon Musk's wikipedia article](example_plot.png)

The predictions are made from aggregating the three components which are shown below.

![Prophet components](example_components.png)

- The trend line reveals that there's been an significant rise in interest in Elon Musk over the past few years
- The weekly graph reveals that interest is high during the weekdays but wanes during the weekends
- The shape of the yearly seasonality is likely related to his company's earnings and product announcements as well as his interactions with the public

## Implementation

Run the **web_traffic_forecasting_model.py** file.

*Note: Prophet can only make predictions for a single time series. Therefore, to obtain predictions for all 145,000 websites, it is necessary to loop through each individual website. This takes a very long time, and on my MacBook Pro, the model took about 4 days to finish.*

Due to space limitations on Github, I do not include the input data files. To run the model, you will need to download and save the following two input files:

- train_2.csv
- key_2.csv

to the same directory as the model. You can download those files [here](https://www.kaggle.com/c/web-traffic-time-series-forecasting/data).