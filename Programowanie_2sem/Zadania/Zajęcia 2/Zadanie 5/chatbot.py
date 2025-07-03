class SimpleChatbot:
    def __init__(self, pytania):
        self.pytania = pytania
        self.indeks = 0  # Śledzi, które pytanie jest następne

    def __iter__(self):
        return self  # Zwraca siebie jako iterator

    def __next__(self):
        if self.indeks < len(self.pytania):
            pytanie = self.pytania[self.indeks]
            self.indeks += 1
            return pytanie
        raise StopIteration  # Rzuca, gdy pytania się kończą