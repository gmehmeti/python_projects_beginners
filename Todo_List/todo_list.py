# Todo List

from typing import List

command = {
    "1": "View Tasks",
    "2": "Add a Task",
    "3": "Remove a Task",
    "4": "Exit",
}


def display_menu():
    print("Todo List Menu:")
    for key, value in command.items():
        print(f"{key}. {value}")
    print()


def get_choice():
    while True:
        cmd = input("Enter your choice: ")
        if cmd not in command.keys():
            print("Invalid choice!")
            continue
        return cmd


def display_tasks(tasks: List[str]):
    if len(tasks) == 0:
        print('Todo list is empty!')
        return

    for index, item in enumerate(tasks, start=1):
        print(f"{index}. {item}")


def add_task(tasks: List[str]):
    while True:
        new_task = input('Enter a new task: ').strip()
        if len(new_task) == 0:
            print("Invalid Task!")
            continue

        tasks.append(new_task)
        print('New task added successfuly!')
        break


def delete_task(tasks: List[str]):
    display_tasks(tasks)
    while True:
        try:
            index = int(input("Enter the task number: "))
            if index < 1 or index > len(tasks):
                raise ValueError()

            tasks.pop(index-1)
            print('Task deleted successfuly!')
            break
        except ValueError:
            print("Invalid task number!")


def main():
    todo_list = []
    while True:
        display_menu()
        user_choice = get_choice()
        # print('User Choice', user_choice)

        if user_choice == "1":
            display_tasks(todo_list)
        elif user_choice == "2":
            add_task(todo_list)
        elif user_choice == "3":
            delete_task(todo_list)
        else:
            break

        print()


if __name__ == "__main__":
    main()
