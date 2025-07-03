from chatbot import SimpleChatbot

# Tworzenie bota z pytaniami
bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?", "Miasto, czy wieś?", "Morze, czy góry?"])

# Test: iterujemy po pytaniach i czekamy na odpowiedzi
for question in bot:
    print(question)
    input()  # Użytkownik wpisuje odpowiedź