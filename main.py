import mod


def run():
  poblacion_paises = mod.read('app/data.csv')
  country = input('Ingrese el pais: ').capitalize()
  data = mod.get_population_by_country(poblacion_paises, country)
  print(data)

  population_data = mod.years_data(data)
  labels, values = zip(*population_data)
  mod.bar(labels, values)
  #el asterisco (*) se utiliza para desempaquetar secuencias (como listas o tuplas) en argumentos de una función. Cuando se coloca delante de una lista o tupla en una llamada a una función, desempaqueta los elementos de la secuencia y los pasa como argumentos individuales a la función.

  #como solo se necesita una informacion crearemos el grafico de pie

  countries = list(map(lambda x: x['Country/Territory'], poblacion_paises)) #create a list and then use map function to operate all the countries
  percentages = [x['World Population Percentage'] for x in poblacion_paises] # add the percentages 
  mod.pie(countries, percentages)


if __name__ == '__main__':
  run()