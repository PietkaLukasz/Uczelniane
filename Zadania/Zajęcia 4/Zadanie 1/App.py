from flask import Flask

app = Flask(__name__)

# Dane użytkowników
uzytkownicy = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

@app.route('/')
def strona_glowna():
    """Zwraca stronę główną z powitaniem i linkami."""
    return """
    <h1>Witaj w Mini Portalu!</h1>
    <p>Przejdź do: 
    <a href="/about">O nas</a> | 
    <a href="/users">Lista użytkowników</a></p>
    """

@app.route('/about')
def o_nas():
    """Zwraca stronę 'O nas'."""
    return """
    <h1>O nas</h1>
    <p>Jesteśmy super ekipą tworzącą mini portal z profilami!</p>
    <a href="/">Wróć do strony głównej</a>
    """

@app.route('/users')
def lista_uzytkownikow():
    """Zwraca listę użytkowników z linkami do ich profili."""
    html = "<h1>Lista użytkowników</h1><ul>"
    for user_id, dane in uzytkownicy.items():
        html += f'<li><a href="/user/{user_id}">{dane["name"]}</a></li>'
    html += '</ul><a href="/">Wróć do strony głównej</a>'
    return html

@app.route('/user/<int:user_id>')
def profil_uzytkownika(user_id):
    """Zwraca profil użytkownika lub błąd, jeśli nie istnieje."""
    if user_id in uzytkownicy:
        dane = uzytkownicy[user_id]
        return f"""
        <h1>Profil użytkownika</h1>
        <p>{dane["name"]}, {dane["age"]} lat</p>
        <a href="/users">Wróć do listy użytkowników</a>
        """
    return """
    <h1>Błąd</h1>
    <p>Użytkownik nie istnieje!</p>
    <a href="/users">Wróć do listy użytkowników</a>
    """

if __name__ == "__main__":
    app.run(debug=True)