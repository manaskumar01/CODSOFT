import os

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "todo_list.txt"
        self.load_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")
        self.save_tasks()

    def remove_task(self, task_number):
        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from the to-do list.")
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file]

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_number = input("Enter the task number to remove: ")
            todo_list.remove_task(task_number)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()