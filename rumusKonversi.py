#  Konversi Celsius
# 1. Konversi Celsius ke Fahrenheit
def celcius_to_farenheit(celcius) :
    farenheit = (celcius * 1.8) + 32
    return farenheit
# 2. Konversi Celsius ke Reaamur
def  celcius_to_reaamur(celcius) : 
    reamur = (celcius * 0.8 )
    return reamur
# 3. Konversi Celsius ke Kelvin
def  celsius_to_kelvin(celcius) :
    kelvin = celcius + 273
    return kelvin

#  Konversi Farenheit
# 1. Konversi Fahrenheit ke Celcius
def farenheit_to_celsius(farenheit):
    celcius  = 0.5 * ( farenheit - 32) 
    return celcius
# 2. Konversi Fahrenheit ke Reamur
def farenheit_to_reaamur(farenheit) :
    reamur = 0.4 * ( farenheit - 32) 
    return reamur
# 3. Konversi Fahrenheit ke Kelvin
def  farenheit_to_kelvin(farenheit) :
    kelvin = 0.5 * ( farenheit - 32) + 273
    return kelvin

# Konversi Reamur
# 1. Konversi Reamur ke Celcius
def  reamur_to_celsius(reamur) :
    celcius = (1.25 * reamur)
    return celcius
# 2. Konversi Reamur ke Fahrenheit
def reamur_to_fahrenheit(reamur) :
    fahrenheit= ((9/5)* reamur) + 32
    return fahrenheit
# 3. Konversi Reamur ke Kelvin
def reamur_to_kelvin(reamur) :
    kelvin = 5/4 * reamur + 273
    return kelvin

# Konversi Kelvin
# 1. Konversi Kelvin ke Celcius
def kelvin_to_celsius(kelvin) :
    celsius = kelvin -  273
    return celsius
# 2. Konversi Kelvin ke Reamur
def kelvin_to_reamur(kelvin):
    reamur = 4/5 * (kelvin - 273)
    return reamur
# 3. Konversi Kelvin ke Farenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = 9/5 * (kelvin - 273) + 32
    return fahrenheit