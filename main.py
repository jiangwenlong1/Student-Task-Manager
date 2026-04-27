tasks = []

def add_task():
    title = input("Enter task title: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline: ")
    priority = input("Enter priority: ")

    task = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['title']} | {task['subject']} | {task['status']}")

def complete_task():
    show_tasks()
    choice = int(input("Enter task number to mark complete: ")) - 1

    if 0 <= choice < len(tasks):
        tasks[choice]["status"] = "completed"
        print("Task marked as completed!")
    else:
        print("Invalid choice.")

def generate_report():
    with open("tasks_report.txt", "w") as f:
        for task in tasks:
            f.write(str(task) + "\n")

    with open("tasks.csv", "w") as f:
        f.write("Title,Subject,Deadline,Priority,Status\n")
        for t in tasks:
            f.write(f"{t['title']},{t['subject']},{t['deadline']},{t['priority']},{t['status']}\n")

    print("Report generated!")

def main():
    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main()
