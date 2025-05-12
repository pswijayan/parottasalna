import sys
import os

TASK_FILE = 'task.txt'

def load_from_file():
    task_list = []
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return task_list
    else:   
        with open(TASK_FILE, 'r') as file:
            for line in file:
                task_list.append(line.strip())
        return task_list

def save_to_file(tasks_list):
    with open(TASK_FILE, 'w') as file:
        for task in tasks_list:
            file.write(f'{task.strip()}\n')

def add_task(new_task, task_description, status="pending"):
    tasks_list = load_from_file()
    tasks_list.append(f'{new_task} || {task_description} || {status}')
    save_to_file(tasks_list)
    print(f'\033[93mNew {new_task} Task added\033[0m') 

def delete_task(index):
    index = int(index)
    tasks_list = load_from_file()
    #print(tasks_list)
    if index >= 0 and index < len(tasks_list):
        del tasks_list[index]
        save_to_file(tasks_list)
        print('\033[93mTask deleted Sucessfully!\033[0m')
        show_tasks()
    else:
        print('\033[93mPlease check Your Input, Whole stored Tasks below: \033[0m')
        show_tasks()

def update_task(index):
    index = int(index)
    tasks_list = load_from_file()
    if index >=0 and index < len(tasks_list):
        task = tasks_list[index]
        #title, Description, status    
        task = task.split('||')

        if task[2].lower().strip() == 'pending':
            task[2] = 'done'
            tasks_list[index] = '||'.join(task)
            save_to_file(tasks_list)
            print('\033[93m Updated sucessfully\033[0m') 

        else:
            task[2] = 'pending'
            tasks_list[index] = '||'.join(task)
            save_to_file(tasks_list)
            print('\033[93m Updated sucessfully\033[0m')

        show_tasks()
    else:
        print('\033[93mPlease check Your Input, Whole stored Tasks below: \033[0m')
        show_tasks()
        
            

def pending_task():
    tasks_list = load_from_file()
    pend_task = []
    for index, task in enumerate(tasks_list):
        task = task.split('||')
        # task have three property title, Description, status
        if task[2].lower().strip() == 'pending': 
            #index, title, Description, status
            pend_task.append(f'{index} || {task[0]} || {task[1]} || {task[2]}') 
    return pend_task

def finished_task():
    tasks_list = load_from_file()
    finished_task = []
    for index, task in enumerate(tasks_list):
        task = task.split('||')
        # task have three property title, Description, status
        if task[2].lower().strip() == 'done': 
            #index, title, Description, status
            finished_task.append(f'{index} || {task[0]} || {task[1]} || {task[2]}') 
    return finished_task


def show_tasks():
    def display_task(tasks):
        for task_str in tasks:
            task_parts = task_str.split('||')
            #index, title, Description, status
            print(f'{task_parts[0].strip()} - {task_parts[1].strip()} "{task_parts[2].strip()}" -> {task_parts[3].strip()} ')

    print('\033[93mPENDIN TASKS\033[0m\n------------') 
    display_task(pending_task())

    print('- - - - - - - - - - - - - - - - - - - - - - -')

    print('\033[93mFINISHED TASKS\033[0m\n------------')
    display_task(finished_task())
            
def show_help():
    print('''
Please use commad line like this to run this TODO
* create task           \033[93m<python or python3> <filename.py> c 'title' 'Description' \033[0m
* show tasks            \033[93m<python or python3> <filename.py> s  \033[0m
* update task status    \033[93m<python or python3> <filename.py> u <index>  \033[0m      - its toggle
* delete task           \033[93m<python or python3> <filename.py> d <index>  \033[0m
''')


def todo():
    inline_argument = sys.argv
    length = len(inline_argument)
    
    try:
        if length == 1:
            show_help()

        elif length == 2 and inline_argument[1].lower() == 's':
            show_tasks()

        elif length == 3 and inline_argument[1].lower() == 'u':
            update_task(inline_argument[2])
        
        elif length == 3 and inline_argument[1].lower() == 'd':
            delete_task(int(inline_argument[2]))

        elif length == 4 and inline_argument[1].lower() == 'c':
            add_task(inline_argument[2],inline_argument[3] )
        else:
            show_help()
    except ValueError as v:
        print('\033[93mPlease enter Correct format, index only accept number \033[0m', v)
        show_help()

    except Exception as e:
        print(e)
        show_help()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    #clear_screen()
    todo()

if __name__ == '__main__':
    main()
