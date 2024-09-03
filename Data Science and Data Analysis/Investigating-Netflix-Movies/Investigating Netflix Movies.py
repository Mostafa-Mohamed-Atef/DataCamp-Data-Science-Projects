import pandas as pd
import matplotlib.pyplot as plt 

netflix_df = pd.read_csv("netflix_data.csv")

netflix_subset = netflix_df[netflix_df["type"]=="Movie"]

netflix_movies_df = netflix_subset.loc[:,["title","country","genre","release_year","duration"]]

netflix_movies = pd.DataFrame(netflix_movies_df)

short_movies = netflix_movies[netflix_movies.duration < 60]

colors = []
for lab,row in netflix_movies.iterrows():
    if row["genre"] == "Children":
        colors.append("Blue")
    elif row["genre"] == "Documentaries":
        colors.append("Green")
    elif row["genre"] == "Stand-Up":
        colors.append("Red")
    else:
        colors.append("Yellow")

fig = plt.figure()
plt.scatter(netflix_movies["release_year"],netflix_movies["duration"],c=colors)
plt.xlabel("Release year");plt.ylabel("Duration (min)");plt.title("Movie Duration by Year of Release")

plt.show()

answer = "no"
