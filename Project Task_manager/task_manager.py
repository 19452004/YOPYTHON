import sys
import json
import os
import uuid
from datetime import datetime


if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    # Constants
    TASKS_FILE = "tasks.json"

    # Inisialisasi file task
    def init_tasks_file():
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "w") as file:
                json.dump([], file)

    # Load tasks from JSON file
    def load_tasks():
        with open(TASKS_FILE, "r") as file:
            return json.load(file)

    # Save tasks to JSON file
    def save_tasks(tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

    # Add a new task
    def add_task():
        description = input("Masukan Deskripsi Task: ")
        tasks = load_tasks()
        new_task = {
            "id": str(uuid.uuid4()),
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added: {new_task['description']}")

    # Update a task
    def update_task():
        task_id = input("Enter task ID to update: ")
        description = input("Enter new task description: ")
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = description
                task["updatedAt"] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task updated: {task['description']}")
                return
        print("Task not found.")

    # Delete a task
    def delete_task():
        task_id = input("Enter task ID to delete: ")
        tasks = load_tasks()
        tasks = [task for task in tasks if task["id"] != task_id]
        save_tasks(tasks)
        print("Task deleted.")

    # Change task status
    def change_status():
        task_id = input("Enter task ID to change status: ")
        status = input("Enter new status (todo, in-progress, done): ")
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = status
                task["updatedAt"] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task status updated to '{status}'.")
                return
        print("Task not found.")

    # List tasks by status
    def list_tasks():
        status = input("Masukkan status untuk difilter (todo, in-progress, done) atau biarkan kosong untuk menampilkan semua: ").strip()
        tasks = load_tasks()
        if status:
            tasks = [task for task in tasks if task["status"] == status]
        for task in tasks:
            print(f"[{task['status']}] {task['id']} - {task['description']} (Created: {task['createdAt']})")

    # Main menu
    def main_menu():
        init_tasks_file()
        while True:
            print("\nTask Manager")
            print("1. Tambah Task")
            print("2. Update Task")
            print("3. Hapus Task")
            print("4. Ubah Task Status")
            print("5. Liat Tasks")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                add_task()
            elif choice == "2":
                update_task()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                change_status()
            elif choice == "5":
                list_tasks()
            elif choice == "6":
                print("Keluar dari Task Manager. TERIMA KASIH!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()