def classify_task(cpu):
    if cpu < 30:
        return "light"
    elif cpu < 70:
        return "medium"
    else:
        return "heavy"


def analyze_tasks(tasks):
    for t in tasks:
        t["type"] = classify_task(t["cpu"])
    return tasks