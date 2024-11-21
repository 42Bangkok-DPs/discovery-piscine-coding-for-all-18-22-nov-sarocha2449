import sys

def main():
    args = sys.argv[1:]
    
    if not args:
        print("none")
        return

    if len(args) == 2:
        try:
            start = int(args[0])
            end = int(args[1])
            result = list(range(start, end + 1))
            print(result)
        except ValueError:
            print("Invalid input: please provide two integers.")
    else:
        print("Invalid input: please provide exactly two arguments.")

if __name__ == "__main__":
    main()
