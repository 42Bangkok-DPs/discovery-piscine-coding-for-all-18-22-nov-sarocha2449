import sys

def main():
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        input_text = sys.stdin.read()
    print(input_text.upper())
if __name__ == "__main__":
    main()