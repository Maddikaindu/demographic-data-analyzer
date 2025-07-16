import requests
url = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/master/adult.data.csv"
response = requests.get(url)
if response.status_code == 200:
    with open("adult.data.csv", "w", encoding="utf-8") as file:
         file.write(response.text)
    print(" Dataset downloaded successfully as 'adult.data.csv'")
else:
  print(f"Failed to download: Status Code {response.status_code}")