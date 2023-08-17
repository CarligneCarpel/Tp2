
todo_list = []
def add_task(deskripayon):
    todo_list.append(deskripsyon)
    print("Tach :", deskripsyon)


def display_tasks():
    print("Lis tach yo :")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

def mark_task_done(index):
    try:
        task = todo_list.pop(index - 1)
        print("Tach fini :", task)
    except IndexError:
        print("endis valide. tach la pa egzite.")

def save_tasks(filename):
    try:
        with open(filename, "w") as file:
            for task in todo_list:
                file.write(task + "\n")
        print("Tach anrejistre nan", filename)
    except Exception as e:
        print("Erè :", str(e))

def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            todo_list.clear()
            for line in lines:
                todo_list.append(line.strip())
        print("Tach chaje", filename)
    except FileNotFoundError:
        print("fichye a pa egziste.")
    except Exception as e:
        print("Erè :", str(e))


while True:
    print("\nMenu :")
    print("1. Ajout yon tach")
    print("2. Affiche tach yo")
    print("3. Make tach yo lè yo fini")
    print("4. Enrejistre tach yo")
    print("Program femen.")
    
    choice = input("Chwazi yon opsyon : ")
    
    if choice == "1":
        task_description = input("antre deskripsyon tach la : ")
        add_task(task_description)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        display_tasks()
        task_index = int(input("antre nimero tach ki fini an "))
        mark_task_done(task_index)
    elif choice == "4":
        save_tasks("tasks.txt")
    elif choice == "5":
        save_tasks("tasks.txt")
        print("Program femen.")
        break
    else:
        print("chwazi ankò.")

