import json

import requests

import matplotlib.pyplot as plt

from requests.api import get

url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

response = requests.get("https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50")

json_response = response.json()


def fetch():
    dataset = [{'price':x.get("price"), 'condition':x.get("condition")} for x in json_response["results"]
                 if x["currency_id"] == "ARS"]
    print(dataset)
    
    return dataset


def transform(dataset, min, max):
    list_min = [x for x in dataset if x["price"] < min]
    list_min_max = [x for x in dataset if x["price"] >= min and x["price"] <= max]
    list_max = [x for x in dataset if x["price"] > max]
    
    data = {'menor al precio mínimo':len(list_min),
             'en rango':len(list_min_max), 'mayor al precio máximo':len(list_max)}
    
    return data


def report(data):
    fig = plt.figure()
    fig.suptitle('Distribución de resultados según parámetros escogidos')
    
    ax = fig.add_subplot()
    explode = (0, 0.1, 0)
    ax.pie(data.values(), labels=data.keys(), explode=explode, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()
    




if __name__ == "__main__":
    
    print('Graficador de resultados de búsqueda')
    
    print('indique precio mínimo')
    min = int(input())
    print('indique precio máximo')
    max = int(input())
    

    dataset = fetch()

    data = transform(dataset, min, max)
    
    report(data)

    