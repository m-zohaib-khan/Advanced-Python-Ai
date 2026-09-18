import requests

# get data from the PokeAPI: (send request to the API and get the response from the owner of the API)
response = requests.get("https://pokeapi.co/api/v2/pokemon")

if response.status_code == 200: # this is server response code, if it is 200 then it means the request was successful and the data was retrieved successfully
    data = response.json() # api get the data in json format
    print(data)

else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)
