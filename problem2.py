"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9
    """
    return round((fahrenheit - 32) * 5/9, 2)

def temperature_converter():
    """
    Interactive temperature converter.
    - Ask for a numeric value
    - Ask for unit (C/F), case-insensitive
    - Convert and print rounded to 2 decimals
    - Handle invalid input gracefully
    """
    try:
        raw = input("Enter temperature value: ").strip()
        value = float(raw)
    except ValueError:
        print("Invalid number! Please enter a numeric value.")
        return

    unit = input("Current unit (C/F): ").strip().lower()
    if unit == "c":
        converted = celsius_to_fahrenheit(value)
        print(f"{value:.2f} °C = {converted:.2f} °F")
    elif unit == "f":
        converted = fahrenheit_to_celsius(value)
        print(f"{value:.2f} °F = {converted:.2f} °C")
    else:
        print("Invalid unit! Please enter 'C' or 'F'.")

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    # Run interactive converter
    temperature_converter()

# ci-touch
