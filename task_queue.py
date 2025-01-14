import heapq
import json
import os
# from colorama import Fore, Style, init

# Initialize colorama
# init(autoreset=True)
# Initialize the priority queue
task_queue = []  # A list to store tasks as a heap
task_ids = set()  # A set to track unique Task IDs

# Function to load tasks from the JSON file
def load_tasks():
    global task_queue, task_ids
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    heapq.heappush(task_queue, (task["Priority"], task["ID"], task["Title"]))
                    task_ids.add(task["ID"])
        except Exception as e:
            print(f"Error loading tasks from file: {e}")

# Function to save tasks to the JSON file
def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            tasks = [{"ID": task[1], "Title": task[2], "Priority": task[0]} for task in task_queue]
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks to file: {e}")

def display_menu():
 
    print("\n///////////////////////////////////////////////////////////////////////////////////////")
    print("///////////////////////////////  🎯   TO-DO LIST   ✅  ////////////////////////////////")
    print("///////////////////////////////////////////////////////////////////////////////////////")
    print("🌟 Welcome to the Priority Task Queue! 🌟")
    print("Choose an option:")
    print("1️⃣. ➕ Add Task")
    print("2️⃣. 📋 List All Tasks")
    print("3️⃣. 🔍 View Highest Priority Task")
    print("4️⃣. ❌ Remove Highest Priority Task")
    print("5️⃣. 🚪 Exit")

    

def add_task():
    try:
        task_id = int(input("Enter Task ID: "))
        if task_id in task_ids:
            print(f"Error: Task ID {task_id} already exists. Please use a unique Task ID.")
            return
        title = input("Enter Task Title: ")
        priority = int(input("Enter Task Priority (lower number = higher priority): "))
        
        # Add task to the heap and track the Task ID
        heapq.heappush(task_queue, (priority, task_id, title))
        task_ids.add(task_id)
        print("Task successfully added.")
        save_tasks()  # Save tasks directly after adding
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers for Task ID and Priority.")

def list_tasks():
    if not task_queue:
        print("No tasks available.")
        return
    # To print bold text
    print("\033[1mAll Tasks Sorted by Priority:\033[0m")

    print("{:<5} {:<10} {:<20} {:<10}".format("No.", "Task ID", "Title", "Priority"))
    sorted_tasks = sorted(task_queue)  # Sort the heap by priority
    for idx, (priority, task_id, title) in enumerate(sorted_tasks, 1):
        print("{:<5} {:<10} {:<20} {:<10}".format(idx, task_id, title, priority))

def view_highest_priority_task():
    if not task_queue:
        print("Error: No tasks available.")
        return
    # Get the highest priority task (smallest priority value)
    priority, task_id, title = task_queue[0]
    print(f"Highest Priority Task: {{ID: {task_id}, Title: \"{title}\", Priority: {priority}}}")

def remove_highest_priority_task():
    if not task_queue:
        print("Error: No tasks available to remove.")
        return
    # Remove the highest priority task (smallest priority value)
    priority, task_id, title = heapq.heappop(task_queue)
    task_ids.remove(task_id)
    print(f"Removed Task: {{ID: {task_id}, Title: \"{title}\", Priority: {priority}}}")
    print("Queue updated.")
    save_tasks()  # Save tasks directly after removing

# Main program loop
def main():
    load_tasks()  # Load tasks when the program starts
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            view_highest_priority_task()
        elif choice == "4":
            remove_highest_priority_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
