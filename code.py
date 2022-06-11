user_choice = -1

tasks = []
tasks.append("Do training")
tasks.append("Tidy up")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    task_index = int(input("Enter task index: "))
    tasks.pop(task_index)
    print("Task deleted!")

def save_tasks():
    file = open("tasks.txt", "w")
    for task in task:
        file.write(task+"\n")
    file.close()



while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks()

    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Export text file")
    print("5. Exit")

    user_choice = int(input("Choose number: "))
    print()