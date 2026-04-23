import pandas as pd
import numpy as np
import time

from energy_predictor import predict_energy
from workload_analyzer import analyze_tasks
from anomaly_detector import detect_anomalies
from optimizer import optimize, fcfs, sjf, energy_aware
from autoscaler import scale_resources
from monitor import report
from simulation import run_simulation
from analytics import compute_efficiency

import matplotlib.pyplot as plt

def plot_gantt(timeline, title="Gantt Chart"):

    plt.figure()

    for i, task in enumerate(timeline):
        plt.barh(
            y=i,
            width=task["duration"],
            left=task["start"]
        )

    plt.xlabel("Time")
    plt.ylabel("Tasks")
    plt.title(title)
    plt.show()




# ===============================
# SYSTEM CONFIG
# ===============================
N_ROWS = 5000
TASK_SAMPLE = 100

# ===============================
# STEP 1: LOAD DATA
# ===============================
print("\n[INFO] Loading dataset...")
df = pd.read_csv("machine_usage.csv", nrows=N_ROWS, header=None)

df.columns = ["machine_id","timestamp","cpu","memory","c5","c6","c7","c8","c9"]
df = df[["cpu","memory"]]

df["cpu"] = pd.to_numeric(df["cpu"], errors='coerce')
df["memory"] = pd.to_numeric(df["memory"], errors='coerce')
df = df.dropna().reset_index(drop=True)

print("[INFO] Data loaded:", len(df), "rows")

# ===============================
# STEP 2: FEATURE ENGINEERING
# ===============================
print("\n[INFO] Generating execution time...")

# 🔥 create diverse workloads
df["execution_time"] = (
    df["cpu"] * np.random.uniform(0.05, 0.2, len(df)) +
    df["memory"] * np.random.uniform(0.02, 0.1, len(df)) +
    np.random.uniform(1, 10, len(df))
).astype(int) + 1

df["task_id"] = np.arange(len(df))
# 🔥 inject heavy tasks (CRUCIAL)
# add some heavier CPU tasks to create contrast


# inject some heavy CPU tasks to reflect real spikes
idx = np.random.choice(df.index, size=int(0.25*len(df)), replace=False)
df.loc[idx, "cpu"] = df.loc[idx, "cpu"] * 2.0

# ===============================
# STEP 3: SAMPLE TASKS
# ===============================
tasks = df.sample(TASK_SAMPLE).to_dict("records")
print("[INFO] Sampled tasks:", len(tasks))

# ===============================
# STEP 4: WORKLOAD ANALYSIS
# ===============================
print("\n[INFO] Analyzing workload...")
tasks = analyze_tasks(tasks)

# ===============================
# STEP 5: ANOMALY DETECTION
# ===============================
print("[INFO] Detecting anomalies...")
anomalies = detect_anomalies(tasks)
print("[INFO] Anomalies found:", len(anomalies))

# ===============================
# STEP 6: WORKLOAD PREDICTION
# ===============================
print("\n[INFO] Predicting future CPU load...")
predicted_cpu = predict_energy(df)
print("[INFO] Predicted CPU:", round(predicted_cpu,2))

# ===============================
# STEP 7: AUTO-SCALING
# ===============================
print("\n[INFO] Allocating resources...")
resources = scale_resources(predicted_cpu)
print("[INFO] Resources allocated:", resources)

# ===============================
# STEP 8: BASE OPTIMIZATION
# ===============================
print("\n[INFO] Running base optimizer...")
waiting_base, energy_base = optimize(tasks)

# ===============================
# STEP 9: MULTI-STRATEGY SIMULATION
# ===============================

print("\n[INFO] Running scheduling strategies...")

strategies = {
    "FCFS": fcfs,
    "SJF": sjf
}

results = {}

# 🔁 NORMAL STRATEGIES
for name, strategy in strategies.items():

    start = time.time()

    waiting, energy, timeline = run_simulation(tasks, strategy)

    end = time.time()

    results[name] = {
        "waiting": waiting,
        "energy": energy,
        "efficiency": compute_efficiency(tasks, energy),
        "runtime": end - start
    }


# 🔥 ENERGY-AWARE (SPECIAL CASE)
start = time.time()

tasks_energy = energy_aware(tasks, resources)
waiting, energy, timeline = run_simulation(tasks_energy, lambda x: x)

end = time.time()
results["Adaptive Energy-Aware"] = {
    "waiting": waiting,
    "energy": energy,
    "efficiency": compute_efficiency(tasks, energy),
    "runtime": end - start,
    "timeline": timeline   # 🔥 ADD THIS LINE
}
# ===============================
# STEP 10: FINAL REPORT
# ===============================
print("\n--- STRATEGY COMPARISON ---")

for name, res in results.items():
    print(f"\n{name}:")
    print(" Waiting Time:", res["waiting"])
    print(" Energy:", round(res["energy"],2))
    print(" Efficiency:", round(res["efficiency"],4))
    print(" Runtime:", round(res["runtime"],5))
    

# ===============================
# STEP 11: BEST STRATEGY (MULTI-OBJECTIVE)
# ===============================

def score(res):
    return (
        0.85 * res["energy"] +
        0.10 * res["waiting"] -
        0.05 * res["efficiency"]
    )

best = min(results, key=lambda x: score(results[x]))

print("\n🏆 BEST STRATEGY (SMART SCORE):", best)

print("\n--- SCORE BREAKDOWN ---")
for name, res in results.items():
    print(name, "-> Score:", round(score(res), 2))

# ===============================
# STEP 12: OPTIONAL EXPORT
# ===============================
save = False

if save:
    pd.DataFrame(results).to_csv("results.csv")
    print("[INFO] Results saved to results.csv")

print("\n[INFO] System execution complete.")


# ===============================
# STEP 13: VISUALIZATION
# ===============================

methods = list(results.keys())

energy = [results[m]["energy"] for m in methods]
waiting = [results[m]["waiting"] for m in methods]

# Energy Graph
plt.figure()
plt.bar(methods, energy)
plt.title("Energy Comparison")
plt.ylabel("Energy")
plt.show()

# Waiting Time Graph
plt.figure()
plt.bar(methods, waiting)
plt.title("Waiting Time Comparison")
plt.ylabel("Waiting Time")
plt.show()








