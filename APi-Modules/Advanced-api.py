import requests

# get data from the PokeAPI: (send request to the API and get the response from the owner of the API)
url="https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)

total_records = response.json().get('count') # get the total number of records in the API

print("Total records in the API:", total_records)


# fetch all the data from the API using pagination: (the API has a limit of 20 records per page, so we need to fetch all the data using pagination)
# limit = 20 # number of records per page


all_data = [] # create an empty list to store all the data

# used the offset parameter to fetch the data from the API in a paginated manner, and then we will append the data to the all_data list.
for offset in range(0, total_records, 20):
    pagination_url = f"{url}?offset={offset}&limit=20" # create the pagination url
    response = requests.get(pagination_url) # send request to the API and get the response from the owner of the API
    data = response.json() # get the data in json format
    all_data.extend(data.get('results', [])) # append the data to the all_data list


print("Total records fetched from the API:", len(all_data)) # print the total number of records fetched from the API

print("All data fetched from the API:", all_data) # print all the data fetched from the API
