import time
from workflows.image_workflow import simulate_image_generation
from utils.logger import log_event
from api.auth import user_login

def main():
    log_event("info", "app-start", "Starting local POC app")

    success_count = 0
    failure_count = 0

    for i in range(10):
        task_id = f"task-{i+1}"
        log_event("info", "task-start", f"Starting task {task_id}", task_id=task_id)

        success = simulate_image_generation(task_id=task_id)

        if success:
            success_count += 1
        else:
            failure_count += 1

        time.sleep(1)

    log_event("info", "app-finish", f"Finished running tasks. Success: {success_count}, Failure: {failure_count}")

    user_login("Sumit")
    user_login("admin")

if __name__ == "__main__":
    main()
