t = []

while True:
    print("\n 1. Add task")
    print("\n 2. View task")
    print("\n 3. exit.")
    
    choice = input("enter ypur choice : ")
    
    if choice == "1":
        task = input("enter your task : ")
        print("your task added.")
        t.append(task)
        
    elif choice == "2" :
        print("\n TO DO LIST :")
        if len(t) == 0:
            print("no task available.")
        else:
            for i in range(len(t)):
                print(f"{i + 1} . {t[i]}")
                
    elif choice == "3":
        print("Goodbye ! ")
        break 
    
    else:
        print("Invalid choice. please try again")