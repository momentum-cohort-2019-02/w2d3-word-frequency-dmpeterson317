import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def normalize_text(text):
    """given a text, lowercases it, removes all punctuation, and replaces all whitespace with normal spaces. Multiple whitespace will be compressed into a single space"""
    
    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char
        
    text = new_text
    text = text.replace("\n", " ")
    return text

def print_word_freq(filename):
    """Read in `filename` and print out the frequency of words in that file."""
    # with statement will auto close the file
    # i.e. file.close()
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    
    word_freq = {}
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            if word in word_freq:
                word_freq[word] += 1 
            else:
                word_freq[word] = 1
    
    sorted_words = sorted(word_freq.items(), key=lambda most_used: most_used[1], reverse=True)
    # sorted() gives me a List of Tuples, calling the temporary function 'most_used()'
    # to sort my list based on the second element of the tuple... in reverse order)
    i = 0
    while i < 10:
    # for item in sorted_words:
        print(f"{sorted_words[i][0]} | {sorted_words[i][1]} {'*' * sorted_words[i][1]}")
        i += 1
    # for word, freq in word_freq.items():
    #     print(word, "|", freq, "*" * freq)
        # for n in freq:
        #     print('*',)
        # print('\n')

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    # file = Path("seneca_falls.txt")
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
