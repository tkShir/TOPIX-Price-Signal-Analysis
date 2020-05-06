# TOPIX-Price-Signal-Analysis  

## Overview
This project attempts to determine whether Nikkei 225, a Japanese Stock Index, will rise or fall, based on other global stock index as well as foreign exchange rate. The data used were from 01/01/2014 to 12/31/2019. If there were missing values in data, average of the respective data set were used.  

The Indexes used are:  
* Dow Jones (DJI)  
* S&P 500 (GSPC)  
* NASDAQ (IXIC)  
* Russell 2000 (RUT)  
* Euro Stoxx 50 (STOXX50E)  
  
The foreign exchange rates used are:  
* US Dollar  
* British Pound  
* Euro  
* Canadian Dollar  
* Swiss Franc  
* Swedish Krona  
* Danish Krone  
* Norway Krone  
* Australian Dollar  
* New Zealand Dollar  
* South African Rand  
* Bahraini Dinar  
* Chinese Yuan  
* Hong Kong Dollar  
* Indian Rupee  
* Philippine Peso  
* Singapore Dollar  
* Thai Baht  
* Kuwaiti Dinar  
* Saudi Riyal  
* United Arab Emirates Dirham  
* Mexican Peso  
* Papua New Guinean Kina  
* Hungarian Forint  
* Czech Koruna  
* Polish Złoty  
* Indonesian Rupiah *  
* Malaysian Ringgit  
* South Korean Won *  
* New Taiwan Dollar  
      * : Currency with this mark has been divided by 100 from its true value for the sake of simplicity  
  
## Result  
Accuracy with Test Data: 64.65517241379311%  

Cross-Validation scores: [0.64655172, 0.66810345, 0.68534483, 0.56034483, 0.65652174]  
Average score: 0.6433733133433284  

## Files
### DJI.csv, GSPC.csv, IXIC.csv, N225.csv, RUT.csv, STOXX50E.csv
Raw data of stock indexes
### FX.csv
Raw data of FX indexes
### result.csv
Processed data combining all of stock indicies data, fx data, and price signal data, matched by dates of each data
### createDF.py
Python program which:  
* Processes each csv and combines them into a single data frame  
* Outputs the result to result.csv
### processDF.py
Python program which:  
* Processes the result.csv by identifying increase/decrease in closing price of Nikkei 225 index  
* Process the data to be prepared for training
* Using Grid Search and Support Vector Machine to create a model
* Checking and validating the result of the model
