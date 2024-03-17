#definiremos dos funciones
from collections.abc import Iterable, ValuesView
import csv
from matplotlib.figure import figaspect
import matplotlib.pyplot as plt


def get_population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,
                       data))

  return result


def read(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    population = []

    for row in reader:
      itearable = zip(header, row)
      country_dict = {key: value for (key, value) in itearable}
      population.append(country_dict)

  return population


def years_data(data):
  population_data = {}
  for entry in data:
      for key, value in entry.items():
          if 'Population' in key:
              population_data[key] = value
  return list(population_data.items())

      
def world_porcentage(data):
  world_data = {}
  for entry in data:
    for key, value in entry.items():
      if 'world' in key:
          world_data[key] = value
  return list(world_data.items())

  

def bar(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()


def pie(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()