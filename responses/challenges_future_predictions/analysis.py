import pandas as pd
import numpy as np


data = pd.read_csv("challenges_future_predictions.csv",delimiter=";")
data = data.rename(columns={data.columns[0]: "challenges", data.columns[1]: "predictions"})


challenges = ["Incorrect forward kinematics.",
            "Difficulty importing the URDF into simulation tool.",
            "Difficulty creating a URDF file.",
            "Difficulty adding end effector model to robotic arm model.",
            "Could not find a URDF with the specific version of the robot I want to simulate.",
            "Limitation in URDF did not allow creating model of robot with parallel linkages.",
            "Other"]

predictions = ["Yes","Don't know","No"]


df_challenges_predictions = pd.DataFrame(columns=predictions,index=challenges)
df_challenges_predictions.challenges = challenges
df_challenges_predictions = df_challenges_predictions.fillna(0)


for index, row in data.iterrows():
    challenges_col = row["challenges"]
    predictions_col = row["predictions"]
    if pd.isnull(challenges_col) or pd.isnull(predictions_col):
        continue

    challenges_in_row = challenges_col.split(",")
    
    for challenge in challenges_in_row:
            df_challenges_predictions.at[challenge,predictions_col] = df_challenges_predictions.at[challenge,predictions_col] + 1


df_challenges_predictions = df_challenges_predictions.round(0).astype(int)

df_challenges_predictions.to_csv("df_challenges_predictions.csv")