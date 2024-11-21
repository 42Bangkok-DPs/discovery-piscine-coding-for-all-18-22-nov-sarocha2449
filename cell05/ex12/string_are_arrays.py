import sys

def main():
    args = sys.argv[1:]
    
    if not args:
        print("none")
        return
    input_string = " ".join(args)
    z_chars = [char for char in input_string if char.lower() == 'z']
    
    if z_chars:
        print("".join(z_chars))
    else:
        print("none")

if __name__ == "__main__":
    main()
