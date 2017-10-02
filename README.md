## Kaggle's "Web Traffic Time Series Forecasting" Competition

The model is my submission to Kaggle's "Web Traffic Time Series Forecasting" Competition. It makes web traffic predictions using Facebook's Prophet library package, which you can download here: [https://github.com/facebook/prophet](https://github.com/facebook/prophet)

### Introduction

The competition asked participants to predict daily web traffic of about 145,000 wikipedia articles, and I thought it would be a good opportunity to apply Prophet to an interesting problem.

The competition consisted of two rounds. The first round was a preliminary round used for training and building of models. Predictions were made for the first three months of the year using historical traffic data from the prior two and a half years. The second round lasted only a week and predictions were made for future dates from 9/13/2017 to 11/13/2017. Final scores and rankings will be based on predictions made in this second round only.

For more detailed rules and guidelines, visit the competition
website here: [https://www.kaggle.com/c/web-traffic-time-series-forecasting](https://www.kaggle.com/c/web-traffic-time-series-forecasting)

### Implementation

Run the **web_traffic_forecasting_model.py** file. 

*Note: Prophet can only make a prediction on a single time series at a time. Therefore, I loop through each individual website to obtain the predictions, and on my machine (Mid-2014 MacBook Pro), the model takes about 4 days to finish.*

Due to space limitations on github, I only include the model file. To run the model, you also need to download and save the two input files to the same directory as the model file.

### Input files for second round

The following data files are required:
- train_2.csv
- key_2.csv

### Output files for second round

There is only one output file, which is the submission file:
- submission_2.csv