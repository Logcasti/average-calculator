# Robust Average Calculator

This is an independent Python command-line utility designed to accurately calculate the average of a user-defined list of numbers, with a focus on robust error handling and enhanced usability.

## Key Features

* **Robust Input Validation:** Implements `try/except` blocks to manage non-numeric input and logical checks (`x <= 0`) to prevent program crashes.
* **Flexible Rounding:** Allows the user to choose custom rounding (whole number, tenth, hundredth, or not at all).
* **Continuous Execution:** Includes a main loop with a 'Start/Stop' option (E/S) for running multiple calculations without restarting the application.
* **Clean Architecture:** Core logic is encapsulated in a dedicated function for better separation of concerns.

## Technical Concepts Demonstrated (Learning Outcomes)

This project helped solidify understanding of essential Python principles:

1.  **Function Scope and Returns:** Mastering **Local** and **Global Variable Scope** to correctly retrieve calculated data using the `return` statement.
2.  **Tuple Unpacking:** Efficiently assigning multiple returned values from a function to distinct variables (e.g., `avg, r_avg = Average_Func(...)`).
3.  **Flow Control:** Effective use of nested `while` loops and the **`continue`** statement for reliable input prompting and continuous program flow.
4.  **Code Refactoring:** Improving function design by only returning necessary calculated values, leading to cleaner, more maintainable code.

##  How to Run the Program

1.  Ensure you have Python installed on your system.
2.  Run the script from your terminal:
    ```bash
    python Number Avg.py
    ```
3.  Follow the on-screen prompts for the number count, number inputs, and rounding choice.
