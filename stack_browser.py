# Stack to store visited pages
history = []

def visit_page(page):
    history.append(page)  # Push page onto the stack
    print(f"Visited: {page}")

def go_back():
    if not history:
        print("No pages in history.")
        return

    last_page = history.pop()  # Pop the last visited page
    print(f"Going back from: {last_page}")

    if history:
        print(f"Current page: {history[-1]}")
    else:
        print("No pages left in history.")

def show_history():
    if not history:
        print("History is empty.")
    else:
        print("History:", " -> ".join(history))

# ---------------- Menu ----------------
while True:
    print("\n1. Visit Page")
    print("2. Back")
    print("3. Show History")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        page = input("Enter page name: ")
        visit_page(page)
    elif choice == "2":
        go_back()
    elif choice == "3":
        show_history()
    elif choice == "4":
        print("Exiting browser simulation.")
        break
    else:
        print("Invalid choice.")
