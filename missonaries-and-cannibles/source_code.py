
# Missionaries and Cannibals Problem

# Initially, everyone is on the left bank
left_m = 3
left_c = 3

right_m = 0
right_c = 0

# Boat starts on the left bank
boat = "Left"

while True:

    # Display current state
    print("\nCurrent State:")
    print("Left Bank  :", left_m, "Missionaries,", left_c, "Cannibals")
    print("Right Bank :", right_m, "Missionaries,", right_c, "Cannibals")
    print("Boat Position:", boat)

    # Check whether the goal is reached
    if right_m == 3 and right_c == 3:
        print("\nCongratulations! Everyone crossed safely.")
        break

    print("\nChoose passengers for the boat:")
    print("1. One Missionary")
    print("2. One Cannibal")
    print("3. Two Missionaries")
    print("4. Two Cannibals")
    print("5. One Missionary and One Cannibal")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Validate user input
    if not choice.isdigit() or int(choice) not in range(1, 7):
        print("Invalid choice! Select between 1 and 6.")
        continue

    choice = int(choice)

    if choice == 6:
        print("Program Ended.")
        break

    # Set the number of passengers
    if choice == 1:
        m, c = 1, 0
    elif choice == 2:
        m, c = 0, 1
    elif choice == 3:
        m, c = 2, 0
    elif choice == 4:
        m, c = 0, 2
    elif choice == 5:
        m, c = 1, 1

    # Check whether the passengers are available
    if boat == "Left":
        if m > left_m or c > left_c:
            print("Not enough people on the left bank!")
            continue

        # Move passengers to the right bank
        new_left_m = left_m - m
        new_left_c = left_c - c
        new_right_m = right_m + m
        new_right_c = right_c + c

    else:
        if m > right_m or c > right_c:
            print("Not enough people on the right bank!")
            continue

        # Move passengers to the left bank
        new_left_m = left_m + m
        new_left_c = left_c + c
        new_right_m = right_m - m
        new_right_c = right_c - c

    # Check the safety conditions
    if (new_left_m > 0 and new_left_c > new_left_m) or \
       (new_right_m > 0 and new_right_c > new_right_m):
        print("Invalid move! Cannibals would eat the missionaries.")
        continue

    # Update the state
    left_m = new_left_m
    left_c = new_left_c
    right_m = new_right_m
    right_c = new_right_c

    # Change the boat position
    if boat == "Left":
        boat = "Right"
    else:
        boat = "Left"

    print("\nMove completed successfully!")

    # Display updated state
    print("Updated State:")
    print("Left Bank  :", left_m, "Missionaries,", left_c, "Cannibals")
    print("Right Bank :", right_m, "Missionaries,", right_c, "Cannibals")
    print("Boat Position:", boat)
