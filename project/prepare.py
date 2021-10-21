import pandas as pd
import regex as re

if __name__ == "__main__":
    
    df = pd.read_csv("curriculum_logs.csv")
    
    df['datetime'] =  pd.to_datetime(df.date +" "+ df.time)
    df = df.set_index(df.datetime)

    df=df[df.program_id!=4] #only five, who cares
    df.program_id = df.program_id.map({1:'PHP', 2:'Java', 3:'Data'}) #map number to program
    df.name = df.name + "-" + df.program_id #concatenate cohort and program
    
    df = df.drop(columns=['id','cohort_id','deleted_at','slack','created_at',
                          'updated_at','date','time','datetime','program_id'])

    
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

    #dataframe without codeup ips
    df = df[df.ip.str[:-3] != "97.105.19"]

    #make column showing count of that path for that cohort
    df['cohort_path_counts'] = df.groupby(['path','name'])['path'].transform('count')
    
    df.to_csv("project/prepared.csv")



