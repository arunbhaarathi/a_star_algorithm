
# A* Pathfinding Visualization

This project visualizes the A* pathfinding algorithm using a grid-based representation in Python with the `pygame` library. The user can set a start node, goal node, and obstacles, then execute the algorithm to find the shortest path.

## Prerequisites

- Python 3.x
- `pygame` library

### Installing Pygame

Install `pygame` using pip:
```bash
pip install pygame
```

## How to Run the Code

1. **Execute the Python file**: Run the script with the following command:
   ```bash
   python a_star.py
   ```

2. **Select the Start Node**:
   - Click on a cell in the grid to set it as the **start node** (highlighted in **red**).

3. **Select the Goal Node**:
   - Click on another cell in the grid to set it as the **goal node** (highlighted in **green**).

4. **Draw Obstacles**:
   - To draw obstacles, click on additional cells. Obstacles are highlighted in **black**.

5. **Execute the A* Search**:
   - Press the **Space** key to start the A* search algorithm.
   - During execution:
     - **Open nodes** (nodes being evaluated) are shown in **yellow**.
     - **Closed nodes** (nodes that have been fully evaluated) are shown in **gray**.

6. **Reset the Grid**:
   - Press the **R** key to reset the grid to its initial state.

## Controls

- **Left Mouse Click**:
  - First click: Set the **start node** (red).
  - Second click: Set the **goal node** (green).
  - Additional clicks: Place **obstacles** (black).

- **Right Mouse Click**: Remove a node setting (start, goal, or obstacle) and revert it to white.

- **Space Key**: Begin the A* search algorithm.

- **R Key**: Reset the grid, removing all nodes and obstacles.

## Additional Details

- **Path Visualization**: 
  - If a path is found, the nodes in the path will be highlighted in **blue**.
  - If no path is available, a message is displayed in the console: `"No path found"`.

- **Grid Structure**: 
  - The grid is a square grid with dimensions of `600x600`, divided into cells of equal size (based on grid rows). 
  - The default grid uses 50 rows, which means each cell is approximately 12x12 pixels.

- **Algorithm Details**:
  - The A* algorithm prioritizes nodes based on their `f` value, where `f = g + h`.
  - `g` is the cost from the start node to the current node.
  - `h` is the heuristic (Manhattan distance to the goal).

## Customization

- **Grid Size**: The grid size can be modified by changing the `WIN_SIZE` and `rows` parameters in the code.
- **Node Colors**: Node colors are defined in the code and can be adjusted to suit personal preferences.

## Further Reading
- For a detailed explanation of the A* algorithm, check out this [article on A* Pathfinding](https://medium.com/@arunbhaarathi/a-a-star-search-algorithm-c4eb77634c3a).

## Troubleshooting

- Ensure `pygame` is installed and working correctly.
- If the grid does not respond to mouse clicks, ensure the `pygame` window is focused.

## Credits
- The Pygame interactive grid was inspired by Tech With Tim's tutorials.

## License

This project is for educational purposes and does not come with a specific license. 

