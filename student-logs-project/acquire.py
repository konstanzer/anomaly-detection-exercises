import env
import pandas as pd


def acquire_logs():
    #Query SQL database and return student logs
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'
    query = """SELECT * FROM logs
               JOIN cohorts on cohorts.id = logs.cohort_id"""
    df = pd.read_sql(query, url)
    
    return df
    

if __name__ == "__main__":
    
    df = acquire_logs()
    df.to_csv("curriculum_logs.csv")