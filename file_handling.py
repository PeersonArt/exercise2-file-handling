# Exercise 2: File Handling

try:
    note = input("Enter a short note/message: ")
    with open("notes.txt", "w") as file:
        file.write(note + "\n")

    with open("notes.txt", "r") as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)

    new_note = input("Enter another note: ")
    with open("notes.txt", "a") as file:
        file.write(new_note + "\n")

    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print("\n--- Updated Content ---")
        print(updated_content)

except FileNotFoundError:
    print("Error: notes.txt not found.")
except Exception as e:
    print("An error occurred:", e)