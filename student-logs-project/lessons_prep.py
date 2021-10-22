import pandas as pd
import numpy as np


def lessons_prep(df):
    """
    Getting the dataframe in shape for lessons exploration.
    """
    #delete paths that aren't lessons, IMO
    subs = ['index.html', 'search', 'AI-ML-DL-timeline.jpg', 'single-page.html',
            'users', 'login', 'uploads', 'modern-data-scientist.jpg',
            'florence-python-assessment.html', 'vocabulary.md', 'content']
    
    #this is the loop I use to drop em
    for s in subs:
        df = df[df.path != s]
        
    #remove staff, questions are about students
    df = df[df.name!='Staff-Java'] 
    #now drop rows if path isn't 3+ characters
    df = df[df.path.str.len()>3]
    
    return df


def lessons_pivot(df):
    """
    Dataframe with all lessons by cohort
    """
    df = lessons_prep(df)
    
    df['path-cohort'] = df['path'] + ";" + df['name']
    df = df.groupby('path-cohort').count().sort_values(by='cohort_path_counts', ascending=False)
    
    #require 10 plus calls to be included
    df = df.cohort_path_counts[df.cohort_path_counts > 9]
    df = pd.DataFrame(df)
    
    df[['lesson', 'cohort']] = list(df.index.str.split(';', 1, expand=True))
    df = df.reset_index(drop=True)
    pivot = df.pivot(index='lesson', columns='cohort', values='cohort_path_counts').fillna(0)
    
    return pivot


def divide_lessons_by_program(pivot):
    """
    Divide lessons into individual program dataframes for exploration.
    """
    java, data, php = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    #divide columns by program
    for col in pivot.columns:
        p = col[-4:]
        if p == 'Java':
            java[col[:-5]] = pivot[col]
        elif p == 'Data':
            data[col[:-5]] = pivot[col]
        else:
            php[col[:-4]] = pivot[col]

    #drop unused rows
    java = java.loc[(java!=0).any(axis=1)].astype(int)
    data = data.loc[(data!=0).any(axis=1)].astype(int)
    php = php.loc[(php!=0).any(axis=1)].astype(int)

    #convert values to column-wise percentages
    rel_java = round(java/java.sum(),4)
    rel_data = round(data/data.sum(),4)
    rel_php = round(php/php.sum(),4)
    
    return rel_java, rel_data, rel_php


def most_accessed(df1, df2, df3):
    """
    Print most accessed lessons
    """
    for frame in [df1, df2, df3]:
        print("-------")
        for ix, col in enumerate(frame.columns):
            top=frame[col][frame[col]==frame.max()[ix]]
            print(col, top.values[0], top.index[0])
            
            
def mean_access_rate(df1, df2, df3):
    """
    Print mean percentage of call to each lesson per program.
    """
    for frame in [df1, df2, df3]:
        print("-------")
        print(np.mean(frame, axis=1).sort_values(ascending=False))
        
        
def outlier_activity(df1, df2, df3, stdev):
    """
    Print lessons where cohort is a program outlier in lesson access.
    """
    for frame in [df1, df2, df3]:
        print("-------")
        for x in range(0, len(frame.index)):
            row = frame.iloc[x] > frame.iloc[x].mean() + stdev*frame.iloc[x].std()
            if sum(row)>0:
                print(list(row.index[row>0]), row.name)