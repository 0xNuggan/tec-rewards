import pandas as pd
import numpy as np
import os
import subprocess
import json
import shutil
from pathlib import Path


giant_table = pd.DataFrame()

# run all notebooks in the relevant distribution folder
for folder in os.listdir("./combine_folder/noSourcecred/"):
    path_to_dist = "./combine_folder/noSourcecred/" + folder + "/results/distribution/final_praise_token_allocation.csv"
    print(path_to_dist)
    round_alloc= pd.read_csv(path_to_dist)
    print(round_alloc.head)
    round_alloc = round_alloc[["USER IDENTITY", "TOTAL TO RECEIVE"]]
    round_alloc.rename(columns={"TOTAL TO RECEIVE": str(folder)}, inplace=True)

    if giant_table.empty:
        giant_table= round_alloc.copy()
    else: 
        giant_table =giant_table.merge(round_alloc, how="outer", on="USER IDENTITY")
        #giant_table = giant_table.join(round_alloc.set_index('USER IDENTITY'), on='USER IDENTITY')
    
giant_table.to_csv('test2.csv')

