import sys
EXPECTED_PARAMETER = "Hello"

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    print(f"What was the parameter? {user_input}")
    if user_input == EXPECTED_PARAMETER:
        print("Good job!")
    else:
        print("Nope, sorry...")

else:
    print("What was the parameter?")
    user_input = input()
    if user_input == EXPECTED_PARAMETER:
        print("Good job!")
    else:
        print("Nope, sorry...")
