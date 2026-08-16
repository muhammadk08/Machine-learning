import requests
import pandas as pd
from randomuser import RandomUser

# Generate random users
users = RandomUser.generateusers(10)

user_rows = []

for user in users:
    user_rows.append({
        "Name": user.getfullname(),
        "Gender": user.getgender(),
        "City": user.getcity(),
        "State": user.getstate(),
        "Email": user.getemail(),
        "DOB": user.getdob(),
        "Picture": user.getpicture()
    })

df_users = pd.DataFrame(user_rows)

print("Random users:")
print(df_users.head())


# Retrieve fruit data
fruit_url = "https://fruityvice.com/api/fruit/all"

fruit_response = requests.get(fruit_url)
fruit_response.raise_for_status()

fruit_data = fruit_response.json()
df_fruits = pd.json_normalize(fruit_data)

print("\nFruit data:")
print(df_fruits.head())


# Find Cherry information
cherry = df_fruits[
    df_fruits["name"].str.lower() == "cherry"
]

if not cherry.empty:
    print("\nCherry family:", cherry["family"].iloc[0])
    print("Cherry genus:", cherry["genus"].iloc[0])


# Find Banana calories
banana = df_fruits[
    df_fruits["name"].str.lower() == "banana"
]

if not banana.empty:
    print(
        "Banana calories:",
        banana["nutritions.calories"].iloc[0]
    )


# Retrieve jokes
joke_url = "https://official-joke-api.appspot.com/jokes/ten"

joke_response = requests.get(joke_url)
joke_response.raise_for_status()

joke_data = joke_response.json()

df_jokes = pd.DataFrame(joke_data)

df_jokes = df_jokes.drop(
    columns=["type", "id"]
)

print("\nJokes:")
print(df_jokes)