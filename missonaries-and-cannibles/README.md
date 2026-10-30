# Missionaries and Cannibals Problem in Python

## 1. Introduction

The Missionaries and Cannibals Problem is a classical problem in Artificial Intelligence (AI). It involves transporting three missionaries and three cannibals from one side of a river to the other using a boat.

The challenge is to transport everyone safely without allowing cannibals to outnumber missionaries on either bank when missionaries are present.

This Python program provides an interactive implementation where users select passengers for each crossing and observe the changes in the state after every move.

## 2. Problem Description

The program consists of:

- **Missionaries:** 3
- **Cannibals:** 3
- **Boat Capacity:** Maximum 2 people
- **Starting Position:** Left Bank
- **Destination:** Right Bank

Initially, all missionaries and cannibals are on the left bank. The objective is to move everyone safely to the right bank.

## 3. Features

- Interactive menu-based program.
- Allows users to select passengers for each crossing.
- Supports different passenger combinations.
- Displays the current state of both riverbanks.
- Displays the boat's current position.
- Validates user input.
- Checks passenger availability before crossing.
- Prevents unsafe moves.
- Detects when the goal state is reached.

## 4. Available Operations

| Choice | Operation |
|---|---|
| 1 | Move One Missionary |
| 2 | Move One Cannibal |
| 3 | Move Two Missionaries |
| 4 | Move Two Cannibals |
| 5 | Move One Missionary and One Cannibal |
| 6 | Exit Program |

The selected passengers cross the river in the direction of the boat's current position.

## 5. Technologies Used

- **Programming Language:** Python
- **Concepts:** Loops, Conditional Statements, Variables, User Input, State Transitions, and Logical Conditions.

## 6. How to Run the Program

1. Install Python on your computer.
2. Save the program in a file named `missionaries_cannibals.py`.
3. Open the terminal or command prompt.
4. Navigate to the folder containing the file.
5. Execute the following command:

```bash
python missionaries_cannibals.py
```

6. Select an operation from the displayed menu.
7. Observe the updated state after every crossing.
8. Continue until everyone reaches the right bank.

## 7. State Representation

The program uses the following state representation:

**(Left Missionaries, Left Cannibals, Right Missionaries, Right Cannibals, Boat Position)**

### Initial State

```text
(3, 3, 0, 0, Left)
```

### Goal State

```text
(0, 0, 3, 3, Right)
```

### Example State Transition

Initially:

```text
Left Bank  : 3 Missionaries, 3 Cannibals
Right Bank : 0 Missionaries, 0 Cannibals
Boat Position: Left
```

After moving two cannibals to the right bank:

```text
Left Bank  : 3 Missionaries, 1 Cannibal
Right Bank : 0 Missionaries, 2 Cannibals
Boat Position: Right
```

## 8. Constraints and Validations

- The boat can carry a maximum of two people.
- At least one person must travel in the boat.
- Cannibals cannot outnumber missionaries on either bank when missionaries are present.
- Passengers must be available on the boat's current bank.
- The boat cannot move without passengers.
- Only valid menu choices are accepted.
- The program terminates when all six people reach the right bank.

## 9. Learning Outcomes

By implementing this program, we understand:

- The concept of state-space representation in AI.
- How to define initial and goal states.
- How operators perform state transitions.
- How to implement constraints and safety conditions.
- How to validate actions before changing the current state.
- How to use Python conditional statements for problem-solving.

## 10. Conclusion

The Missionaries and Cannibals Problem demonstrates important Artificial Intelligence concepts such as state-space representation, operators, constraints, and state transitions.

This interactive Python implementation allows users to perform river crossings manually while ensuring that all moves follow the given rules and safety conditions.