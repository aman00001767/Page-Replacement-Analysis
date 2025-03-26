import time

class PerformanceAnalyzer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def evaluate(self, reference_string, frames):
        start_time = time.time()
        page_faults = self.algorithm(frames).execute(reference_string)
        execution_time = time.time() - start_time
        hit_ratio = (len(reference_string) - page_faults) / len(reference_string)

        return {
            "Algorithm": self.algorithm.__name__,
            "Page Faults": page_faults,
            "Execution Time (s)": execution_time,
            "Hit Ratio": hit_ratio
        }

if __name__ == "__main__":
    reference_string = [1, 3, 0, 3, 5, 6, 3]
    frames = 3
    from module1_algorithms import FIFO

    analyzer = PerformanceAnalyzer(FIFO)
    result = analyzer.evaluate(reference_string, frames)
    print(result)
from module1_algorithms import FIFO, LRU, Optimal, LFU, Clock

algorithms = [FIFO, LRU, Optimal, LFU, Clock]
results = []

for algo in algorithms:
    analyzer = PerformanceAnalyzer(algo)
    results.append(analyzer.evaluate(reference_string, frames))

for res in results:
    print(res)
from tabulate import tabulate

print(tabulate(results, headers="keys", tablefmt="grid"))
import matplotlib.pyplot as plt
import numpy as np

def plot_results(results):
    algorithms = [res["Algorithm"] for res in results]
    page_faults = [res["Page Faults"] for res in results]
    execution_times = [res["Execution Time (s)"] for res in results]

    x = np.arange(len(algorithms))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, page_faults, width, label="Page Faults")
    ax.bar(x + width/2, execution_times, width, label="Execution Time")

    ax.set_ylabel("Values")
    ax.set_title("Performance Comparison of Page Replacement Algorithms")
    ax.set_xticks(x)
    ax.set_xticklabels(algorithms)
    ax.legend()

    plt.show()

plot_results(results)
