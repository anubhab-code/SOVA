import pandas as pd
import datetime

col_li = ['Date', 'Work']

def create_todo():
    global col_li
    df = pd.DataFrame(columns=col_li)
    df.to_csv('todo.csv')
    
def insert_into_todo(stri):
    df = pd.read_csv('todo.csv', index_col=0)
    curr_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    df = df.append({'Date' : curr_date , 'Work' : stri} , ignore_index=True)
    df.drop(df.columns[df.columns.str.contains('Unnamed',case = False)],axis = 1)
    df.to_csv('todo.csv')

def delete_todo(ind):
    df = pd.read_csv('todo.csv', index_col=0)
    li = []
    li.append(ind)
    df.drop(li, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv('todo.csv', index=True)

# to be executed only once, or can result in data loss
#create_todo()
