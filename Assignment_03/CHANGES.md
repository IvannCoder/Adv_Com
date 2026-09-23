# Assignment 03 — CHANGES

**Name:** Hein Thura Naung  **Student ID:** 6705140056

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Bare tuples for products like `("Laptop", 1200.0, "electronics")` | Created a `Product` class and an `OrderItem` class linking product and quantity | Domain Modeling & Composition | Ran `py Assignment_03.py` → PASS |
| 2 | Loose magic numbers scattered around (`0.07`, `100.0`, `10`) | Named constants at the top (`TAX_RATE`, `DISCOUNT_THRESHOLD`, etc.) | Clean Code / Maintainability | Ran `py Assignment_03.py` → PASS |
| 3 | No validation on item quantities during creation | Added a check in `OrderItem.__init__` to raise `ValueError` if quantity < 1 | Encapsulation & State Validation | Ran `py Assignment_03.py` → PASS |
| 4 | Long `if/elif` chains checking the customer tier for discounts and points | A base `Customer` class with subclasses (`SilverCustomer`, `GoldCustomer`, etc.) using polymorphism | Inheritance & Polymorphism | Ran `py Assignment_03.py` → PASS |
| 5 | Mixed math and printing inside the legacy `calc` function | Pure calculation methods that return numbers only, separated from the `build_receipt` string builder | Pure Functions vs. I/O Separation | Ran `py Assignment_03.py` → PASS |

## 2 · Short reflection (4–6 sentences)

Replacing the long customer tier `if/elif` conditions with different customer classes made the code easier for me to understand and manage. I learned that when different types of customers have different rules, it is better to let each class handle its own behavior instead of putting everything into one long condition. I also learned that keeping the output exactly the same is important when refactoring because even small changes in spaces or line breaks can affect the result. Separating the calculation methods from the receipt printing also made the code easier to test and understand. Overall, this refactoring helped me see that good object-oriented design is not only about making code look more organized, but also about making the code easier to understand, change, and maintain.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Can you explain why refactoring is important and assist me step-by-step to refactor this code without doing everything for me? Just guide me and explain the concepts." | Explained the core goals of refactoring (improving design without changing behavior) and set up a step-by-step coaching workflow for the assignment. | Accepted | Read through the principles to understand what constraints to keep in mind before writing code. |
| 2 | "How can I structure the Product and OrderItem classes with composition and constructor validation?" | Suggested basic classes with `__init__` validation for `quantity < 1`. | Accepted | Checked that invalid quantities raise errors and script runs cleanly |
| 3 | "How do I make the Order methods return pure numbers instead of printing, while still keeping a separate function for the receipt output?" | Suggested splitting the math into individual methods like `calculate_subtotal()` and handling the string formatting separately in `build_receipt()`. | Accepted | Verified that calculations returned clean numbers and printed output stayed identical |
| 4 | "Help me refactor the tier `if/elif` chains into a polymorphic class family." | Suggested a base `Customer` class with subclasses and a dictionary mapping approach. | Edited | Verified that calculated points and discounts matched the original logic |
| 5 | "Why did my self-test fail on line 12 with a blank line difference?" | Pointed out the exact trailing newline and spacing needed in the receipt builder. | Accepted | Added the extra newline, re-ran the self-test, and got PASS |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
