import pandas as pd
import datetime
import openpyxl
import numpy as np
import xlrd
import os.path

def excel_file_make():
    global excel_file #Make the excel file as global variable so as to use it later.
    path = 'C:\\Users\\BB\\Desktop\\DailyGoal\\DailyGoalFile.xlsx' #Path of the excel file I want.
    excel_file = 'C:\\Users\\BB\\Desktop\\DailyGoal\\DailyGoalFile.xlsx'
    if os.path.isfile(path): #Checking if the excel file exists, if it does not then creating one.
        print('Excel file already exists.')
        return excel_file
    else:
        print('Excel file does not exist. Creating one.')
        today_date = datetime.datetime.now().date() #Excel file created with index as date from today.
        date_index = pd.date_range(today_date - datetime.timedelta(0), periods=30, freq='D') #Change periods for more rows(date).
        columns = ['Goal for the day?', 'How many?', 'Total Completed?', 'Reason for not completing?'] #Coloumn names.
        df = pd.DataFrame(index=date_index, columns=columns) #Creating the DataFrame.
        df.index.names = ['Date']
        df = df.fillna(0) #Filling all the values with zero in case I forget to input data of one day then it'll be displayed as zero.
        df = df.to_excel('C:\\Users\\BB\\Desktop\\DailyGoal\\DailyGoalFile.xlsx')
        if os.path.isfile(path):
            print('Excel file has been created.')
            return excel_file


excel_file_make()


df = pd.read_excel(excel_file, header=0, index_col='Date') #Read the excel file.
df = df.applymap(str) #Convert DF into str.
def take_input():
    goal_date = str(input('Enter the date in YYYY-MM-DD format: ')) #Goal for which date you want to set.
    if goal_date in df.index:
        row_index = df.loc[goal_date]
        print(row_index)
        number_of_goals = str(input('Enter the number of goals: ')) #Number of goals you want to set.
        df.loc[goal_date, 'How many?'] = number_of_goals
        if number_of_goals == 0:
            return
        else:
            goals_for_day = ''
            for i in range(int(number_of_goals)):
                print(f'Goal {i+1} -')
                goals_for_day += input() + '\n'

            df.loc[goal_date, 'Goal for the day?'] = goals_for_day

    else:
        print('There seems to be an issue with the date you entered.') #If date is outside the range.


take_input()


def check_completion():
    ask = str(input("Did you complete your goals? Type Yes/No. ")) #Check completion.
    if ask == "No":
        goal_date = str(input('Enter the date in YYYY-MM-DD format: '))
        if goal_date in df.index:
            total_completed = str(input(f'Enter the number of goals you completed on {goal_date}: '))
            df.loc[goal_date, 'Total Completed?'] = total_completed
            number_of_goals = df.loc[goal_date, 'How many?']
            if number_of_goals <= total_completed: #Checks if you input false or not.
                return
            else:
                reason_incomplete = str(input("Why didn't you complete? "))
                df.loc[goal_date, 'Reason for not completing?'] = reason_incomplete #Enter the reason.
    else:

        return

check_completion()

#print(df.head())

df = df.to_excel('C:\\Users\\BB\\Desktop\\DailyGoal\\DailyGoalFile.xlsx') #Saves the output for next use.





