import os

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("📝 Enter task description: ").strip()
    if task:
        tasks.append("[ ] " + task)
        print("✅ Task added.\n")

def mark_done(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                if tasks[num-1].startswith("[ ]"):
                    tasks[num-1] = tasks[num-1].replace("[ ]", "[✔]", 1)
                    print("👍 Task marked as done.\n")
                else:
                    print("⚠️ Task already marked done.\n")
            else:
                print("❌ Invalid task number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Removed: {removed}\n")
            else:
                print("❌ Invalid task number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

def main():
    print("📂 Welcome to Task Manager")
    filename = input("Enter task file name (e.g., tasks.txt): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    tasks = load_tasks(filename)

    while True:
        print("\n🗂️  MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save & Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(filename, tasks)
            print(f"💾 Tasks saved to {filename}. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
