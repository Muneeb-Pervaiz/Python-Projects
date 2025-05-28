print("Select any one option to perform on tha file: ")
print("1) Create")
print("2) Read")
print("3) Modify")

choice = input("Enter your choice: ")
filename = input("Enter the file name (with .txt): ")

if choice == "1":
    try:
        with open(filename, "x") as file:
            print(filename, "File created successfully")
    except FileExistsError:
        print("File already exist.")


elif choice == "2":
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n--- Content ---")
            print(content)
    except FileNotFoundError:
        print("File not found")

elif choice == "3":
    newline = input("Write new lines to modify: ")
    try:
        # content = input("Enter your content: ")
        with open(filename, "a") as file:
            file.write("\n" + newline)
        print("File Modified Successfully")
    except FileNotFoundError:
        print("File Not Found")

else:
    print("Invalid Choice. Please Enter 1, 2 or 3.")

input("Press enter to exit...")

            
