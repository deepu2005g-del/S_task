# Task 6: Word Count Tool

from collections import Counter

def word_count_tool():
    try:
        filename = input("Enter file name: ").strip()

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print("File not found")
            return
        except PermissionError:
            print("Permission denied")
            return

        lines = text.splitlines()
        words = text.split()
        chars = len(text)

        print("\nFile Analysis:")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {chars}")

        try:
            clean_words = [word.lower().strip(".,!?;:\"'()[]") for word in words]
            freq = Counter(clean_words)

            print("\nTop 10 Words:")
            for word, count in freq.most_common(10):
                print(f"{word}: {count}")

        except Exception as e:
            print("Frequency Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

if __name__ == "__main__":
    word_count_tool()