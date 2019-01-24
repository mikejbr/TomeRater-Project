
#This is Codeacademy capstone project TomeRater.  This project creates code that allows to users to read and rate books, as well as analyzes the resulting objects.
#Developer: Michael Brown
#Version: 1.0
#Start Date: 1/20/2019
#Finish Date: 1/24/2019

#Creating a User Class:

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    
    #Define base methods for User Class
    def get_email(self):
        return self.email
    
    def change_email(self, email):
        self.email = email
        return self.email
    
    def __repr__(self):
        book_count = 0
        for book in self.books.values():
            book_count += 1
        return "User {name}, email: {email}, books read: {count}".format(name = self.name, email = self.email, count = book_count)
    
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
    
    #Define advanced methods for User Class
    def read_book(self, book, rating = None):
        self.book = book
        self.rating = rating
        self.books[self.book] = self.rating
        return self.books
    
    def get_average_rating(self):
        self.count = 0
        self.ratings = 0
        self.average_rating = 0.0
        for rating in self.books.values():
            if rating != None:
                self.ratings += rating
                self.count += 1
            else:
                continue
        self.average_rating = self.ratings / self.count
        return self.average_rating

#Creating a Book Class:

class Book():
    def __init__(self, title, isbn, price = None):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []
        
    #Define base methods for Book Class:
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN has been updated to {isbn}.".format(isbn = self.isbn))
        return self.isbn
    
    def add_rating(self, rating):
        self.rating = rating
        if self.rating >= 0 and self.rating <= 4:
            self.ratings.append(self.rating)
        else:
            print("Invalid Rating")
        return self.ratings

    def set_price(self, price):
        self.price = price
        print("The price has been set to {price}.".format(price = self.price))
        return self.price
    
    def __repr__(self):
        return "Book {title}".format(title = self.title)
        
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    #Define advanced methods for Book Class
    def get_average_rating(self):
        self.count = 0
        self.total_ratings = 0
        self.average_rating = 0
        for rating in self.ratings:
            if rating != None:
                self.total_ratings += rating
                self.count += 1
            else:
                continue
        self.average_rating = self.total_ratings / self.count
        return self.average_rating

#Creating a Fiction child Class of the parent Book Class:

class Fiction(Book):
    def __init__(self, title, author, isbn, price = None):
        super().__init__(title, isbn, price)
        self.author = author
        
    #Define base methods for Fiction Class:
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

#Creating a Non-Fiction child Class of the parent Book Class:

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price = None):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level
        
    #Define base methods for Non_Fiction Class:
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

#Creating a TomeRater Class:

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        
    #Define base methods for TomeRater Class:
    def __repr__(self):
        self.total_users = 0
        self.total_books = 0
        for user in self.users:
            self.total_users += 1
        for book in self.books:
            self.total_books += 1
        return "Object has {users} users and {books} books".format(users = self.total_users, books = self.total_books)
        
    def __eq__(self, other_tomerater):
        return self.users == other_tomerater.users and self.books == other_tomerater.books
    
    def create_book(self, title, isbn, price = None):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.new_book = Book(self.title, self.isbn, self.price)
        #Uncomment print statement to confirm book created
        #print(self.new_book)
        return self.new_book
    
    def create_novel(self, title, author, isbn, price = None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.new_novel = Fiction(self.title, self.author, self.isbn, self.price)
        #Uncomment print statement to confirm novel created
        #print(self.new_novel)
        return self.new_novel
    
    def create_non_fiction(self, title, subject, level, isbn, price = None):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        self.price = price
        self.new_non_fiction = Non_Fiction(self.title, self.subject, self.level, self.isbn, self.price)
        #Uncomment print statement to confirm non fiction book created
        #print(self.new_non_fiction)
        return self.new_non_fiction
    
    def add_book_to_user(self, book, email, rating = None):
        self.book = book
        self.email = email
        self.rating = rating
        if self.email in self.users:
            self.users[self.email].read_book(self.book, self.rating)
            if self.rating != None:
                self.book.add_rating(self.rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
            #Uncomment print statement to confirm book added to user
            #print("{book} was added to {email}".format(book = self.book, email = self.email))
        else:
            print("No user with email {email}".format(email = self.email))
    
    def add_user(self, name, email, user_books = None):
        self.name = name
        self.email = email
        self.user_books = user_books
        self.new_user = User(self.name, self.email)
        self.users[self.email] = self.new_user
        if self.user_books != None:
            for book in self.user_books:
                self.add_book_to_user(book, self.email)
        #Uncomment return statement to confirm user added
        #return "{name} with email {email} was added.".format(name = self.name, email = self.email)
    
    #Define advanced methods for TomeRater Class
    def print_catalog(self):
        for book in self.books:
            print(book)
            
    def print_users(self):
        for user in self.users.values():
            print(user)
            
    def most_read_book(self):
        self.read_count = 0
        self.most_read = None
        for book, count in self.books.items():
            if count > self.read_count:
                self.read_count = count
                self.most_read = book
            else:
                continue
        return self.most_read
    
    def highest_rated_book(self):
        self.current_rating = 0.0
        self.highest_rating = 0.0
        self.highest_rated = None
        for book in self.books:
            self.current_rating = book.get_average_rating()
            if self.current_rating > self.highest_rating:
                self.highest_rating = self.current_rating
                self.highest_rated = book
            else:
                continue
        return self.highest_rated
    
    def most_positive_user(self):
        self.current_most_positive = 0.0
        self.most_positive = 0.0
        self.the_most_positive_user = None
        for user in self.users.values():
            self.current_most_positive = user.get_average_rating()
            if self.current_most_positive > self.most_positive:
                self.most_positive = self.current_most_positive
                self.the_most_positive_user = user
            else:
                continue
        return self.the_most_positive_user

    def get_n_most_expensive_books(self, n):
        self.n = n
        self.count = 0
        self.books_by_price = {}
        self.books_in_order = []
        self.output = []
        for book in self.books:
            self.books_by_price[book.price] = book.title
        self.books_in_order = sorted(self.books_by_price.keys())
        self.books_in_order.reverse()
        for price in self.books_in_order:
            self.output.append(self.books_by_price[price])
        print("The following are the top {n} most expensive books in order:".format(n = self.n))
        while self.count < self.n:
            print(self.output[self.count])
            self.count += 1
        return "End of List"

