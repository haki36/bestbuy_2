🛍️ Store Manager CLI
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Bootcamp](https://img.shields.io/badge/Masterschool-Bootcamp-orange)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)
> A modular **store management CLI** built with **Python and Object-Oriented Programming (OOP)**.  
> The application simulates a real-world retail system with support for inventory management, order processing, product variations, and promotional pricing strategies.
---
📌 Overview
This project demonstrates how to:
Build an interactive Command Line Interface (CLI)
Design scalable systems using OOP principles
Apply inheritance and polymorphism for product variations
Implement business logic separation
Integrate promotion strategies (discounts)
Validate user input and handle errors gracefully
Architecture
```text
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
  promotions.py
        │
        ▼
Terminal Output / Order Processing
```
---
🖥️ Demo Flow
Start the application
Choose an action from the menu
Interact with the store (list, order, etc.)
System processes logic and updates stock
Results are displayed in the terminal
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
🛒 Store Functionality
Display all active products
Calculate total inventory quantity
Create and process customer orders
Automatic stock updates after purchase
Input validation and error handling
📦 Product System (OOP)
Base `Product` class
`NonStockedProduct` for unlimited items such as software licenses
`LimitedProduct` for products with a maximum quantity per order
🎯 Promotion System
Abstract `Promotion` class
Supported promotions:
Percentage discount
Second item half price
Buy 2 get 1 free
Promotions can be assigned dynamically to products
🧠 Advanced OOP Concepts
Inheritance
Polymorphism
Encapsulation
Abstract classes
Strategy Pattern for pricing logic
---
📂 Project Structure
```text
store-manager-cli/
│
├── main.py         # CLI menu & user interaction
├── products.py     # Product classes (base + variations)
├── store.py        # Store logic and order processing
├── promotions.py   # Promotion strategy classes
├── test_product.py # Unit tests for Product
└── README.md
```
---
🚀 Installation & Usage
Requirements
Python 3.10+
Run the application
```bash
python main.py
```
Run the tests
```bash
pytest
```
or only:
```bash
pytest test_product.py
```
---
🧾 Example Products
The store is initialized with:
MacBook Air M2
Bose QuietComfort Earbuds
Google Pixel 7
Windows License (`NonStockedProduct`)
Shipping (`LimitedProduct`)
Each product includes:
Name
Price
Quantity or product type
Status (`active` / `inactive`)
Optional promotion
---
🛒 Order Example
```text
Which product # do you want? 1
What amount do you want? 2
Product added to list!

Order made! Total payment: $2175.00
```
---
🧠 Technical Concepts Applied
Concept	Implementation
CLI interaction	`input()` + menu loop
OOP	`Product`, `Store`, subclasses
Inheritance	`NonStockedProduct`, `LimitedProduct`
Polymorphism	`buy()` and promotion handling
Strategy Pattern	promotion system
Validation	input, stock, quantity, limits
Exception Handling	`ValueError`
Modular Design	separate Python modules
---
🎓 Learning Objectives
This project focuses on:
Structuring Python applications
Writing reusable and scalable OOP code
Designing flexible business logic
Implementing store and inventory scenarios
Working with inheritance and abstract classes
Building maintainable CLI applications
---
📈 Portfolio Upgrade Ideas
Possible improvements:
Add database support with SQLite or PostgreSQL
Build a REST API with Flask or FastAPI
Add a GUI with Tkinter
Add logging
Add admin functionality for managing products
Add more unit tests for `Store` and promotions
Support multiple promotions per product as an advanced feature
---
🇩🇪 Kurzbeschreibung
Ein CLI-basiertes Shopsystem in Python mit Fokus auf Objektorientierung und sauberer Architektur.
Die Anwendung unterstützt:
Produktverwaltung
Bestellprozesse
verschiedene Produkttypen
Rabatt- und Aktionssysteme
Das Projekt demonstriert fortgeschrittene OOP-Konzepte wie Vererbung, Polymorphismus, abstrakte Klassen und das Strategy Pattern.
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