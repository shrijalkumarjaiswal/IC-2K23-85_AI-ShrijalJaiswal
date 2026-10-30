
# Water Jug Problem with Validations

# Maximum capacity of the jugs
jug1_capacity = 4
jug2_capacity = 3

# Initially both jugs are empty
jug1 = 0
jug2 = 0

while True:

    print("\nCurrent State:")
    print("Jug 1:", jug1, "/", jug1_capacity)
    print("Jug 2:", jug2, "/", jug2_capacity)

    print("\nChoose an action:")
    print("1. Fill Jug 1")
    print("2. Fill Jug 2")
    print("3. Empty Jug 1")
    print("4. Empty Jug 2")
    print("5. Pour Jug 1 into Jug 2")
    print("6. Pour Jug 2 into Jug 1")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Validate user input
    if not choice.isdigit() or int(choice) not in range(1, 8):
        print("Invalid choice! Enter a number between 1 and 7.")
        continue

    choice = int(choice)

    # Fill Jug 1
    if choice == 1:
        if jug1 == jug1_capacity:
            print("Jug 1 is already full!")
        else:
            jug1 = jug1_capacity
            print("Jug 1 filled successfully.")

    # Fill Jug 2
    elif choice == 2:
        if jug2 == jug2_capacity:
            print("Jug 2 is already full!")
        else:
            jug2 = jug2_capacity
            print("Jug 2 filled successfully.")

    # Empty Jug 1
    elif choice == 3:
        if jug1 == 0:
            print("Jug 1 is already empty!")
        else:
            jug1 = 0
            print("Jug 1 emptied successfully.")

    # Empty Jug 2
    elif choice == 4:
        if jug2 == 0:
            print("Jug 2 is already empty!")
        else:
            jug2 = 0
            print("Jug 2 emptied successfully.")

    # Pour Jug 1 into Jug 2
    elif choice == 5:
        if jug1 == 0:
            print("Jug 1 is empty! Nothing to pour.")
        elif jug2 == jug2_capacity:
            print("Jug 2 is already full!")
        else:
            amount = min(jug1, jug2_capacity - jug2)
            jug1 -= amount
            jug2 += amount
            print("Water transferred:", amount, "litres.")

    # Pour Jug 2 into Jug 1
    elif choice == 6:
        if jug2 == 0:
            print("Jug 2 is empty! Nothing to pour.")
        elif jug1 == jug1_capacity:
            print("Jug 1 is already full!")
        else:
            amount = min(jug2, jug1_capacity - jug1)
            jug2 -= amount
            jug1 += amount
            print("Water transferred:", amount, "litres.")

    # Exit
    elif choice == 7:
        print("Program Ended.")
        break

    # Display updated state
    print("\nUpdated State:")
    print("Jug 1:", jug1, "/", jug1_capacity)
    print("Jug 2:", jug2, "/", jug2_capacity)
