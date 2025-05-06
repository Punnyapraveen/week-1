# Predefined credentials (in real apps, use a database)
stored_username = "user"
stored_password = "pass123"

# Function to handle login
def login_system():
    try:
        # Get user input
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if input is empty
        if not username or not password:
            print("Username or password cannot be empty.")
            return

        # Validate credentials
        if username == stored_username and password == stored_password:
            print("Login successful!")
        else:
            print("Invalid username or password.")

    except Exception as e:
        # Catch unexpected errors
        print("An error occurred:", e)

# Run the login system
login_system()
