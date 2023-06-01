# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 07:59:06 2023

@author: hp
"""


#importing required libraries
import pandas as pd
import os

#changing the directory
os.chdir("E:\OnineSales.ai")

#reading csv files as a dataframe
dept = pd.read_csv("data/Departments.csv")
employee = pd.read_csv("data/Employees.csv")
salary = pd.read_csv("data/Salaries.csv")


#merg dept and employee dataframe on id
df = pd.merge(dept, employee, left_on='ID', right_on=('DEPT_ID'))

# merge df and salary dataframe
dataframe = pd.merge(df, salary, left_on=('ID_y'), right_on=('EMP_ID'))


#calculating average salaries of a department 
data = dataframe.groupby(['NAME_x'])['AMT_(USD)'].mean()

#sorting the data in desccending order
#printing3 highest salaries of the department
#storing the final ans in ans df
ans = data.sort_values(ascending=False).head(3)
