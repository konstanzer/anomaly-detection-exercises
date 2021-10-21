import env
import pandas as pd

if __name__ == "__main__":
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'
    query = """SELECT * FROM logs
               JOIN cohorts on cohorts.id = logs.cohort_id"""
    
    df = pd.read_sql(query, url)
    df.to_csv("curriculum_logs.csv")