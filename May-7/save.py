def save_input_to_file(file_name):
    user_input = input("Enter your text: ")
    with open(file_name, 'w') as file:
        file.write(user_input)
    print("Text saved to file.")

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            print("Text from file:")
            print(text)
    except FileNotFoundError:
        print("File not found.")

def main():
    file_name = "write.txt"
    while True:
        print("\n1. Save input to file")
        print("2. Read from file")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            save_input_to_file(file_name)
        elif choice == "2":
            read_from_file(file_name)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
