# import pandas as pd
# from nba_api.stats.static import teams

# nba_teams = teams.get_teams()

# print("Type:", type(nba_teams))
# print("Number of teams:", len(nba_teams))
# print("First team:", nba_teams[0])

# print("\nFirst 3 teams:")
# print(nba_teams[0:3])


# def one_dict(list_dict):
#     keys = list_dict[0].keys()
#     out_dict = {key: [] for key in keys}

#     for dictionary in list_dict:
#         for key, value in dictionary.items():
#             out_dict[key].append(value)

#     return out_dict


# dict_nba_team = one_dict(nba_teams)
# df_teams = pd.DataFrame(dict_nba_team)

# print("\nFirst 5 teams as a table:")
# print(df_teams.head())

# df_warriors = df_teams[df_teams["nickname"] == "Warriors"]

# print("\nWarriors row:")
# print(df_warriors)

# id_warriors = df_warriors[["id"]].values[0][0]

# print("\nWarriors ID:", id_warriors)

import requests
import os
from PIL import Image
from IPython.display import IFrame


url = "https://www.ibm.com/"
r = requests.get(url)

print(r.status_code)

if r.status_code == 200:
    print("Request worked")
else:
    print("Request failed")

print(r.request.headers)
print("Request body:", r.request.body)

print(r.headers)

header = r.headers

print(header["Content-Type"])
print(r.encoding)

print(r.text[:100])


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png"

r = requests.get(url)

print(r.status_code)
print(r.headers["Content-Type"])

path = "IDSNlogo.png"

with open(path, "wb") as file:
    file.write(r.content)

print("Image saved")



url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"

path = os.path.join(os.getcwd(), "example_download.txt")

r = requests.get(url)

with open(path, "wb") as file:
    file.write(r.content)

print("Text file downloaded")


url_get = "https://httpbin.org/get"

payload = {
    "name": "Joseph",
    "ID": "123"
}

r = requests.get(url_get, params=payload)


print(r.status_code)
print(r.headers["Content-Type"])
data = r.json()
print(data)


url_post = "https://httpbin.org/post"

payload = {
    "name": "Joseph",
    "ID": "123"
}

r_post = requests.post(url_post, data=payload)

print(r_post.url)