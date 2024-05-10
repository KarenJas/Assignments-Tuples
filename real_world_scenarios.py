#2. Python Data Structure Challenges in Real-World Scenarios

#Function to add books to any library
def add_book_to_library(library, title, author):
    #Make new tuple for new book
    new_book = (title, author)
    #Check for duplicates in library
    if new_book not in library:
        #Append new book to library
        library.append(new_book)
        #Inform user that the book has been added
        print("Book added successfully!")
    else:
        #Inform user if book is a duplicate
        print("This book already exists in the library.")

#Test
#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#add_book_to_library(library, "To Kill a Mockingbird", "Harper Lee")
#add_book_to_library(library, "1984", "George Orwell") 
