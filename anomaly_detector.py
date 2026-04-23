def detect_anomalies(tasks):
    anomalies = []

    for t in tasks:
        if t["cpu"] > 90:
            anomalies.append(t)

    return anomalies

def detect_spikes(tasks):
    spikes = [t for t in tasks if t["cpu"] > 90]
    return spikes

def detect_outliers(tasks):
    cpus = [t["cpu"] for t in tasks]
    mean = sum(cpus)/len(cpus)

    outliers = [t for t in tasks if abs(t["cpu"] - mean) > 40]
    return outliers