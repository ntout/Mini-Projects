import math

def width():
    feet = float(input('Enter the width of your wall in feet: '))
    return feet


def height():
    feet = float(input('Enter the height of your wall in feet: '))
    return feet


def price():
    dollar = float(input('Enter the price (in dollars) per gallon: '))
    return dollar


def coats():
    coat = float(input('How many coats of paint you want to apply: '))
    return coat


def total_sqft():
    total = 0
    num_wall = int(input('Enter the number of walls you want to paint: '))
    while num_wall > 0:
        h = height()
        w = width()
        sqft = w * h
        total  = total + sqft
        num_wall = num_wall - 1
    return total

def gallons():
    sqft = total_sqft()
    gal = math.ceil(sqft / 400)
    return gal

def total_cost():
    cost = gallons() * price()
    return cost


print(total_cost())
