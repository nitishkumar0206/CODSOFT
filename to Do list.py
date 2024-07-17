#TO DO LIST USING PYTHON PROGRAMMING

def main ():
    Tasks=[]
    print("WELCOME TO THE TO DO LIST USING PYTHON")
    total_task=int(input("Enter how many tasks you want to add="))
    for i in range(1,total_task + 1):
     task_name =input(f"Enter task {i} =")
     Tasks.append(task_name)

    print("Today's tasks are :",Tasks)


    while True :
          operation=int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n--"))

          if operation == 1:
              add=input("Enter task you want to add =")
              Tasks.append(add)
              print("Task has been added successfully")

          elif operation ==2:
              update=input("Enter the task you want to update=")
              if update in Tasks:
                  x=input("Enter new task=")
                  y=Tasks.index(update)
                  Tasks[y]=x
                  print("Task updated.")
              else:
                  print("Task not found.")

          elif operation==3:
              delete=input("Enter the task you want to delete=")
              if delete in Tasks:
                  x=Tasks.index(delete)
                  del Tasks[x]
                  print("Task has been deleted successfully.")
              else:
                  print("Task not found.")

          elif operation==4:
              print("Total tasks",Tasks)  

          elif operation==5:
              print("Closing the list.")
              break

          else:
              print("Invalid Input. Please enter number from 1 to 5.")          

main()
    