from glob import glob
import pandas as pd

"""
Finds optinos where:

"""

DESIRED_DOWNSIDE_PROTECTION = 0.10
DESIRED_UNCHANGED_PI_PERCENT = 0.10

# go through every csv and find where both conditions met

dfs = []
for path in glob("data/option_chains/**/*.csv"):
    try:
        df = pd.read_csv(path)
        rows = df[(df["percent_protection"] >= DESIRED_DOWNSIDE_PROTECTION) &\
                (df["pi_if_unchanged_percent"] >= DESIRED_UNCHANGED_PI_PERCENT)]
        dfs.append(rows)
    except:
        pass

master_df = pd.concat(dfs, ignore_index=True)
master_df.to_csv("data/best_options.csv", index=False)