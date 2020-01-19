import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv(r"C:\Users\sousa\Desktop\github\SODeveloperSurvey\Data\survey-results-public.csv")
schema = pd.read_csv(r"C:\Users\sousa\Desktop\github\SODeveloperSurvey\Data\survey-results-schema.csv")


## A Look at the Data
# Solution to Question 1
num_rows = df.shape[0]
num_cols = df.shape[1]

# Solution to Question 2
no_nulls = set(df.columns[df.isnull().mean()==0])

# Solution to Question 3
most_missing_cols = set(df.columns[df.isnull().mean() > 0.75])

## How To Break Into the Field
# Solution to Question 1
def get_description(schema, column_name):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT -
            desc - string - the description of the column
    '''
    desc = list(schema[schema['Column'] == column_name]['Question'])[0]
    return desc

descrips = set(get_description(schema, col) for col in df.columns)

# Solution to Question 4
higher_ed = lambda x: 1 if x in ("Master's degree", "Doctoral", "Professional degree") else 0

df['HigherEd'] = df["FormalEducation"].apply(higher_ed)
higher_ed_perc = df['HigherEd'].mean()


# Solution to Question 6
sol = {'Everyone should get a higher level of formal education': False,
       'Regardless of formal education, online courses are the top suggested form of education': True,
       'There is less than a 1% difference between suggestions of the two groups for all forms of education': False,
       'Those with higher formal education suggest it more than those who do not have it': True}
