import sys
def main():
    if len(sys.argv) > 1:
        word = " ".join(sys.argv[1:])
        print(word.upper())
    elif len(sys.argv) <= 1:
        print("none")
    else:
        word = sys.stdin.read()
        print(word.upper())
if __name__ == "__main__":
    main()