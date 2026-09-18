import threading
from concurrent.futures import ThreadPoolExecutor

# transform the data from the src to destination;
def transformation(input):

    src=input["src"]
    dest=input["dest"]

    # simulate the transformation process
    print(f"Reading from {src}")
    print('Transforming data...')
    print(f"Writing data to {dest}")

    return f"Data transformation from {src} to {dest} completed."


# create the array of dictionaries to simulate the data transformation process;
array = [
        {
            "src": "table-1",
            "dest": "table-1"
        },
        {
            "src": "table-2",
            "dest": "table-2"
        },
        {
            "src": "table-3",
            "dest": "table-3"
        },
        {
            "src": "table-4",
            "dest": "table-4"
        },
        {
            "src": "table-5",
            "dest": "table-5"
        }
    ]


# trnasformation process using multithreading;
with ThreadPoolExecutor(max_workers=5) as executor:

    results = executor.map(transformation, array)


# print the returned values from the transformation process;
print(f"the returned values are: {list(results)}")
    