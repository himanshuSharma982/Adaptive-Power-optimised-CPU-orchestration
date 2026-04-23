from energy_model import compute_energy

def optimize(tasks):

    # prioritize low energy tasks
    tasks_sorted = sorted(tasks, key=lambda x: x["cpu"])

    total_energy = 0
    total_waiting = 0
    time = 0

    for t in tasks_sorted:
        total_waiting += time

        energy = compute_energy(t["cpu"], t["execution_time"], time)
        energy += time * 0.2   # waiting penalty

        total_energy += energy
        time += t["execution_time"]

    return total_waiting, total_energy

def fcfs(tasks):
    return tasks

import numpy as np

def sjf(tasks):
    est = []
    for t in tasks:
        e = t["execution_time"] + np.random.uniform(-2, 2)
        est.append({**t, "est_time": max(1, e)})
    return sorted(est, key=lambda x: x["est_time"])





def hybrid(tasks):
    return sorted(tasks, key=lambda x: (x["cpu"], x["execution_time"]))


def energy_aware(tasks, resources=1):

    return sorted(tasks, key=lambda t: (t["cpu"], -t["execution_time"]))