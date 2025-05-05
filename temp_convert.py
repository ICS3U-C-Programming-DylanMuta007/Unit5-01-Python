#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : April 2025
# converts celsius to fahrenheit using functions


def fahrenheit():
    # The fahrenheit() functions converts from celsius to fahrenheit

    # Asks for the temperature in celsius
    celsius = input("Enter the temperature (°C): ")

    try:
        # Converts user input
        celsius_float = float(celsius)

        # Converts from celsius to fahrenheit
        fahrenheit_conversion = (9 / 5) * celsius_float + 32

        # Prints the conversion
        print(f"\n{celsius_float}°C is equal to {fahrenheit_conversion}°F. ")

    except ValueError:
        # Catches all invalid input
        print(f"{celsius} is not a valid input")


def main():
    # Calls function fahrenheit
    fahrenheit()


if __name__ == "__main__":
    main()
