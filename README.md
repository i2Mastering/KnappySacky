# Knapsack Optimization Algorithm

## Overview
This project implements an object-oriented approach to solving the knapsack problem. The knapsack algorithm determines the best combination of items to maximize total value while staying within a specified capacity constraint.

## Features
- Computes the volume of each object.
- Links objects with their corresponding cubic volume and value.
- Implements a greedy algorithm to select the most valuable items within the given capacity.
- Displays the selected items, total value, and remaining space in the knapsack.

## How It Works
1. **Read Input Data**: Reads object details (name, value, height, width, depth) from a CSV file.
2. **Calculate Volume**: Computes the cubic volume of each object.
3. **Sort Objects**: Sorts objects by value-to-volume ratio.
4. **Select Items**: Iteratively adds items to the knapsack until the capacity is reached.
5. **Display Results**: Outputs the selected items, total value, and remaining capacity.

## Installation
Ensure you have Python installed. Clone the repository and ensure you have a CSV file (`IKEpacks.csv`) with object details formatted as:
```
ItemName,Value,Height,Width,Depth
Backpack,100,10,5,5
Laptop,500,2,10,14
...
```

## Usage
Run the script:
```bash
python script.py
```
When prompted, enter the capacity of your knapsack.

## Example Interaction
```
Please enter the capacity of your knapsack: 100
The suggested items are 1 Laptop, 1 Backpack with total value of $600.00 dollars.
The space left in cubic inches is 20.00
```

## License
This project is open-source and free to use.
