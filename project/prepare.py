import pandas as pd


df.date = pd.to_datetime(df.date)
df = df.set_index(df.date)
pages = df['path'].resample('d').count()
df = df.drop(columns=['id','cohort_id','deleted_at','slack','created_at','updated_at','date'])

df=df[df.program_id!=4] #only five, who cares
df=df[df.name!='Staff'] #remove staff, questions are about students
df.program_id = df.program_id.map({1:'PHP', 2:'Java', 3:'Data'}) #map number to program
df.name = df.name + "-" + df.program_id #concatenate cohort and program

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
        
df['path'] = home #make path only the top subdirectory

