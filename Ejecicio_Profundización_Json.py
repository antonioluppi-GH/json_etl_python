import json

import requests

import matplotlib.pyplot as plt

url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

response = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50")

json_response = response.json()

json_response["results"]



def fetch():
    dataset = [[["price"], ["condition"]] for x in json_response["results"] if x["currency_id"] == "ARS"]
    print(dataset)
    return dataset


if __name__ == "__main__":

    fetch()
