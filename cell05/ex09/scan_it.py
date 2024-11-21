import sys

def count_word_occurrences(word, text):
    return text.split().count(word)

def main():
    if len(sys.argv) < 2:
        print("none")
        return
    
    target_word = sys.argv[1]
    
    if len(sys.argv) > 2:
        text = sys.argv[2]
    else:
        print("none")
        return

    count = count_word_occurrences(target_word, text)

    print(count)

if __name__ == "__main__":
    main()
