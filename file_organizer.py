# colorama is text color python library Fore() is color changer, init() to initalize the properties of the colorama
from colorama import init, Fore
from time import sleep
import os
import shutil

def display_banner() -> None :
    init(autoreset=True)
    print(Fore.BLUE + """
  ___ _ _        ___                     _             
 | __(_) |___   / _ \\ _ _ __ _ __ _ _ _ (_)______ _ _ 
 | _|| | / -_) | (_) | '_/ _` / _` | ' \\| |_ / -_) '_|
 |_| |_|_\\___|  \\___/|_| \\__, \\__,_|_||_|_/__\\___|_|  
                         |___/                         
""")
    
def organize_files(folder_path : str) -> None :
    files = os.listdir(folder_path)
    for file in files :
        file_name, extension = os.path.splitext(file)
        extension = extension[1:]
        
        if os.path.exists(folder_path + "/" + extension) :
            shutil.move(folder_path + "/" + file, folder_path + "/" + extension + "/" + file)
        else :
            os.makedirs(folder_path + "/" + extension)
            shutil.move(folder_path + "/" + file, folder_path + "/" + extension + "/" + file)

def start_app() -> None :
    start = str(input("Start Application(y/n) : "))
    if start != "y" :
        print("Terminated...")
        return
    display_banner()
    folder_path = str(input("Enter the folder directory to organize : "))
    organize_files(folder_path)
    print("Organizing", end="")
    for _ in range(3) :
        print(".", end="", flush="")
        sleep(1)
    print("\nCompleted")
        

if __name__ == "__main__" :
    # start the application
    start_app()