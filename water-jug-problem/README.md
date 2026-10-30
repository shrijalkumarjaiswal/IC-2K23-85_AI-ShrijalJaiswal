# Water Jug Problem in Python

## 1. Introduction
The Water Jug Problem is a classical problem in Artificial Intelligence (AI). It involves two water jugs of different capacities and requires performing different operations to manage the amount of water in them.

This Python program provides an interactive way to perform these operations and observe the changes in the state of both jugs after each step.

## 2. Problem Description
The program uses two water jugs:

- **Jug 1:** Capacity of 4 litres.
- **Jug 2:** Capacity of 3 litres.

Initially, both jugs are empty. The user can select different operations to fill, empty, or transfer water between the jugs.

## 3. Features

- Interactive menu-based program.
- Fill either jug completely.
- Empty either jug.
- Transfer water between the two jugs.
- Display the current state after each operation.
- Validate user input.
- Prevent filling an already full jug.
- Prevent emptying an already empty jug.
- Prevent water overflow during transfer.

## 4. Available Operations

| Choice | Operation |
|---|---|
| 1 | Fill Jug 1 |
| 2 | Fill Jug 2 |
| 3 | Empty Jug 1 |
| 4 | Empty Jug 2 |
| 5 | Pour Jug 1 into Jug 2 |
| 6 | Pour Jug 2 into Jug 1 |
| 7 | Exit Program |

## 5. Technologies Used

- **Programming Language:** Python
- **Concepts:** Loops, Conditional Statements, Variables, User Input, and State Transitions.

## 6. How to Run the Program

1. Install Python on your computer.
2. Save the program in a file named `water_jug.py`.
3. Open the terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the following command:

```bash
python water_jug.py
```

6. Select an operation from the displayed menu.
7. Observe the updated state after every operation.

## 7. Example

Initially:

```text
Jug 1: 0 / 4
Jug 2: 0 / 3
```

After selecting option 1 (Fill Jug 1):

```text
Jug 1: 4 / 4
Jug 2: 0 / 3
```

After selecting option 5 (Pour Jug 1 into Jug 2):

```text
Jug 1: 1 / 4
Jug 2: 3 / 3
```

## 8. Constraints

- Jug 1 cannot contain more than 4 litres.
- Jug 2 cannot contain more than 3 litres.
- Water cannot be transferred from an empty jug.
- Water cannot be transferred into a full jug.
- An already full jug cannot be filled again.
- An already empty jug cannot be emptied again.
- Only valid menu choices (1–7) are accepted.

## 9. Learning Outcomes

By implementing this program, we understand:

- The concept of state-space representation in AI.
- How actions change the current state.
- How to apply constraints to a problem.
- How to implement a simple problem-solving approach using Python.
- How to handle invalid user inputs.

## 10. Conclusion

The Water Jug Problem demonstrates the basic concepts of Artificial Intelligence, particularly states, actions, and constraints. This program provides a simple interactive implementation in Python, allowing users to perform operations and observe state changes step by step.