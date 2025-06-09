import logging
import json
import time
import datetime
import watchtower
import config  # for LOG_GROUP_NAME, AWS_REGION, ENV

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
            "level": record.levelname,
            "message": record.getMessage(),
            "env": config.ENV,
        }
        if hasattr(record, "extra_data"):
            log_data.update(record.extra_data)
        return json.dumps(log_data)

class DynamicLogger:
    def __init__(self):
        self.log_group = config.LOG_GROUP_NAME
        self.region = config.AWS_REGION

    def get_logger(self, level=logging.INFO):
        logger_name = self.log_group
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        if not logger.handlers:
            formatter = JsonFormatter()

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            # Create stream name with timestamp
            timestamp_str = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
            stream_name = f"{self.log_group}/{timestamp_str}"

            cloudwatch_handler = watchtower.CloudWatchLogHandler(
                log_group=self.log_group,
                stream_name=stream_name,
                create_log_group=True,
                # region_name=self.region,  # optional
            )
            cloudwatch_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(cloudwatch_handler)

        return logger

def log_event(level, event, message, **kwargs):
    dyn_logger = DynamicLogger()
    logger = dyn_logger.get_logger()
    extra = {
        "event": event,
        "extra_data": kwargs
    }
    getattr(logger, level.lower())(message, extra=extra)
