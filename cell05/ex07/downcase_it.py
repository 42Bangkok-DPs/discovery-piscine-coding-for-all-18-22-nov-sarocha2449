import sys

def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(text.lower())
    elif len(sys.argv) <= 1:
        print("none")
    else:
        text = sys.stdin.read()
        print(text.lower())
if __name__ == "__main__":
    main()