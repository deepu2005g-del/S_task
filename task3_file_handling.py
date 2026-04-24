# Task 3: File Handling Program

def file_operations():
    try:
        filename = input("Enter file name: ").strip()

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                print("\nFile Content:\n")
                print(content)

        except FileNotFoundError:
            print("File not found! Creating new file...")
            content = ""

        find_word = input("Enter word to find: ").strip()
        replace_word = input("Enter word to replace with: ").strip()

        if not find_word:
            raise ValueError("Find word cannot be empty")

        if find_word not in content:
            print(f"The word '{find_word}' was NOT found in the file.")
            return

        count = content.count(find_word)

        updated_content = content.replace(find_word, replace_word)

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"Replacement successful! '{find_word}' replaced {count} time(s).")

        except PermissionError:
            print("Permission denied to write file.")
        except Exception as e:
            print("Write Error:", e)

    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)

if __name__ == "__main__":
    file_operations()