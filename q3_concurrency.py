import time
import threading


def calculate_fibonacci(n):
    """Recursive Fibonacci calculation."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


class FibThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = None
        self.start_ns = 0
        self.end_ns = 0

    def run(self):
        # Capture start time when this thread begins execution
        self.start_ns = time.perf_counter_ns()
        self.result = calculate_fibonacci(self.n)
        # Capture end time when this thread finishes computation
        self.end_ns = time.perf_counter_ns()


def run_multithreaded_benchmark():
    fib_inputs = [35, 38, 40]
    rounds = 10
    total_times = []

    print("\n=== Fibonacci Computation (With Multithreading) ===")

    for r in range(1, rounds + 1):
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
        elapsed_t = t2 - t1
        total_times.append(elapsed_t)

        results_map = {t.n: t.result for t in threads}
        print(
            f"Round {r:2d} : Fib(35)={results_map[35]}, Fib(38)={results_map[38]}, Fib(40)={results_map[40]} | T = {elapsed_t:,} ns")

    avg_t = sum(total_times) / rounds
    print(f"Average T (With Multithreading)    : {int(avg_t):,} ns")
    return avg_t


def run_sequential_benchmark():
    fib_inputs = [35, 38, 40]
    rounds = 10
    total_times = []

    print("\n=== Fibonacci Computation (Without Multithreading) ===")

    for r in range(1, rounds + 1):
        t1 = time.perf_counter_ns()

        results = [calculate_fibonacci(n) for n in fib_inputs]

        t2 = time.perf_counter_ns()
        elapsed_t = t2 - t1
        total_times.append(elapsed_t)

        print(f"Round {r:2d} : Fib(35)={results[0]}, Fib(38)={results[1]}, Fib(40)={results[2]} | T = {elapsed_t:,} ns")

    avg_t = sum(total_times) / rounds
    print(f"Average T (Without Multithreading) : {int(avg_t):,} ns")
    return avg_t


def main():
    while True:
        print("\n==== Question 3: Concurrency Benchmark ====")
        print("1. Run Benchmark (Multithreaded vs Sequential)")
        print("2. Exit")

        choice = input("Enter choice (1-2): ").strip()
        if choice == '1':
            avg_multi = run_multithreaded_benchmark()
            avg_seq = run_sequential_benchmark()

            diff_percent = abs(avg_multi - avg_seq) / avg_seq * 100
            faster_str = "reduced" if avg_multi < avg_seq else "increased"
            print(
                f"\nObservation: Multithreading {faster_str} the average completion time by approximately {diff_percent:.1f}%.\n")

        elif choice == '2':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()