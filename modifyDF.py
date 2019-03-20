import pandas as pd
import numpy as np

def modifyDF():
    res_df = pd.read_csv("result.csv", header = 0)

    print(res_df.head())



modifyDF()
