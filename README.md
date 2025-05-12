🧮 Infix Expression Calculator using Python, PyQt, and Stack-Based Evaluation
This is a GUI-based calculator application built with Python and PyQt, capable of evaluating complex infix mathematical expressions with full support for operator precedence, parentheses, and unary operations.

The core of the calculator uses a custom stack-based expression parser that implements BODMAS/PEMDAS logic to correctly evaluate the order of operations. It also differentiates between positive and negative numbers, handles unary minus (e.g., -5 + 3), and supports nested parentheses and exponentiation.

✨ Features
✅ Infix expression parsing (e.g., 3 + 4 * (2 - 1)^2)

✅ Full BODMAS support (brackets, orders, division, multiplication, addition, subtraction)

✅ Handles unary minus and negative numbers correctly

✅ Supports exponentiation (^)

✅ Clean and intuitive PyQt GUI

✅ Real-time input and output display

🛠️ Technologies Used
Python – Core logic and scripting

PyQt5/PyQt6 – GUI design and event handling

Stack-based Evaluation Algorithm – For parsing and calculating expressions

🚀 Usage
You can enter any valid mathematical expression using the GUI, including:
-3 + 4 * 2 / (1 - 5)^2
(2 + 3) * (4 - 2)^3
The calculator will evaluate and display the result instantly using the internal expression engine.
