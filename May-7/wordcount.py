def count_word_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read().lower()
            words = text.split()
            word_freq = {}
            for word in words:
                word = word.strip('.,!?"\'')
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
            return word_freq
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    file_name = input("Enter the file path: ")
    word_freq = count_word_frequency(file_name)
    if word_freq:
        print("Word Frequency:")
        for word, freq in word_freq.items():
            print(f"{word}: {freq}")

if __name__ == "__main__":
    main()

