# source: Engineer Man
# https://www.youtube.com/watch?v=StmNWzHbQJU

import pip._vendor.requests as requests

url = ""


while True:
    response = requests.post(url, data={}).text
    print(response)
