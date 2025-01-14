
# 🌟 **Priority Task Queue - To-Do List App** 🎯

Welcome to the **Priority Task Queue**! This Python-based app helps you manage tasks with different priority levels. You can add, view, remove tasks, and keep everything organized based on priority.

## ✨ **Features**

- **Add Tasks**: Add tasks with a unique ID, title, and priority level.
- **View Tasks**: View the task with the highest priority.
- **Remove Tasks**: Remove the highest priority task from the list.
- **List All Tasks**: View all tasks sorted by priority.
- **Persistent Storage**: Automatically saves tasks to a JSON file for later use, so no data is lost when the app closes.

---

## 💥 **Extra Features (Bonus)**

- **Dynamic Priority Updates**: Modify the priority of a task dynamically.
- **Stylish Interface**: Uses emojis for a more engaging and user-friendly UI.

---

## 🛠️ **How to Use the Application**

1. **Clone the Repository**:  
   First, clone the repository to your local machine.

   ```bash
   https://github.com/sabarinath404/T0-DO-List.git
   cd T0-DO-List
   ```

2. **Install Python**:  
   Ensure you have Python installed on your system. If you need a specific version, you can install it from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies**:  
   The script uses the built-in `heapq` and `json` libraries, so no extra installations are required for them.

4. **Run the Script**:  
   Simply run the Python script to start the app:

   ```bash
   python task_queue.py
   ```

5. **Interact with the Application**:  
   Once the app is running, choose from the available options to manage your tasks.

---

## 🌟 **Sample Menu**
After running the script, you will see a menu like this:

```
///////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////  🎯   TO-DO LIST   ✅  ////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////
🌟 Welcome to the Priority Task Queue! 🌟
Choose an option:
1️⃣. ➕ Add Task
2️⃣. 📋 List All Tasks
3️⃣. 🔍 View Highest Priority Task
4️⃣. ❌ Remove Highest Priority Task
5️⃣. 🚪 Exit
```

---

## 💡 **How the Priority Queue Works**

- **Priority** is assigned as a number, where lower numbers represent higher priority.
- **Tasks** are stored in a **priority queue**, and the task with the highest priority (smallest number) is always at the top.
- Tasks are saved in a **JSON file**, ensuring they persist even after the app is closed.

---

## 📝 **Example Interactions**

- **Add Task**:  
   ```bash
   Add Task: ID=101, Title="Fix Bug", Priority=1
   ```

- **View Task**:  
   ```bash
   View Task: {ID: 101, Title: "Fix Bug", Priority: 1}
   ```

- **Remove Task**:  
   ```bash
   Remove Task: {ID: 101, Title: "Fix Bug", Priority: 1}
   Queue updated.
   ```

---

## 🛠️ **Technologies Used**

- Python
- Data Structures: Priority Queue, JSON for storage

---

## 📄 **Future Improvements**

- **Dynamic Task Priority**: Implement a feature to modify task priorities after they are created.
- **Task Categories**: Add functionality to categorize tasks (e.g., Work, Personal, Urgent).
- **Task Completion**: Mark tasks as complete and filter them.

---

## 🚀 **Conclusion**

This **Priority Task Queue** app helps you keep your tasks in check, organized by priority, and automatically saves your tasks to a file for later use. 

---

**Happy Tasking!** 🎯
