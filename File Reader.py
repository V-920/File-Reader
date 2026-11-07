import os
while True:
    dire = input("Enter the directory path: ")
    files = input("Enter file name: ")

    try:
        os.chdir(dire)
        with open(files, 'r') as file:
            content = file.read()
            print(content)
        
    except FileNotFoundError as e:
        print("An error occurred:", e)
    except PermissionError as e:
        print("An error occurred:", e)