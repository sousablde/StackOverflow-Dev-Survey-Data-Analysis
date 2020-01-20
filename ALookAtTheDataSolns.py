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


## Job Satisfaction?
# Question 1
job_sol_1 = {'The proportion of missing values in the Job Satisfaction column': 0.214,
             'According to EmploymentStatus, which group has the highest average job satisfaction?': 'contractors',
             'In general, do smaller companies appear to have employees with higher job satisfaction?': 'yes'}

# Question 2
job_sol_2 = {'Do individuals who program outside of work appear to have higher JobSatisfaction?': 'yes',
             'Does flexibility to work outside of the office appear to have an influence on JobSatisfaction?': 'yes', 
             'A friend says a Doctoral degree increases the chance of having job you like, does this seem true?': 'yes'}

# What Happened?
# Question 1
desc_sol = {'A column just listing an index for each row': 'Respondent',
       'The maximum Satisfaction on the scales for the survey': 10,
       'The column with the most missing values': 'ExpectedSalary',
       'The variable with the highest spread of values': 'Salary'}

# Question 2
scatter_sol = {'The column with the strongest correlation with Salary': 'CareerSatisfaction',
       'The data suggests more hours worked relates to higher salary': 'No',
       'Data in the ______ column meant missing data in three other columns': 'ExpectedSalary',
       'The strongest negative relationship had what correlation?': -0.15}

# Question 3
a = 'it is a way to assure your model extends well to new data'
b = 'it assures the same train and test split will occur for different users'
c = 'there is no correct match of this question'
d = 'sklearn fit methods cannot accept NAN values'
e = 'it is just a convention people do that will likely go away soon'
f = 'python just breaks for no reason sometimes'

lm_fit_sol = {'What is the reason that the fit method broke?': d,
       'What does the random_state parameter do for the train_test_split function?': b,
       'What is the purpose of creating a train test split?': a}

## Your Turn
# Question 1
prop_sals = 1 - df.isnull()['Salary'].mean()
# Question 2
num_vars = df[['Salary', 'CareerSatisfaction', 'HoursPerWeek', 'JobSatisfaction', 'StackOverflowSatisfaction']]
sal_rm = num_vars.dropna(subset=['Salary'], axis=0)
# Question 3
question3_solution = 'It broke because we still have missing values in X'
# Question 4
all_rm = num_vars.dropna()
# Question 5
question5_solution = 'It worked, because Python is magic.'
# Question 6
r2_test = 0.019170661803761924
# Question 7
question7_solution = {'The number of reported salaries in the original dataset': 5009,
                       'The number of test salaries predicted using our model': 645,
                       'If an individual does not rate stackoverflow, but has a salary': 'We still want to predict their salary',
                       'If an individual does not have a a job satisfaction, but has a salary': 'We still want to predict their salary',
                       'Our model predicts salaries for the two individuals described above.': False}