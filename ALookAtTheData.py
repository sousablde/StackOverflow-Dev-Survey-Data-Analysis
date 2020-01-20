import pandas as pd
import numpy as np
from collections import defaultdict
import ALookAtTheDataSolns as s # come back to here

def display_gif(fn):
    return '<img src="{}">'.format(fn)


## A Look at the Data
# Question 1
def check_rows_cols(num_rows, num_cols):
    '''
    INPUT:
    num_rows - int the number of rows in df
    num_cols - int the number of cols in df

    This function will print a statement related to whether or not you provided the correct number of rows and columns of the dataset.
    '''
    if num_rows == s.num_rows:
        print("Nice job there are {} rows in the dataset!".format(num_rows))
    else:
        print("That doesn't look like what we were expecting for the number of rows.")

    if num_cols == s.num_cols:
        print("Nice job there are {} columns in the dataset!".format(num_cols))
    else:
        print("That doesn't look like what we were expecting for the number of columns.")


# Question 2
def no_null_cols(no_nulls):
    '''
    INPUT:
    no_nulls - a set of columns with no missing values

    This function will print a statement related to whether or not you provided the correct set of columns with no missing values
    '''
    if no_nulls == s.no_nulls:
        print("Nice job that looks right!")
        return display_gif('https://bit.ly/2K9X0gD')
    else:
        print("That doesn't look like for the set of no nulls.  There should be {} columns in your list".format(len(s.no_nulls)))
        return display_gif('https://bit.ly/2Hog74V')
        

# Question 3
def most_missing_cols(most_missing_cols):
    '''
    INPUT:
    most_missing_cols - a set of columns with more than 75% of the values in the column missing

    This function will print a statement related to whether or not you provided the correct set of columns with more than 75% of the values in the column missing
    '''
    if most_missing_cols == s.most_missing_cols:
        print("Nice job that looks right!")
    else:
        print("That doesn't look like for the set of most nulls.  There should be {} columns in your list".format(len(s.most_missing_cols)))

## How To Break Into the Field
# Question 1
def check_description(descrips):
    '''
    INPUT:
    descrips - should be a set of all descriptions in the dataset - each description should be a string.  You should not need to change the descrips variable at all if your function works correctly.

    This function will print a statement related to whether or not you provided the correct solution for the get_description function
    '''
    val_type = type(next(iter(descrips)))
    if descrips == s.descrips:
        print("Nice job it looks like your function works correctly!")
    elif val_type != str:
        print("Oops - Looks like your column descriptions aren't strings.")
    else:
        print("Though you did provide the correct data type, your result does not match what we were expecting.  Try again.\n\n  Your function should return the description for any column name passed to it.")


#Question 3
def total_count(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df


#Question 4
def higher_ed_test(higher_ed_perc):
    '''
    INPUT:
    higher_ed_perc - a float of the percentage of individuals who received a master's, phd, or professional degree in the stackoverflow dataframe

    This function will print a statement related to whether or not you provided the correct percentage of individuals who received a master's, phd, or professional degree in the stackoverflow dataframe
    '''
    val_type = type(higher_ed_perc)
    if higher_ed_perc == s.higher_ed_perc:
        print("Nice job!  That's right.  The percentage of individuals in these three groups is {}.".format(higher_ed_perc))
    elif val_type != float:
        print("Oops - your final result should be a decimal value associated with the proportion of individuals who are in these three categories (ex. Provide 0.50798 if ~50% of individuals are in these categories)")
    else:
        print("That doesn't look quite like expected.  You can get the percentage of 1's in a 1-0 column by using the .mean() method of a pandas series.")

#Question 6
def conclusions(sol):
    '''
    INPUT:
    sol - a dictionary with keys as strings of statements and values as True or False as to the truth of the string according to the data.

    This function will print a statement related to whether or not you provided the correct in terms of the True or False statement
    '''
    if sol == s.sol:
        print("Nice job that looks right!")
    if sol['There is less than a 1% difference between suggestions of the two groups for all forms of education']:
        print("That's not quite right.  Almost all are less than a 1% difference.  However, there is almost a 3% difference in those that ")
    if sol['Everyone should get a higher level of formal education']:
        print("That's not quite right.  The data suggests there are a number of ways to become a developer that don't require one of the categories of degree labeled as 1.")
    if not sol['Regardless of formal education, online courses are the top suggested form of education']:
        print("That's not quite right.  Notice that online courses are the top way to break into the field for both audiences.")
    if not sol['Those with higher formal education suggest it more than those who do not have it']:
        print("Not quite.  Notice that those in the 1 category pushed earning a higher degree by approximately 2 times the other group.")




## Job Satisfaction?
# Question 1
def jobsat_check1(job_sol_1):
    '''
    INPUT job_sol_1 - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if job_sol_1 == s.job_sol_1:
        print("Nice job! That's what we found as well!")
    elif job_sol_1['The proportion of missing values in the Job Satisfaction column'] != s.job_sol_1['The proportion of missing values in the Job Satisfaction column']:
        print("Oops! That first proportion doesn't look like what I was expecting.")
    elif job_sol_1['According to EmploymentStatus, which group has the highest average job satisfaction?'] != s.job_sol_1['According to EmploymentStatus, which group has the highest average job satisfaction?']:
        print("Oops! Though it wasn't what I was expecting either, the job category with the highest job satisfaction was not fulltime nor retired individuals!")
    elif job_sol_1['In general, do smaller companies appear to have employees with higher job satisfaction?'] != s.job_sol_1['In general, do smaller companies appear to have employees with higher job satisfaction?']:
        print("Looking at the average job satisfaction for each group within CompanySize, and sorting using sort_values(), there is a bit of trend don't you think?  Maybe not significant, but still an intriguing trend!")

def jobsat_check2(job_sol_2):
    '''
    INPUT job_sol_2 - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if job_sol_2 == s.job_sol_2:
        print("Nice job! That's what we found as well!")
    else:
        print("Are you sure at least one more of these wasn't true?  I thought a quick look suggested evidence for all, but maybe you found some evidence suggesting otherwise.  I did not do anymore than quick descriptive statistics to view the results. Certainly there could be confounding factors, and there is no evidence of statistically significant differences based on my solutions.")





## What Happened?
# Question 1
def describe_check(desc_sol):
    '''
    INPUT desc_sol - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if desc_sol == s.desc_sol:
        print("Nice job that looks right!")
    if desc_sol['A column just listing an index for each row'] != s.desc_sol['A column just listing an index for each row']:
        print("Oops! Are you sure that is the column that is just keeping track of the index for each row?")
    if desc_sol['The column with the most missing values'] != s.desc_sol['The column with the most missing values']:
        print("That doesn't look like the column with the most missing values.  You can have a column appear in the dictionary more than once.")
    if desc_sol['The maximum Satisfaction on the scales for the survey'] != s.desc_sol['The maximum Satisfaction on the scales for the survey']:
        print("Oops! That doesn't look quite right. Are you sure that is the max value associated with the Satisfaction scales for the survey?")
    if desc_sol['The variable with the highest spread of values'] != s.desc_sol['The variable with the highest spread of values']:
        print("That doesn't look like the column with the largest spread.  You can have a column appear in the dictionary more than once.")


#Question 2
def scatter_check(scatter_sol):
    '''
    INPUT scatter_sol - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if scatter_sol == s.scatter_sol:
        print("Nice job that looks right!")
    if scatter_sol['The column with the strongest correlation with Salary'] != s.scatter_sol['The column with the strongest correlation with Salary']:
        print("Oops! No, that is not the column with the strongest correlation with salary.")

    if scatter_sol['The data suggests more hours worked relates to higher salary'] != s.scatter_sol['The data suggests more hours worked relates to higher salary']:
        print("Oops! Actually, the more you work is actually correlated with lower salary values.")

    if scatter_sol['Data in the ______ column meant missing data in three other columns'] != s.scatter_sol['Data in the ______ column meant missing data in three other columns']:
        print("Oops! Actually, which column has two other columns with missing data when it is filled - your answer doesn't look like what I was expecting.")

    if scatter_sol['The strongest negative relationship had what correlation?'] != s.scatter_sol['The strongest negative relationship had what correlation?']:
        print("Oops! The strongest negative correlation is actually between HoursPerWeek and Salary.")


#Question 3
def lm_fit_check(lm_fit_sol):
    '''
    INPUT scatter_sol - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if lm_fit_sol == s.lm_fit_sol:
        print("Nice job that looks right!")
    else:
        print("Oops! Your solution should use only the first three statements here (a,b, and d).  Try again.")



# Question 1
def prop_sals_test(prop_sals):
    '''
    INPUT prop_sals - a float as the percent of missing values in the salary column

    Prints statement related to the correctness of the solution of the proportion
    '''
    if np.allclose(prop_sals, s.prop_sals):
        print("Nice job! That looks right!")
    else:
        print("Oops!  Make sure your value is for the proportion of nan values in only the Salary column.")


# Question 2
def sal_rm_test(sal_rm):
    '''
    INPUT sal_rm - a pandas dataframe with all rows that are missing a value the salary column removed.  The dataframe should only have the columns of num_vars (quant variables)

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if sal_rm.equals(s.sal_rm):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, this should be the num_vars dataframe with salary removed.")

# Question 3
def question3_check(question3_solution):
    '''
    INPUT question3_solution - the letter (a, b, or c) corresponding to the statement that best describes what happend when fitting your model.

    Prints statement related to the correctness of the letter chosen.
    '''
    if question3_solution == s.question3_solution:
        print("Nice job! That's right! Those missing values in the X matrix will still not allow us to predict the response.")
    else:
        print("Oops!  That wasn't what we were expecting.  Your solution should be either a, b, or c for the string that best relates to what happened.")


# Question 4
def all_rm_test(all_rm):
    '''
    INPUT all_rm - a pandas dataframe with all rows that are missing a value in any column removed from num_vars (only the numeric columns)

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if all_rm.equals(s.all_rm):
        print("Nice job! That looks right.  The default is to drop any row with a missing value in any column, so we didn't need to specify any arguments in this case.")
    else:
        print("Oops!  That doesn't look like what we were expecting.  Make sure you are working with only the numeric columns, and you have dropped any rows with missing values.")


# Question 5
def question5_check(question5_solution):
    '''
    INPUT question3_solution - the letter (a, b, or c) corresponding to the statement that best describes what happend when fitting your model.

    Prints statement related to the correctness of the letter chosen.
    '''
    if question5_solution == s.question5_solution:
        print("Nice job! That's right! Python isn't exactly magic, but sometimes it feels like it is!")
    else:
        print("Oops!  Your solution should have worked.  In which case, no output should have printed.  This solution should follow just as in the screencast.")


# Question 6
def r2_test_check(r2_test):
    '''
    INPUT r2_test - the rsquared value from fitting a model with all nan values dropped and only using quantitative variables.

    Prints statement related to the correctness rsquared matching solution.
    '''
    if r2_test == s.r2_test:
        print("Nice job! That's right! Your rsquared matches the solution.")
    else:
        print("Oops!  That wasn't the value that was expected.  You should fit your model using the training data, predict on the X_test data, and then score comparing the y_test and your predicted values.")

# Question 7
def question7_check(question7_solution):
    '''
    INPUT question7_solution - a dictionary with statements of takeaways from the rest of the notebook.  The values should be the variables a, b, c, d, e, f, or g

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if question7_solution == s.question7_solution:
        print("Nice job! That looks right to me!  We would really like to predict for anyone who provides a salary, but our model right now definitely has some limitations.")
    elif question7_solution['The number of reported salaries in the original dataset'] != s.question7_solution['The number of reported salaries in the original dataset']:
        print("The number of reported salaries in the original dataset doesn't look quite right.")
    elif question7_solution['The number of test salaries predicted using our model'] != s.question7_solution['The number of test salaries predicted using our model']:
        print("The number of salaries predicted using our model doesn't look quite right.")
    elif question7_solution['If an individual does not rate stackoverflow, but has a salary'] != s.question7_solution['If an individual does not rate stackoverflow, but has a salary']:
        print("Whether an individual rates stackoverflow or has a job satisfaction we would still like to predict the salary if we can.")
    elif question7_solution['If an individual does not have a a job satisfaction, but has a salary'] != s.question7_solution['If an individual does not have a a job satisfaction, but has a salary']:
        print("Whether an individual rates stackoverflow or has a job satisfaction we would still like to predict the salary if we can.")
    elif question7_solution['Our model predicts salaries for the two individuals described above.'] != s.question7_solution['Our model predicts salaries for the two individuals described above.']:
        print("Unfortunately, our current model will not predict for anyone who has missing values in any column - even if they do have a salary!")












