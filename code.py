user_choice = -1

tasks = []
tasks.append("Do training")
tasks.append("Tidy up")

while user_choice != 5:
    if user_choice == 1:
        print(tasks)

    if user_choice == 2:
        task = input("Enter task: ")
        tasks.append(task)

    #if user_choice == 3:
        

    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Export text file")
    print("5. Exit")

    user_choice = int(input("Choose number: "))