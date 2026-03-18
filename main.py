from products import Product
from store import Store

def init_store():
    """Create and return a store with the initial stock of products."""
    try:
        product_list = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250)
        ]
        best_buy = Store(product_list)
        return best_buy
    except ValueError as e:
        print(f"Store initialization failed: {e}")
        raise SystemExit


def list_all_products(store):
    """Display all active products currently available in the store."""
    print("-" * 10)
    product_list = store.get_all_products()
    counter = 1
    for product in product_list:
        print(f"{counter}. ", end="")
        product.show()
        counter += 1
    print("-" * 10)
    print()


def show_total_amount(store):
    """Display the total quantity of all products in the store."""
    total_amount = store.get_total_quantity()
    print(f"Total amount in store: {total_amount}")
    print()


def make_order(store):
    """Let the user create an order and print the total payment."""
    shopping_list = []
    active_products = store.get_all_products()

    if len(active_products) == 0:
        print("Shop is empty. No order is possible!")
        print()
        return

    list_all_products(store)
    print("When you want to finish order, enter empty text.")

    while True:
        product_choice = input("Which product # do you want? ").strip()
        if product_choice == "":
            break

        product_quantity = input("What amount do you want? ").strip()
        if product_quantity == "":
            break

        try:
            product_choice = int(product_choice)
            product_quantity = int(product_quantity)

            if product_choice < 1 or product_choice > len(active_products):
                print("Invalid product number!\n")
                continue

            if product_quantity <= 0:
                print("Quantity must be greater than 0!\n")
                continue

            product = active_products[product_choice - 1]
            shopping_list.append((product, product_quantity))

            print("Product added to list!\n")
        except ValueError:
            print("Please enter valid numbers!\n")

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print("*" * 8)
            print(f"\nOrder made! Total payment: ${total_cost:.2f}")
            print()
        except ValueError as e:
            print(f"Order failed: {e}")
            print()


def quit_program(store):
    """Exit the program."""
    raise SystemExit


def show_menu_and_get_input():
    """
    Display the menu and return the selected function.
    Keeps asking the user until a valid menu option is entered.
    """
    print("Menu:")
    for key, value in FUNCTIONS.items():
        print(f"{key}. {value[1]}")

    while True:
        try:
            choice = int(input("Please choose a number: "))
            if choice in FUNCTIONS:
                return FUNCTIONS[choice][0]
            print("Try again...")
        except ValueError:
            print("Try again...")

FUNCTIONS = { 1: (list_all_products, "List all products in store"),
              2: (show_total_amount, "Show total amount in store"),
              3: (make_order, "Make an order"),
              4: (quit_program, "Quit")
             }


def main():
    """Run the store menu loop."""
    store = init_store()
    while True:
        choice_func = show_menu_and_get_input()
        choice_func(store)

if __name__ == '__main__':
    main()
