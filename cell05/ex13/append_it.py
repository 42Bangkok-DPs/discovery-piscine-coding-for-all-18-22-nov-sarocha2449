import sys

def main():
    args = sys.argv[1:]
    
    if not args:
        print("none")
        return
    for word in args:
        if word.endswith(('l', 'n')):
            print(f"{word}ism")
            
if __name__ == "__main__":
    main()
