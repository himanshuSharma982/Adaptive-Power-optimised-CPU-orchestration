from config import CONFIG

def compute_power_quadratic(cpu):
    return CONFIG["POWER_BASE"] + CONFIG["POWER_DYNAMIC_FACTOR"] * (cpu/100)**2

def compute_power(cpu):
    return 1 + (cpu / 50) ** 3 * 15

def compute_power(cpu):
    # make high CPU disproportionately expensive
    return 1 + (cpu/100.0)**3 * 12
def compute_energy(cpu, execution_time, waiting_time):

    power = compute_power(cpu)

    # base energy
    energy = power * execution_time

    # 🔥 PEAK PENALTY (THIS IS THE KEY)
    if cpu > 60:
        energy += (cpu - 60) ** 2 * execution_time * 0.5

    # small waiting cost
    energy += waiting_time * 0.05

    return energy