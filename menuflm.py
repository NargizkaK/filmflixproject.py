import addflmData, amendflm, deleteflm, printflm, searchflm

def open_file(file_path): #file_path is the parameter or value
    try:
        with open(file_path) as read_file:
            # read() reads the file content and save it in the variable called rf
            of = read_file.read()
 
            return of
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
 
def films_menu():
    try:
        option = 0 
        optionsList = ["1","2","3","4","5","6"]
 
        menu_choices = open_file("Python/project.py/__pycache__/flmMenutxt")
 
        while option not in optionsList:
            print(menu_choices)
 
            option = input("Enter an option from the menu above (Example: 1 or 3 or 5,,): ")
 
          
            if option not in optionsList:
                print(f"{option} is not a valid choice")
        return option
    except FileNotFoundError as e:
        print(f"Add error: {e}")
        
 
 
mainProgram = True 
 
while mainProgram:
    main_menu = films_menu()
 
    if main_menu == "1":
        printflm.print_films()
    elif main_menu == "2":
        addflmData.add_film()
    elif main_menu == "3":
        amendflm.update_films()
    elif main_menu == "4":
        deleteflm.delete_films()
    elif main_menu == "5":
        searchflm.search_film()
 
    else: 
        mainProgram = False
input("Press Enter to exit....")
 
