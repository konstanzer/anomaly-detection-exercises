import pandas as pd
import regex as re
from acquire import acquire_logs


def prepare_logs():
    """
    Get all the student logs data.
    Make datetime index.
    Drop program ID 4
    Combine program and cohort name in new column.
    Delete IPs that look like Codeup admin.
    Drop extra columns not used in analysis.
    """
    df = acquire_logs()
    df['datetime'] =  pd.to_datetime(df.date +" "+ df.time)
    df = df.set_index(df.datetime)
    
    #only five, who cares
    df=df[df.program_id!=4]
    #map number to program
    df.program_id = df.program_id.map({1:'PHP', 2:'Java', 3:'Data'}) 
    #concatenate cohort and program
    df.name = df.name + "-" + df.program_id 
    
    #dataframe without codeup ips
    df = df[df.ip.str[:-3] != "97.105.19"]
    
    df = df.drop(columns=['id','cohort_id','deleted_at','slack','created_at',
                          'updated_at','time','datetime','program_id'])
    
    df = prepare_paths(df)
    
    return df


def prepare_paths(df):
    """
    The path column is noisy.
    I want it to represent the lesson accessed.
    I use the home directory as the lesson, excluding leading numbers.
    I then standardize some path names one-by-one.
    Make new column showing new path counts by cohort.
    """
    #make path only the top subdirectory
    paths = df.path.str.split("/") #split subdirectories
    home = []
    #to match 3-classifiation, e.g.
    r = re.compile(r'\d*-')
    #make list of top subdirectory
    for s in paths:
        try:
            s=s[0]
            #some lessons have numbers
            if r.match(s):
                home.append(s.split("-", maxsplit=1)[1])
            else:
                home.append(s)
        except:
            home.append(None)
            
    df['path'] = home
    
    #standardizing path names
    df.path[df.path==""]="empty"
    df.path[df.path == '3.0-mysql-overview'] = 'mysql'
    df.path[df.path == '1._Fundamentals'] = 'fundamentals'
    df.path[df.path == 'capstone'] = 'capstones'
    df.path[df.path == 'javascript'] = 'javascript-i'
    df.path[df.path == 'working-with-time-series-data'] = 'timeseries'
    
    #make column showing count of that path for that cohort
    df['cohort_path_counts'] = df.groupby(['path','name'])['path'].transform('count')
    
    return df


if __name__ == "__main__":
    
    df = prepare_logs()
    df.to_csv("prepared.csv")



