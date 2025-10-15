# Robust Average Calculator (v2.0)

This is an independent Python command-line utility designed to accurately calculate the average of a user-defined list of numbers, with a focus on robust error handling and enhanced usability.

## Key Features

* **Architectural Rounding Choice:** Provides users with a choice between two industry-standard rounding algorithms: **Banker's Rounding** (Python's default) and **Half-Up Rounding** (The mathematically common method).
* **Targeted Computational Accuracy:** Implemented a custom solution within the **Half-Up Rounding** logic using a **`Tolerance` value** to correct for the inherent imprecision of floating-point arithmetic when encountering half-way (`.X5`) values.
* **Robust Input Validation:** Implements `try/except` blocks to manage non-numeric input and logical checks (`x <= 0`) to prevent program crashes.
* **Flexible Rounding:** Allows the user to choose custom rounding (whole number, tenth, hundredth, or not at all).
* **Continuous Execution:** Includes a main loop with a 'Start/Stop' option (E/S) for running multiple calculations without restarting the application.
* **Clean Architecture:** Core logic is encapsulated in dedicated functions (`Half_Up()` and `Bank_Rounding()`) for better **separation of concerns** and **modularity**.

## What I learned (Technical Mastery)

This project helped solidify understanding of essential Python principles and software design:

1.  **Function Abstraction and Scope:** Mastering **Local** and **Global Variable Scope** to correctly retrieve calculated data using the `return` statement, including the abstraction of core logic into distinct functions.
2.  **Tuple Unpacking:** Efficiently assigning multiple returned values from a function to distinct variables (e.g., `avg, r_avg = Average_Func(...)`).
3.  **Complex Flow Control:** Effective use of **nested `while` loops** and the **`continue`** statement for reliable input prompting, application state management, and continuous program flow.
4.  **Code Refactoring:** Improving function design by only returning necessary calculated values, leading to cleaner, more maintainable code.
5.  **Advanced Flow Control:** **Incorporated nested loops** to precisely control program flow using **`break`** and **`continue`** for guaranteed input count and reliable application state transitions.
6.  **Low-Level Debugging:** Gained practical experience in debugging and engineering a precise workaround for **floating-point precision errors** specific to the half-up rounding check using a $\text{Tolerance}$ value.
7.  **Domain-Specific Logic:** Understood and implemented two different **industry-standard mathematical protocols** (Banker's vs. Half-Up Rounding) based on specific computational requirements.

## How to Run the Program

1.  Run from Bash
2.  Run in File Explorer
3.  Run in an IDLE
