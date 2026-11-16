# main.py
from models import Book, Member,Magazine,DVD  # TODO: also import Magazine, DVD#
 #book = Book("Python 101", 1, "A. Rao")
book=Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, "John", 10)
dvd = DVD("Python Course", 3, "Mike", 1, 120)
# TODO: create one Magazine and one DVD
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)
# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)
try:
    bob.borrow(magazine)   # Bob's first item

    bob.borrow(dvd)        # should fail because max_items = 1

except ValueError as e:
    print("Could not borrow:", e)
try:
    alice.return_item(dvd)   # Alice never borrowed DVD

except ValueError as e:
    print("Could not return:", e)
# 3. Polymorphism: one loop, no type checks
items = [book,magazine,dvd]  # TODO: add the magazine and the DVD
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)
