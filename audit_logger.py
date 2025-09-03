import json
from datetime import datetime

def log_event(action, data):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "data": data
    }
    with open("audit_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
