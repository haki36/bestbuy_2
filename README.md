🛍️ Store Manager CLI
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Bootcamp](https://img.shields.io/badge/Masterschool-Bootcamp-orange)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)
> A small **store manager CLI** built with **Python + OOP**.
> The application allows users to manage store inventory,
> display available products, calculate stock totals,
> and place simple customer orders through the terminal.
---
📌 Overview
This project demonstrates how to:
Build an interactive CLI application
Model products and store logic with classes and objects
Separate business logic from application flow
Validate user input and stock values
Manage active and inactive products
Process orders and calculate total payment
Structure a Python project into multiple modules
The project architecture separates user interaction from
product and store management logic.
    User Input (CLI Menu)
          │
          ▼
        main.py
          │
          ▼
      store.py
          │
          ▼
     products.py
          │
          ▼
Terminal Output / Order Result
---
🖥️ Demo Flow
User starts the program
A menu is displayed
User selects an option
The selected action is executed
Results are printed in the terminal
Orders update product stock automatically
Example:
```bash
python main.py
```
```text
Menu:
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```
---
✨ Core Features
Product inventory management with OOP
List all active products in the store
Show total quantity of all products
Make customer orders directly in the terminal
Automatically reduce stock after purchase
Deactivate products when quantity reaches zero
Input validation for invalid menu choices and purchase amounts
Clean separation of responsibilities across modules
---
📂 Project Structure
```text
store-manager-cli/
│
├── main.py         # CLI menu and user interaction
├── products.py     # Product class
├── store.py        # Store class and order handling
└── README.md
```
---
🚀 Installation & Usage
Requirements
Python 3.10+
No external dependencies are required for this project.
---
Run the Program
```bash
python main.py
```
---
🧾 Example Products
The store is initialized with these sample products:
MacBook Air M2
Bose QuietComfort Earbuds
Google Pixel 7
Each product includes:
name
price
quantity
active / inactive status
---
🛒 Order Flow
When the user chooses the order option:
Active products are displayed
The user selects a product number
The user enters the quantity
The product is added to the shopping list
The total payment is calculated
Product quantities are updated
Example:
```text
Which product # do you want? 1
What amount do you want? 2
Product added to list!
```
---
🧠 Technical Concepts Applied
Concept	Implementation
CLI interaction	`input()` + menu loop
OOP	`Product` and `Store` classes
Encapsulation of logic	methods like `buy()`, `order()`, `get_all_products()`
Validation	price, quantity, user input, stock checks
Modular structure	`main.py`, `products.py`, `store.py`
State management	active / inactive products
Exception handling	`try/except ValueError`
---
🎓 Learning Objectives
This exercise practices:
Structuring Python projects
Working with classes and objects
Separating concerns across modules
Validating data with custom logic
Handling stock management
Building terminal-based applications
Using exceptions for safe program flow
---
📈 Portfolio Upgrade Ideas
Possible improvements:
Add special product types such as limited or non-stocked products
Add product categories
Add discount support
Add unit tests
Add logging
Save products to JSON or SQLite
Add admin functions to insert or remove products dynamically
Convert the project into a Flask or FastAPI web app
---
🇩🇪 Kurzbeschreibung
Ein Python-CLI-Projekt zur Verwaltung eines kleinen Shopsystems.
Die Anwendung basiert auf OOP mit Klassen und Objekten und erlaubt das
Anzeigen aktiver Produkte, das Berechnen des gesamten Lagerbestands
sowie das Ausführen von Bestellungen direkt im Terminal.
Die Produkt- und Store-Logik sind sauber voneinander getrennt, sodass
das Projekt eine gute Übung für Objektorientierung, Modularisierung
und Eingabevalidierung ist.
---
📄 License
MIT License
---
👤 Author
Hakan Yildirim  
Python Software Developer (AI Track)  
Masterschool Bootcamp
GitHub: https://github.com/haki36  
LinkedIn: https://linkedin.com/in/hakan-yildirim-tech