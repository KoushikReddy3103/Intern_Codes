import pandas as pd
import numpy as np
from collections import defaultdict
from make_dict import make_it_dict
from logic import logic_elements
df = pd.read_csv("C:/Users/ykoushikreddy/Downloads/source_file_xander.csv")
df1 = pd.read_csv("C:/Users/ykoushikreddy/Downloads/Indian-Name-12.csv",encoding='unicode_escape')
with open("C:/Users/ykoushikreddy/Downloads/Names.txt") as names_file:
    f = names_file.read()

name_series = pd.Series(f.split("\n"))
df2 = pd.read_csv("C:/Users/ykoushikreddy/Downloads/year_of_birth_counts.csv")
S1 = set(df1["Name"].unique())
S2 = set(name_series.unique())
S3 = set(df2["first_name"].unique())
temp = S1.union(S2)
S_final = S3.union(temp)
S_final.remove(np.nan)
S_final.remove("")
L1 = []
L2 = []
names = []
def extract_names(df):
    df["EMAIL"] = df["EMAIL"].apply(lambda x:str(x))
    df["Username"] = df["EMAIL"].apply(lambda x:x.split("%40")[0])
    for name in df["Username"].unique():
        if '_' in name:
            name = name.strip("0123456789")
            L1.append(name.split("_"))
        elif "." in name:
            name = name.strip("0123456789")
            L2.append(name.split("."))
        else:
            name = name.strip("0123456789")
            names.append(name)
extract_names(df)
D = defaultdict(set)
make_it_dict(S_final,D)
email_name = input("Enter the name:")
print("The split for name:{email_name} is".format(email_name=email_name),logic_elements(email_name,D))


