tasks = []
completed_tasks = []
def add_task():
 task_name = input("Enter the task name:")
 if task_name == "":
  print("Sorry, task name cannot be empty. please try again")
  return add_task()
 task_desc = input("Enter a task description(optional):")
 task_state = input("Enter the status of the task(E.G, pending, completed, started, on hold, etc):")
 task = {
  "name": task_name,
  "description": task_desc,
  "status": task_state
 }
 tasks.append(task)
 print("Task added successfully!")
def complete_task(task_index):
 task = tasks[task_index]
 task["status"] = "completed"
 completed_tasks.append(task)
 tasks.remove(task)
 print(f"Congrats. the task {task['name']} has been completed!")
def list_tasks():
 num = 0
 while num < len(tasks):
  print(f"{num+1}. task: {tasks[num]['name']}. status: {tasks[num]['status']}.")
  num += 1
print("Welcome to this ToDo list app! Please read the commands carefully")
while True:
 print("Please choose an options from the list below")
 command = int(input("Enter a command: (1. add new tasks. 2. complete a task. 3. View completed tasks. 4. go back)"))
 if command == 1:
  add_task()
 elif command == 2:
  print("Here are the currently availabel tasks:")
  list_tasks()
  child_command = int(input("Please choose a task number to complete (or -1 to go back):"))
  if child_command == -1:
   continue
  else:
   complete_task(child_command-1)
 elif command == 3:
  print("Here are all the completed tasks:")
  [print(f"{x['name']}. description: {x['description']}. status: {x['status']}") for x in completed_tasks]
 else:
  print("Exiting, goodbye!")
  break
