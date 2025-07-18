def count_words_in_file(filename):
    word_counts = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in line)
                words = line.split()

                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1

        for word in sorted(word_counts):
            print(f"{word}: {word_counts[word]}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = input("Enter the name of the text file (with .txt extension): ")
count_words_in_file(file_name)