"""
1. Convert Celsius to Fahrenheit: Given a list of temperatures in Celsius,
use map() to convert them to Fahrenheit. The formula is F = (C * 9/5) + 32.
Example
    celsius_temps = [0, 10, 20, 30]
    # Expected output: [32.0, 50.0, 68.0, 86.0]
"""

celsius_temps = [0, 10, 20, 30]

def celcius_conversion(num):
    return (num * 9/5) + 32

celsius_map_obj = map(celcius_conversion, celsius_temps)
converted_temp = list(celsius_map_obj)
print(converted_temp)