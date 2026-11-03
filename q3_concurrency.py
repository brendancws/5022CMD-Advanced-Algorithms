
import time  # Used to measure execution time in nanoseconds
import threading  # Provides support for multithreading


# ==================================================
# FUNCTION 1: RECURSIVE FIBONACCI CALCULATION
# ==================================================
# Calculates Fibonacci numbers using recursion.
# Each number is the sum of the previous two numbers.
# Base cases prevent the recursion from continuing forever.

def calculate_fibonacci(n):
    """Recursive Fibonacci calculation."""

    # Return 0 if n is zero or negative
    if n <= 0:
        return 0

    # Return 1 if n equals 1
    elif n == 1:
        return 1

    # Recursively calculate the previous two Fibonacci numbers
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


# ==================================================
# CLASS 1: FIBONACCI THREAD
# ==================================================
# Creates a separate thread for Fibonacci calculation.
# Each thread stores its input, result, and execution times.

class FibThread(threading.Thread):

    def __init__(self, n):
        super().__init__()  # Initialize the parent Thread class
        self.n = n  # Fibonacci number to calculate
        self.result = None  # Stores the calculated result
        self.start_ns = 0  # Stores the thread's start time
        self.end_ns = 0  # Stores the thread's end time

    # Automatically runs when the thread is started
    def run(self):

        # Capture start time when this thread begins execution
        self.start_ns = time.perf_counter_ns()

        # Perform the recursive Fibonacci calculation
        self.result = calculate_fibonacci(self.n)

        # Capture end time when this thread finishes computation
        self.end_ns = time.perf_counter_ns()


# ==================================================
# FUNCTION 2: MULTITHREADED BENCHMARK
# ==================================================
# Runs three Fibonacci calculations using separate threads.
# Repeats the benchmark 10 times to calculate average time.

def run_multithreaded_benchmark():

    # Fibonacci inputs used for performance testing
    fib_inputs = [35, 38, 40]

    rounds = 10  # Number of benchmark repetitions
    total_times = []  # Stores execution time for each round

    print("\n=== Fibonacci Computation (With Multithreading) ===")

    # Repeat the multithreading benchmark for 10 rounds
    for r in range(1, rounds + 1):

        # Create one thread for each Fibonacci input
        threads = [FibThread(n) for n in fib_inputs]

        # Start all threads
        for t in threads:
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()

        # t1 = start time of the thread that started first (minimum start time)
        # t2 = end time of the thread that completed last (maximum end time)
        t1 = min(t.start_ns for t in threads)
        t2 = max(t.end_ns for t in threads)

        # Calculate total elapsed time in nanoseconds
        elapsed_t = t2 - t1
        total_times.append(elapsed_t)

        # Store Fibonacci results using their input numbers
        results_map = {t.n: t.result for t in threads}

        # Display the results and execution time for this round
        print(
            f"Round {r:2d} : Fib(35)={results_map[35]}, Fib(38)={results_map[38]}, Fib(40)={results_map[40]} | T = {elapsed_t:,} ns")

    # Calculate average execution time across all rounds
    avg_t = sum(total_times) / rounds

    print(f"Average T (With Multithreading)    : {int(avg_t):,} ns")
    return avg_t


# ==================================================
# FUNCTION 3: SEQUENTIAL BENCHMARK
# ==================================================
# Calculates Fibonacci numbers one after another.
# No additional threads are created.
# Repeats 10 rounds for comparison with multithreading.

def run_sequential_benchmark():

    fib_inputs = [35, 38, 40]  # Same inputs for a fair comparison
    rounds = 10
    total_times = []

    print("\n=== Fibonacci Computation (Without Multithreading) ===")

    # Run the sequential benchmark 10 times
    for r in range(1, rounds + 1):

        # Record the start time before calculations
        t1 = time.perf_counter_ns()

        # Calculate Fibonacci numbers sequentially
        results = [calculate_fibonacci(n) for n in fib_inputs]

        # Record the end time after all calculations
        t2 = time.perf_counter_ns()

        # Calculate elapsed time and save it
        elapsed_t = t2 - t1
        total_times.append(elapsed_t)

        # Display Fibonacci results and execution time
        print(f"Round {r:2d} : Fib(35)={results[0]}, Fib(38)={results[1]}, Fib(40)={results[2]} | T = {elapsed_t:,} ns")

    # Calculate average sequential execution time
    avg_t = sum(total_times) / rounds

    print(f"Average T (Without Multithreading) : {int(avg_t):,} ns")
    return avg_t


# ==================================================
# FUNCTION 4: MAIN PROGRAM
# ==================================================
# Displays the menu and runs both benchmarks.
# Compares their average execution times in percentage.

def main():

    # Keep displaying the menu until the user exits
    while True:

        print("\n==== Question 3: Concurrency Benchmark ====")
        print("1. Run Benchmark (Multithreaded vs Sequential)")
        print("2. Exit")

        # Get the user's menu selection
        choice = input("Enter choice (1-2): ").strip()

        if choice == '1':

            # Run both benchmarks and collect average times
            avg_multi = run_multithreaded_benchmark()
            avg_seq = run_sequential_benchmark()

            # Calculate the percentage difference between both methods
            diff_percent = abs(avg_multi - avg_seq) / avg_seq * 100

            # Determine whether multithreading reduced or increased time
            faster_str = "reduced" if avg_multi < avg_seq else "increased"

            # Display the benchmark performance comparison
            print(
                f"\nObservation: Multithreading {faster_str} the average completion time by approximately {diff_percent:.1f}%.\n")

        elif choice == '2':

            # Exit the program when option 2 is selected
            print("Exiting. Goodbye!")
            break

        else:

            # Handle invalid menu selections
            print("Invalid choice.")


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================
# Runs the main function when the file is executed directly.

if __name__ == "__main__":
    main()
