from time import sleep

# to manage todos we are using the dict data type like title - desc pair
todos = {}

def create_todo(todo : str, description : str) :
    
    todos[todo] = description
    print("Todo successfully saved")
    
def update_todo(todo : str, updated_desc : str) :
    if todo in todos :
        todos[todo] = updated_desc
        print("Todo updated successfully")
    else :
        print("Todo is not found")

def delete_todo(todo : str) :
    if todo in todos :
        todos.pop(todo)
        print("Deleted successfully")
    else :
        print("Todo is not found")
        
def delete_all_todos() -> None :
    
    todos.clear()
    print("All todos are cleared")
        
def save_todos() -> None :
    
    if not todos :
        print("Empty Todo list")
        return
    try :
        file_name = "todos.txt"
        with open(file_name, 'w') as file :
            for title, desc in todos.items() :
                file.write(f"title : {title}, description : {desc}\n")
        print("File saved successfully")
    except FileNotFoundError :
        pass
    
def display_todos() -> None :
    
    if not todos :
        print("Todo List is empty.")
        return
    
    for title, desc in todos.items() :
        print(f"title : {title}, description : {desc}")
        
def display_CLI() -> None :
        print("\n+----------------------------------+")
        print("|         TODO CLI MENU           |")
        print("+----------------------------------+")
        print("| 1. Create a new TODO            |")
        print("| 2. Update an existing TODO      |")
        print("| 3. Delete a TODO                |")
        print("| 4. Delete all TODOs             |")
        print("| 5. Display all TODOs            |")
        print("| 6. Save TODOs                   |")
        print("| 7. Exit                         |")
        print("+----------------------------------+")
        
def options_logic() -> None :
    
    # get the options from the user
    try :
        while True :
            display_CLI()
            option = int(input("Enter your choice (1-7): "))
            if option == 1 :
                title = str(input("Enter the title : "))
                desc = str(input("Enter the description : "))
                create_todo(title, desc)
            elif option == 2 :
                title = str(input("Enter the title to update : "))
                desc = str(input("Enter the description : "))
                update_todo(title, desc)
            elif option == 3 :
                del_todo = str(input("Enter the todo to delete : "))
                delete_todo(del_todo)
            elif option == 4 :
                delete_all_todos()
            elif option == 5 :
                display_todos()
            elif option == 6 :
                save_todos()
            elif option == 7 :
                print("Exiting", end="")
                for _ in range(3):
                    print(".", end="", flush=True)
                    sleep(1)
                break
            else :
                print("Invalid Input. Try again")
                
    except ValueError :
        print("Invalid Format.")

# to abstract the behind process
def start_app() -> None :
    options_logic()
    
if __name__ == "__main__" :
    
    # start the CLI application
    start_app()