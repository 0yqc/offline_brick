# WIP, does not work yet

import requests

key = input("your API key: ").strip()
user = input("username or email: ").strip()
password = input("password: ").strip()

result = requests.get("https://rebrickable.com/users/_token/?key=" + key + "&username=" + user + "&password=" + password)
# token = result.json()["user_token"]

print("Your user token: " + result.json())