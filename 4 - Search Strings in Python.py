import os

search = input("Enter your directory: ")
word = input("Enter word for search: ")

for root, dirs, files in os.walk(search):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, start=1):
                        if word in line:
                            # found = True
                            print("File Path", file_path)
                            print("File Name", file)
                            print("Word in", line_num )
                            print("Line num", line.strip())
                            

            except Exception as m:
                print("Error", file_path)


