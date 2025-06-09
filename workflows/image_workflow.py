import time
import random
from utils.logger import log_event

def simulate_image_generation(task_id: str = None) -> bool:
    try:
        log_event("info", "image-workflow-start", "Starting image generation", service="image-service", task_id=task_id)

        start_time = time.time()

        # Simulate processing delay (3 to 9 seconds)
        delay = random.uniform(3, 9)
        time.sleep(delay)

        if random.choice([False, False, True]):  # ~33% chance failure
            raise RuntimeError("Simulated image generation failure")

        duration_ms = int((time.time() - start_time) * 1000)

        if duration_ms > 7000:
            log_event("warning", "image-generation-latency", "Image generation took too long", service="image-service", duration_ms=duration_ms, task_id=task_id)
        else:
            log_event("info", "image-generation-complete", "Image generation completed successfully", service="image-service", duration_ms=duration_ms, task_id=task_id)

        return True

    except Exception as e:
        log_event("error", "image-generation-failure", str(e), service="image-service", task_id=task_id)
        return False
