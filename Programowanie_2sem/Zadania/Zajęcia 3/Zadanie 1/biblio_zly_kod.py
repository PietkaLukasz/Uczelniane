class biblioteka:
    def __init__(self,BOOKS):
        self.BOOKS=BOOKS

    def findBook(self,isbn):#znajdz ksiazke po isbn
        if isbn in self.BOOKS:
            return self.BOOKS[isbn]
        else:
            return None

def add_book(isbn,title, books): #dodaje ksiazke
    books[isbn]=title
    return books

if __name__ == "__main__":
    b=biblioteka({"978-83-240-1234-5":"Pan Tadeusz","978-83-727-9876-2":"Wiedzmin"})
    print(b.findBook("978-83-240-1234-5"))
    print(b.findBook("999-99-999-9999-9"))
    add_book("978-83-111-2222-3","Lalka",b.BOOKS)
    print(b.findBook("978-83-111-2222-3"))