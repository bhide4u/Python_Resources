# Separation of Concerns

# Separation of concerns is a design principle that advocates for dividing a software system into distinct sections or modules, each responsible for a specific aspect or concern of the system. 
# The goal is to keep different concerns separated, reducing complexity and making the code easier to understand, maintain, and modify.

# In Python, you can achieve separation of concerns by organizing your code into modules, classes, and functions that handle specific tasks or responsibilities. 

# Here's an example to illustrate the concept:

# Let's say we are developing a web application for a bookstore. We can separate the concerns into different modules as follows:

# 1. book.py: This module handles the book-related operations, such as creating book objects and performing book-related calculations.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_discounted_price(self, discount):
        return self.price * (1 - discount)

# 2. order.py: This module focuses on handling the order-related functionality, such as creating order objects, calculating the total price, and applying discounts.

from book import Book

class Order:
    def __init__(self, books):
        self.books = books

    def calculate_total_price(self):
        total = 0
        for book in self.books:
            total += book.price
        return total

    def apply_discount(self, discount):
        for book in self.books:
            book.price = book.get_discounted_price(discount)

# 3. app.py: This module serves as the entry point of our application. It brings everything together, creates book and order objects, and performs operations.

from book import Book
from order import Order

# Create book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12)

# Create an order
order = Order([book1, book2])

# Calculate and print the total price
total_price = order.calculate_total_price()
print("Total price:", total_price)

# Apply a discount and recalculate the total price
order.apply_discount(0.1)
total_price_with_discount = order.calculate_total_price()
print("Total price with discount:", total_price_with_discount)

# By separating the concerns into different modules ('book.py', 'order.py') and keeping each module focused on its specific functionality, we achieve a cleaner and more maintainable codebase. The 'app.py' module acts as a higher-level component that orchestrates the interactions between the book and order modules.

# Separation of concerns allows for easier modification and extension of individual modules without affecting other parts of the system. It improves code reusability, testability, and overall code organization.