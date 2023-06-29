import tkinter as tk
from tkinter import messagebox
import random

class BookClub:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Club Pairing")

        self.members = ['Gregory', 'Alyxandria', 'Markeith', 'Sarah', 'Valerie',
                        'Jessica', 'Nick', 'Eric', 'Harmony', 'Liz',
                        'Jordan', 'member12']

        self.books = {
            'How To Sell a Haunted House': ('Grady Hendrix', 'halloween'),
            'Tell Me Im Worthless': ('Alison Rumfitt', 'halloween'),
            'Dont Fear The Reaper': ('Graham Jones', 'halloween'),
            'Our Share of Night': ('Mariana Enriquez', 'halloween'),
            'The Spite House': ('Johnny Compton', 'halloween'),
            'The God of Endings': ('Jacqueline Holland', 'halloween'),
            'Pinata': ('Leopoldo Gout', 'halloween'),
            'Abnormal Statistics': ('Max Booth III', 'halloween'),
            'Lone Women': ('Victor LaValle', 'halloween'),
            'The Marigold': ('Andrew F Sullivan', 'halloween'),
            'All I Want For Christmas': ('Maggie knox', 'christmas'),
            'Always In December': ('Emily Stone', 'christmas'),
            'The Christmas Bookshop': ('Jenny Colgan', 'christmas'),
            'The Christmas Wish': ('Lindsey Kelk', 'christmas'),
            'Absent In The Spring': ('Agatha Christie', 'spring'),
            'An American in Provence': ('Jamie Beck', 'spring'),
            'You Are Badass': ('Jen Sincero', 'self help'),
            'The Subtle Art Of Not Giving A Fuck': ('Mark Madison', 'self help'),
            'A Long Time Coming': ('Meghan Quinn', 'romance'),
            'Not A Happy Family': ('Shari Lapena', 'mystery')
        }

        self.genre_books = {
            'halloween': [],
            'christmas': [],
            'spring': [],
            'self help': [],
            'romance': [],
            'mystery': []
        }

        for book, (author, genre) in self.books.items():
            self.genre_books[genre].append(book)

        self.pair_button = tk.Button(self.master, text="Pair Member with Random Book", command=self.pair)
        self.pair_button.pack()

        self.pair_halloween_button = tk.Button(self.master, text="Pair Member with Halloween Book",
                                           command=lambda: self.pair('halloween'))
        self.pair_halloween_button.pack()

        self.pair_christmas_button = tk.Button(self.master, text="Pair Member with Christmas Book",
                                           command=lambda: self.pair('christmas'))
        self.pair_christmas_button.pack()

    def pair(self, genre=None):
        member = random.choice(self.members)
        if genre:
            book = random.choice(self.genre_books[genre])
        else:
            book = random.choice(list(self.books.keys()))

        author, _ = self.books[book]
        messagebox.showinfo("Pairing", f"{member} is paired with the book {book} by {author}")


root = tk.Tk()
app = BookClub(root)
root.mainloop()
