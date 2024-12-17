import random
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed=47):  # Menggunakan seed 047
    random.seed(seed)
    return [random.randint(0, max_value) for _ in range(n)]

# Fungsi untuk memeriksa apakah elemen dalam array unik
def is_unique(array):
    seen = set()
    for num in array:
        if num in seen:
            return False
        seen.add(num)
    return True

# Fungsi menghitung worst case
def calculate_worst_case(n):
    return n 

# Fungsi menghitung average case
def calculate_average_case(n):
    return n / 2

# Parameter
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 250 - 47
seed = 47  #  NIM 047

# Data untuk plotting
worst_case_times = []
average_case_times = []

for n in n_values:
    array = generate_array(n, max_value, seed)
    
    # Perhitungan Worst Case
    worst_case_time = calculate_worst_case(n)
    worst_case_times.append(worst_case_time)
    
    # Perhitungan Average Case
    average_case_time = calculate_average_case(n)
    average_case_times.append(average_case_time)

# Plotting
for i, n in enumerate(n_values):
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, worst_case_times, label='Worst Case', marker='o', color="yellow")
    plt.plot(n_values, average_case_times, label='Average Case', marker='x', color="green")
    plt.title(f"Worst Case and Average Case Analysis for n={n}")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Number of Operations")
    plt.legend()
    plt.grid(True)
    plt.show()
