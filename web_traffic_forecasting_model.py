#==============================================================================
# Import packages
#==============================================================================

print('Import packages...')
import time     
import numpy as np
import pandas as pd
from fbprophet import Prophet

#==============================================================================
# Import data
#==============================================================================

start_time = time.time()

# Read the initial CSV file into a dataframe
df_train = pd.read_csv('train_2.csv', index_col='Page', header=0)
df_key = pd.read_csv('key_2.csv', index_col='Page', header=0)

#==============================================================================
# Clean data
#==============================================================================

site_name = df_train.index
df_train = df_train.transpose()
df_train = df_train.fillna(method='ffill')
df_train = df_train.fillna(method='bfill')
df_train = np.log(df_train[df_train != 0])
df_train = df_train.fillna(0)

#==============================================================================
# Run model
#==============================================================================

# Parameters
start = 0
end = df_train.shape[1]
periods = 62

# Initialization
index = pd.date_range(start='9/13/2017', end='11/13/2017', freq='D')
df_pred = pd.DataFrame()

for i in range(start, end):

    df = df_train.iloc[:,i]
    
    # Formatting input for Prophet model
    df = df.reset_index()
    df.columns.values[:] = ['ds', 'y']
    
    if np.sum(df['y']) > 0:
    
        model = Prophet(yearly_seasonality=True)
        model.fit(df)
        
        # Make daily forecasts 74 days out to 11/13/2017
        future = model.make_future_dataframe(periods=74)
        forecast = model.predict(future)
        
        forecast.index = forecast['ds']
        
        #model.plot(forecast)
        #model.plot_components(forecast)
    
        pred = pd.DataFrame(forecast['yhat'][forecast['ds'] >= '2017-09-13'])

    else:
    
        pred = pd.DataFrame(np.zeros((periods,1)), index=index, columns=['yhat'])    
    
    pred.rename(columns = {'yhat':site_name[i]}, inplace=True)
    
    df_pred = pd.concat([df_pred, pred], axis=1)
    
    # Keep track of forecasts
    print(i) if i % 10 == 0 else False
        
#==============================================================================
# Create submission file
#==============================================================================

# Unstack the dataframe
df_final = pd.DataFrame(df_pred.unstack())
df_final.rename(columns = {0:'Visits'}, inplace=True)
df_final.reset_index(inplace=True)
df_final['key'] = df_final['level_0'] + '_' + df_final['ds'].astype(str)

# Merge df_final with df_key
df_final = pd.merge(df_final, df_key, how='inner', left_on='key', right_on=None,
                    left_index=False, right_index=True)

# Override negative predictions with zeros
df_final['Visits'] = df_final['Visits'].apply(lambda x: 0 if x < 0 else x)

# Exponentiate the predicitions and then round up to zero decimal places
df_final['Visits'] = np.round(np.exp(df_final['Visits']), decimals=0)

# Create the submission file
df_submission = df_final.to_csv('submission_2.csv', index=False, columns=['Id','Visits'])

end_time = time.time()

print('Script completed in', time.strftime("%Hh %Mm %Ss", time.gmtime(end_time-start_time)))
