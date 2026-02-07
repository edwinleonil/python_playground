import random
import matplotlib.pyplot as plt
import copy

def visualize_comparison():
    # 1. Setup Data
    N = 100
    # Create one random list
    original_data = [random.randint(0, 1000) for _ in range(N)]
    
    # Create two independent copies so they start identical
    data_stochastic = original_data.copy()
    data_quicksort = original_data.copy()

    # Trackers
    stoch_comparisons = 0
    qs_comparisons = 0

    # 2. Setup Plot
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- Pot 1: Stochastic ---
    bars1 = ax1.bar(range(N), data_stochastic, color='skyblue')
    ax1.set_title('Stochastic Optimization')
    ax1.set_ylim(0, 1050)
    ax1.set_xlim(-1, N)
    
    # --- Plot 2: QuickSort ---
    bars2 = ax2.bar(range(N), data_quicksort, color='salmon')
    ax2.set_title('QuickSort')
    ax2.set_ylim(0, 1050)
    ax2.set_xlim(-1, N)

    # 3. Algorithms
    
    # Generator for QuickSort (Iterative to be pause-able)
    def quicksort_generator(arr):
        nonlocal qs_comparisons
        size = len(arr)
        stack = [(0, size - 1)]
        
        while stack:
            start, end = stack.pop()
            if start >= end:
                continue
                
            pivot = arr[end]
            low = start
            
            # Partitioning
            for i in range(start, end):
                qs_comparisons += 1  # Logic: "if arr[i] < pivot"
                if arr[i] < pivot:
                    arr[i], arr[low] = arr[low], arr[i]
                    low += 1
                    yield True # Visual update on swap
            
            arr[low], arr[end] = arr[end], arr[low]
            yield True 
            
            # Push sides to stack
            stack.append((low + 1, end))
            stack.append((start, low - 1))

    # Initialize QuickSort Generator
    qs_gen = quicksort_generator(data_quicksort)
    qs_finished = False

    # Stochastic Helpers
    def check_sorted(arr):
        # This check is "free" just for the loop condition, 
        # or else the check cost dominates the metric 
        # (in reality, checking if sorted IS expensive, but we'll ignore it for the visual game)
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
        return True

    print("Starting Comparison...")

    # 4. Main Animation Loop
    while True:
        # --- Update Stochastic Sort ---
        stoch_sorted = False
        if check_sorted(data_stochastic):
            stoch_sorted = True
            for bar in bars1: bar.set_color('lightgreen')
        else:
            # Perform a batch of random attempts
            for _ in range(100): 
                idx = random.randint(0, N - 2)
                
                # Comparison happens here
                stoch_comparisons += 1
                if data_stochastic[idx] > data_stochastic[idx+1]:
                    data_stochastic[idx], data_stochastic[idx+1] = data_stochastic[idx+1], data_stochastic[idx]

        # --- Update QuickSort ---
        # We process MULTIPLE steps of QuickSort per frame to speed it up
        # Increase the range (e.g., range(10)) to make it faster
        for _ in range(50): 
            if not qs_finished:
                try:
                    # Advance generator
                    next(qs_gen) 
                except StopIteration:
                    qs_finished = True
                    for bar in bars2: bar.set_color('lightgreen')
                    break
        
        # --- Update Visuals ---
        # Update Stochastic Bars
        for bar, h in zip(bars1, data_stochastic):
            bar.set_height(h)
        ax1.set_title(f'Stochastic\nComparisons: {stoch_comparisons}')

        # Update QuickSort Bars
        for bar, h in zip(bars2, data_quicksort):
            bar.set_height(h)
        status_qs = "Sorted" if qs_finished else "Running"
        ax2.set_title(f'QuickSort\nComparisons: {qs_comparisons} ({status_qs})')

        fig.canvas.draw()
        fig.canvas.flush_events()

        # Check termination
        if stoch_sorted and qs_finished:
            print(f"Comparison Finished.")
            print(f"Stochastic Comparisons: {stoch_comparisons}")
            print(f"QuickSort Comparisons: {qs_comparisons}")
            plt.pause(5) # Hold final screen
            break

        # Adjust speed
        # plt.pause(0.001) 

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    visualize_comparison()
