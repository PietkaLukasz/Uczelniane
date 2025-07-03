from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Prosta trasa Flask
@app.route('/')
def hello():
    return "Cześć, to test Flask!"

# Funkcja sprawdzająca SQLAlchemy
def sprawdz_sqlalchemy():
    engine = create_engine("sqlite:///:memory:")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'SQLAlchemy działa!'"))
        return result.scalar()

if __name__ == "__main__":
    # Wyświetla wynik dla SQLAlchemy
    print(sprawdz_sqlalchemy())
    # Uruchamia Flask
    print("Uruchamiam serwer Flask... Otwórz http://127.0.0.1:5000/ w przeglądarce")
    app.run(debug=True)