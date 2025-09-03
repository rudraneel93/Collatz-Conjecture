import math
import matplotlib.pyplot as plt

def compute_collatz_stopping_time(n, cache):
    """
    Compute the stopping time s(n) for the Collatz sequence using an iterative approach with memoization.
    """
    steps = 0
    current = n
    while current != 1:
        if current in cache:
            steps += cache[current]
            break
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        steps += 1
    cache[n] = steps
    return steps

def main(N):
    """
    Compute the cumulative average of s(n) / log(n) for n from 2 to N.
    Plot the results to visualize convergence.
    """
    cache = {1: 0}  # Initialize cache with s(1)=0
    running_sum = 0.0
    n_values = []
    average_values = []
    
    for n in range(2, N+1):
        s_n = compute_collatz_stopping_time(n, cache)
        ratio = s_n / math.log(n)  # Using natural log
        running_sum += ratio
        cumulative_average = running_sum / (n - 1)  # Since we start from n=2
        n_values.append(n)
        average_values.append(cumulative_average)
        
        # Print progress every 100,000 steps
        if n % 100000 == 0:
            print(f"Processed n={n}, current average: {cumulative_average}")
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, average_values, label='Cumulative Average')
    plt.xlabel('n')
    plt.ylabel('Cumulative Average of s(n) / log(n)')
    plt.title('Estimation of the Collatz Stopping Constant')
    plt.legend()
    plt.grid(True)
    plt.savefig('collatz_plot.png')
    plt.show()
    
    # Output the final average
    print(f"Final estimated constant for n up to {N}: {cumulative_average}")

if __name__ == "__main__":
    N = 100000000  # Set the upper limit for n
    main(N)
