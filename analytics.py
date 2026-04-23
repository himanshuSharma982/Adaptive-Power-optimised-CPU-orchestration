import numpy as np

def compute_efficiency(tasks, energy):
    total_work = sum(t["execution_time"] for t in tasks)
    return total_work / energy

def fairness(waiting_times):
    return np.var(waiting_times)

def summarize(results):
    for name, res in results.items():
        print(f"\n{name}:")
        print("Waiting:", res["waiting"])
        print("Energy:", res["energy"])
        print("Efficiency:", res["efficiency"])