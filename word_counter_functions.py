"""Word Counter Program"""

def get_sentence_input() -> str:
    """Prompts the user to enter a sentence and returns it as a string."""
    return input("Enter a sentence: ").strip()


def count_words(sentence: str) -> int:
    """Counts and returns the number of words in a given sentence."""
    words = sentence.split()  # Splits the sentence by whitespace
    return len(words)


def main():
    """Main function to execute the program."""
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} word{'s' if word_count != 1 else ''}.")


if __name__ == "__main__":
    main()
