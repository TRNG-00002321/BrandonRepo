#1. Create a dictionary of five countries and their capitals.
# Write a function that takes a country name as input and returns its capital.

countries = {"USA": "Washington, D.C.", "Japan": "Tokyo", "China": "Beijing", "Mexico": "Mexico City", "South Korea": "Seoul"}

def read_capitals(country_name):
    print(countries[country_name])


print("Selection: \nUSA\nJapan\nChina\nMexico\nSouth Korea")
country_name = str(input("Enter a country name: "))

read_capitals(country_name)
