# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Main converter function
def temperature_converter():
    try:
        # Ask user for conversion direction
        choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()

        # Get the temperature value
        temp = float(input("Enter the temperature: "))

        # Perform conversion based on user choice
        if choice == 'C':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        elif choice == 'F':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
        else:
            print("Invalid choice! Please enter 'C' or 'F'.")
    except ValueError:
        # Handle non-numeric temperature input
        print("Please enter a valid number for the temperature.")

# Run the converter
temperature_converter()
