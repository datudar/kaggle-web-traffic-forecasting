## Kaggle's "Web Traffic Time Series Forecasting" Competition

This model is my submission to Kaggle's "Web Traffic Time Series Forecasting" Competition. It makes web traffic predictions using [Facebook's Prophet package](https://github.com/facebook/prophet). 

### Introduction

The competition asks participants to predict daily web traffic of about 145,000 wikipedia articles. For more detailed information including rules and guidelines, visit the competition website [here](https://www.kaggle.com/c/web-traffic-time-series-forecasting).

### Implementation

Run the **web_traffic_forecasting_model.py** file. 

*Note: Prophet can only make a prediction on a single time series at a time. Therefore, I loop through each individual website to obtain the predictions, and on my machine (Mid-2014 MacBook Pro), the model takes about 4 days to finish.*

Due to space limitations on github, I only include the model file; however, to run the model, you also need to download and save the two input files to the same directory as the model file.

### Input files for second round

The following data files are required:
- train_2.csv
- key_2.csv

### Output files for second round

There is only one output file, which is the submission file:
- submission_2.csv