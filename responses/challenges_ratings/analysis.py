import pandas as pd
import numpy as np


data = pd.read_csv("challenges_ratings.csv",delimiter=";")
data = data.rename(columns={data.columns[0]: "challenges", data.columns[1]: "ratings"})


challenges = ["Incorrect forward kinematics.",
            "Difficulty importing the URDF into simulation tool.",
            "Difficulty creating a URDF file.",
            "Difficulty adding end effector model to robotic arm model.",
            "Could not find a URDF with the specific version of the robot I want to simulate.",
            "Limitation in URDF did not allow creating model of robot with parallel linkages.",
            "Other"]

ratings = ["Easy","Medium","Difficult"]


df_challenges_ratings = pd.DataFrame(columns=ratings,index=challenges)
df_challenges_ratings.challenges = challenges
df_challenges_ratings = df_challenges_ratings.fillna(0)


for index, row in data.iterrows():
    challenges_col = row["challenges"]
    ratings_col = row["ratings"]
    if pd.isnull(challenges_col) or pd.isnull(ratings_col):
        continue

    challenges_in_row = challenges_col.split(",")
    
    for challenge in challenges_in_row:
            df_challenges_ratings.at[challenge,ratings_col] = df_challenges_ratings.at[challenge,ratings_col] + 1


df_challenges_ratings = df_challenges_ratings.round(0).astype(int)

df_challenges_ratings.to_csv("df_challenges_ratings.csv")