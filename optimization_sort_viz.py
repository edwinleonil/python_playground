import random
import matplotlib.pyplot as plt

def visualize_optimization():
    # 1. Generate 100 random numbers between 0 and 1000
    N = 100
    numbers = [random.randint(0, 1000) for _ in range(N)]

    # 2. Setup the Plot
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the initial bar chart
    bars = ax.bar(range(len(numbers)), numbers, color='skyblue')
    
    ax.set_ylim(0, 1050)
    ax.set_xlim(-1, N)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Stochastic Optimization Sort: Starting...')

    def calculate_cost(arr):
        """Cost is the number of inversions (smaller numbers following larger ones)."""
        cost = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                cost += 1
        return cost

    iteration = 0
    
    # 3. Optimization Loop
    while True:
        current_cost = calculate_cost(numbers)
        
        # If perfectly sorted, stop
        if current_cost == 0:
            ax.set_title(f"Optimization Complete! Sorted in {iteration} iterations.")
            # Update one last time
            for bar, h in zip(bars, numbers):
                bar.set_height(h)
                bar.set_color('lightgreen') # Change color to indicate success
            fig.canvas.draw()
            fig.canvas.flush_events()
            print("Sorted!")
            break

        # --- Optimization Step (Stochastic Hill Climbing) ---
        # To make the animation visible but fast enough, we perform multiple
        # mutation attempts per "frame" of the plot.
        mutations_per_frame = 50
        changed = False

        for _ in range(mutations_per_frame):
            # Pick a random index
            idx = random.randint(0, N - 2)
            
            # Simple Local Search Rule:
            # If the pair is out of order, swap them to reduce local cost.
            # This is a stochastic implementation of bubble sort logic.
            if numbers[idx] > numbers[idx+1]:
                numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
                changed = True
            
            iteration += 1

        # Only redraw if something changed
        if changed:
            # Efficiently update height of bars instead of clearing plot
            for bar, h in zip(bars, numbers):
                bar.set_height(h)
            
            ax.set_title(f"Iteration: {iteration} | Cost (Inversions): {current_cost}")
            
            # Draw the update
            plt.pause(0.001) 

    # Keep window open after finishing
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    visualize_optimization()
