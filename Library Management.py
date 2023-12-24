class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AMAZING BOOKS AVAILABLE NOW: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"Sorry, '{bookname}' is not available at the moment. It's either taken by someone else. Please wait until it's returned.\n")
        else:
            track.append({name: bookname})
            print("📚 BOOK ISSUED! Thank you for borrowing. Take care of it and return it on time.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("🎉 BOOK RETURNED! Thank you! Hope you enjoyed reading it. \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("🎁 BOOK DONATED! Thank you for your generosity. Have an amazing day ahead!\n")
        self.books.append(bookname)


class Student:
    def requestBook(self):
        print("📚 Welcome to our library! Ready to explore new worlds?")
        self.book = input("Enter the title of the book you wish to borrow: ")
        return self.book

    def returnBook(self):
        print("🔙 Returning a book? Thank you for your visit!")
        name = input("Please provide your name: ")
        self.book = input("Enter the title of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("🎁 Generosity is contagious! Thank you for your donation!")
        self.book = input("Enter the title of the book you'd like to donate: ")
        return self.book


if __name__ == "__main__":
    Mdulibrary = Library([
        "The Catcher in the Rye", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Animal Farm",
        "Lord of the Flies", "Brave New World", "The Grapes of Wrath", "The Adventures of Huckleberry Finn", "Moby-Dick",
        "The Odyssey", "Frankenstein", "Dracula", "Jane Eyre", "Wuthering Heights", "Great Expectations", "The Picture of Dorian Gray",
        "Les Miserables", "Anna Karenina", "War and Peace", "Crime and Punishment", "The Brothers Karamazov", "Don Quixote",
        "One Hundred Years of Solitude", "The Name of the Rose", "The Count of Monte Cristo", "Gulliver's Travels", "The Canterbury Tales",
        "The Divine Comedy", "The Iliad", "The Aeneid", "The Prince", "The Republic", "The Wealth of Nations", "The Art of War",
        "Sapiens: A Brief History of Humankind", "The Origin of Species", "A Short History of Nearly Everything", "Thinking, Fast and Slow"
    ])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE MADURAI LIBRARY ♦♦♦♦♦♦♦\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. List all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Recommend a book\n7. Exit the library\n""")

    while True:
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                Mdulibrary.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                student_name = input("Enter your name: ")
                book_to_borrow = student.requestBook()
                Mdulibrary.borrowBook(student_name, book_to_borrow)
            elif usr_response == 3:  # return
                returned_book = student.returnBook()
                Mdulibrary.returnBook(returned_book)
            elif usr_response == 4:  # donate
                donated_book = student.donateBook()
                Mdulibrary.donateBook(donated_book)
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED! \n")
            elif usr_response == 6:  # recommend a book
                print("📚 Great! Tell us your interests, and we'll recommend a book!")
                print("Some book genres you might like: Fiction, Mystery, Science, History, Fantasy, Romance, Self-Help, etc.")
                recommendation = input("Enter your preferred book genre: ")
                print(f"We recommend 'The {recommendation} Chronicles'. Enjoy your read!\n")
                Mdulibrary.books.append(f"The {recommendation} Chronicles")
            elif usr_response == 7:  # exit
                print("THANK YOU! Have a great day!\n")
                exit()
            else:
                print("INVALID INPUT! Please try again.\n")
        except ValueError:
            print("INVALID INPUT! Please enter a valid number.\n")
        except Exception as e:
            print(f"{e} - INVALID INPUT! Please try again.\n")
