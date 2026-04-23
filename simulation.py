from energy_model import compute_energy

def run_simulation(tasks, strategy_func):

    tasks_sorted = strategy_func(tasks)

    time = 0
    total_energy = 0
    total_waiting = 0

    system_load = 0
    

    for t in tasks_sorted:

        waiting = time
        total_waiting += waiting

        system_load = system_load + t["cpu"]

        energy = (system_load ** 2) * 0.01 + t["execution_time"] * (1 + t["cpu"]/100)

        total_energy += energy

        time += t["execution_time"]

    return total_waiting, total_energy, []

