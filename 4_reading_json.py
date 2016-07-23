# coding: utf-8

import json
# for building a world map
import pygal

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country. vfor pop_dict in pop_data:
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # Some values are base 10, and cant be converted to int directly
        # so we pass it to float first
        population = int(float(pop_dict['Value']))
        # The float() function turns the string into a decimal, and the int()
        # function drops the decimal part of the number and returns an integer.
        print(country_name + ": " + str(population))

# Lets build a world map
wm = pygal.maps.world.World()

wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')

# next task... connect that json to the svg file.
