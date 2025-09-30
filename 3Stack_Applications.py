def reverse_string(s: str) -> str:
    stack = list(s)
    reversed_list = []
    while stack:
        reversed_list.append(stack.pop())
    return "".join(reversed_list)

def check_balanced_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["} 

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
                
    return not stack

def simple_text_editor():
    text_stack = []

    print("\n--- Simple Text Editor (Type and Undo) ---")
    print("Commands: 'TYPE <text>', 'UNDO', 'EXIT'")

    while True:
        current_text = "".join(text_stack)
        print(f"\n[TEXT: '{current_text}']")
        
        user_input_raw = input("Enter command: ").strip()
        user_command_lower = user_input_raw.lower() 

        if user_command_lower.startswith("type "):
            new_chars = user_input_raw[5:]
            for char in new_chars:
                text_stack.append(char)
            print(f"Typed: '{new_chars}'")

        elif user_command_lower == "undo":
            if text_stack:
                text_stack.pop()
                print("Undo successful.")
            else:
                print("Nothing to undo.")

        elif user_command_lower == "exit":
            print(f"Final text: '{current_text}'")
            print("Exiting editor.")
            break
            
        else:
            print("Invalid command.")

def main_menu():
    while True:
        print("\n=== STACK APPLICATIONS ===")
        print("1. Reverse String")
        print("2. Check Balanced Parentheses")
        print("3. Simple Text Editor (Undo)")
        print("4. Exit")
        print("==========================")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            s = input("Enter a string to reverse: ")
            result = reverse_string(s)
            print(f"Original: '{s}' | Reversed: '{result}'")

        elif choice == '2':
            s = input("Enter an expression (e.g., '({[]})'): ")
            result = check_balanced_parentheses(s)
            print(f"Expression: '{s}' | Balanced: {result}")

        elif choice == '3':
            simple_text_editor()
            
        elif choice == '4':
            print("Program closed.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()