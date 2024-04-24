import tkinter as tk

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class RereadApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Reread - Used Bookstore")
        
        # Create a list of sample books
        self.library = [
            Book("To Kill a Mockingbird", "Harper Lee", 10.99),
            Book("1984", "George Orwell", 8.99),
            Book("The Catcher in the Rye", "J.D. Salinger", 7.99),
            Book("Pride and Prejudice", "Jane Austen", 9.99),
            Book("The Great Gatsby", "F. Scott Fitzgerald", 11.99)
        ]
        
        # Create a frame to hold the library
        self.library_frame = tk.Frame(self.master)
        self.library_frame.pack(padx=10, pady=10)
        
        # Create labels for each book in the library
        for i, book in enumerate(self.library):
            book_label = tk.Label(self.library_frame, text=f"{book.title} by {book.author} - ${book.price:.2f}")
            book_label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            
            add_to_cart_button = tk.Button(self.library_frame, text="Add to Cart", command=lambda idx=i: self.add_to_cart(idx))
            add_to_cart_button.grid(row=i, column=1, padx=5, pady=5)

    def add_to_cart(self, idx):
        selected_book = self.library[idx]
        print(f"Added '{selected_book.title}' to cart!")

def main():
    root = tk.Tk()
    app = RereadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

