def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()

    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(path_to_file, word_count, char_count):
    print(f"*****BEGIN REPORT OF {path_to_file}******")
    print(f"{word_count} WORDS FOUND IN DOCUMENT")

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("***** END REPORT *****")

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file, "r") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print_report(path_to_file, word_count, char_count)

if __name__ == "__main__":
    main()