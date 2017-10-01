# Kaggle's "Web Traffic Time Series Forecasting" Competition

This project is my solution to Kaggle's "Web Traffic Time Series Forecasting" Competition. It uses the Facebook's Prophet package for predictions, which you can download here: [https://github.com/facebook/prophet](https://github.com/facebook/prophet)

### Introduction

The competition asks participants to predict the daily web traffic of about 145,000 wikipedia articles. For detailed rules and guidelines, visit the competition
website here: [https://www.kaggle.com/c/web-traffic-time-series-forecasting](https://www.kaggle.com/c/web-traffic-time-series-forecasting)

The competition spanned two rounds.

The first round was a preliminary round that lasted a few months so that participants could train and build their models. Predictions were made for dates in the past.

The second round lasted about a week, and this is the round that will ultimately be counted. Predictions are made for the dates in the future (9/13/2017 to 11/13/2017).

### Implementation

Run the **web_traffic_forecasting_model.py** file. Note: Currently, Prophet can only make a prediction on a single time-series at a time, so I looped through each individual website. On my machine (Mid-2014 MacBook Pro), the model took about 4 days to run.

Due to space limitations on hithub, I only include the model file and not the two input files. To run the model, you need to download the two input from the competition website and save them in the same directory as the model file.

### Input files

The following data files are needed:
- train_2.csv
- key_2.csv

# Output files

There is only one output file:
- submission_2.csv