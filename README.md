# Expense Tracker CLI

A simple command-line based Expense Tracker built using Python. This project allows users to manage daily expenses by adding, viewing, deleting, and calculating total spending, with data stored persistently using a JSON file.

---

## Features

* Add a new expense with name and amount
* View all recorded expenses
* Calculate total spending
* Delete an expense
* Persistent storage using JSON (data saved between runs)

---

## Tech Stack

This project is built using:

* **Python**
* **File I/O** (for reading and writing data)
* **JSON** (for structured data storage)
* **Classes (OOP)** for organizing logic
* **os module** (for file handling)
* **sys module** (for program control)

---

## Project Structure

```
expense-tracker/
│
├── main.py              # Main application file
├── .gitignore           # Ignored files
└── README.md            # Project documentation
```

---

## How It Works

* The program stores all expenses in a JSON file.
* When the app starts, it loads existing data (if available).
* Users interact with a menu-driven CLI to manage expenses.
* All changes are saved automatically.

Example structure of stored data:

```json
[
  {"name": "Food", "amount": 120},
  {"name": "Transport", "amount": 50}
]
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/expense-tracker.git
```

2. Navigate to the project folder:

```bash
cd expense-tracker
```

3. Run the program:

```bash
python main.py
```

---
## Example Usage

Enter expense name: Food  
Enter amount: 120  

Food - ₹120  
Total spending: ₹120

---

## Learning Outcomes

Through this project, I practiced:

* Working with **file handling and error handling in Python** 
* Using **JSON for data persistence**
* Applying **Object-Oriented Programming (OOP)**
* Building a **menu-driven CLI application**
* Managing files using the **os module**

---

## Author
Shubh Thadani

---

## Note

The `data.json` file is ignored to avoid storing personal expense data.
