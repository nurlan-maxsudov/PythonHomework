import json
import csv

def load_tasks(filename="tasks.json"):
    with open(filename, 'r') as file:
        return json.load(file)

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    print("\nAll Tasks:")
    print(f"{'ID':<5}{'Task Name':<20}{'Completed':<12}{'Priority':<8}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5}{task['task']:<20}{str(task['completed']):<12}{task['priority']:<8}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")


def convert_to_csv(tasks, csv_filename="tasks.csv"):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Task", "Completed", "Priority"])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "ID": task['id'],
                "Task": task['task'],
                "Completed": task['completed'],
                "Priority": task['priority']
            })
    print(f"\nTasks have been saved to {csv_filename}")

def mark_task_complete(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"\nTask {task_id} marked as complete.")
            return
    print(f"\nTask with ID {task_id} not found.")

def main():
    tasks = load_tasks()

    display_tasks(tasks)

    calculate_statistics(tasks)

    mark_task_complete(tasks, 3)

    save_tasks(tasks)

    
    convert_to_csv(tasks)

if __name__ == "__main__":
    main()
