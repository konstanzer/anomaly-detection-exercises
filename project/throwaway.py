#make series of high lesson count per cohort
max_counts = df2.groupby('name').max()['cohort_path_counts']
all_counts = df2.groupby('name').count()[['path', 'cohort_path_counts']]
max_lessons = []

#now find the lesson associated with those counts
for ix, v in max_counts.items():
    p=df2.path[((df2['name'] == ix) & (df2['cohort_path_counts'] == v))]
    max_lessons.append((ix, p.iloc[0], v))

lessons_top = pd.DataFrame(max_lessons, columns=['cohort','lesson','count'])
lessons_top[['cohort', 'program']] = lessons_top['cohort'].str.split('-', 1, expand=True)
lessons_top = lessons_top.sort_values(by='program').set_index('cohort')

lessons_top.to_csv("project/top_lessons.csv")
lessons_top