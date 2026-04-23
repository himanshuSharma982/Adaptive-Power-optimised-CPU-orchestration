def report(predicted_cpu, resources, waiting, energy, anomalies):

    print("\n===== ENERGY SYSTEM REPORT =====")
    print("Predicted Load:", round(predicted_cpu,2))
    print("Resources Allocated:", resources)
    print("Total Waiting Time:", waiting)
    print("Total Energy:", round(energy,2))
    print("Anomalies Detected:", len(anomalies))