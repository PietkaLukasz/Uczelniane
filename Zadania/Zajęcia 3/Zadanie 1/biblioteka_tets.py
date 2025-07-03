from biblioteka_poprawiony import Biblioteka

biblioteka = Biblioteka({
    "978-83-240-1234-5": "Pan Tadeusz",
    "978-83-727-9876-2": "Wiedźmin"
})

#Testy
print(biblioteka.znajdz_ksiazke("978-83-240-1234-5"))  # Powinno zwrócić: Pan Tadeusz
print(biblioteka.znajdz_ksiazke("999-99-999-9999-9"))  # Powinno zwrócić: None
biblioteka.dodaj_ksiazke("978-83-111-2222-3", "Lalka")
print(biblioteka.znajdz_ksiazke("978-83-111-2222-3"))  # Powinno zwrócić: Lalka