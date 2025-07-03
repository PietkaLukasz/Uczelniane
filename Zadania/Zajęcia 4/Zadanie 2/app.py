from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista zadań (id, treść, czy_wykonane)
zadania = [
    {"id": 1, "tresc": "Kupić mleko", "czy_wykonane": False},
    {"id": 2, "tresc": "Zadzwonić do mamy", "czy_wykonane": True}
]
nastepne_id = 3  # Śledzi ID dla nowych zadań

@app.route('/')
def strona_glowna():
    """Zwraca stronę główną z linkami."""
    return render_template('index.html')

@app.route('/about')
def o_aplikacji():
    """Zwraca stronę 'O aplikacji'."""
    return render_template('about.html')

@app.route('/tasks', methods=['GET'])
def lista_zadan():
    """Zwraca listę zadań."""
    return render_template('tasks.html', zadania=zadania)

@app.route('/add', methods=['POST'])
def dodaj_zadanie():
    """Dodaje nowe zadanie z formularza."""
    global nastepne_id
    tresc = request.form.get('tresc')
    if tresc:
        zadania.append({"id": nastepne_id, "tresc": tresc, "czy_wykonane": False})
        nastepne_id += 1
    return redirect(url_for('lista_zadan'))

@app.route('/done/<int:zadanie_id>')
def oznacz_jako_wykonane(zadanie_id):
    """Oznacza zadanie jako wykonane."""
    for zadanie in zadania:
        if zadanie["id"] == zadanie_id:
            zadanie["czy_wykonane"] = True
            break
    return redirect(url_for('lista_zadan'))

@app.route('/delete/<int:zadanie_id>')
def usun_zadanie(zadanie_id):
    """Usuwa zadanie z listy."""
    global zadania
    zadania = [zadanie for zadanie in zadania if zadanie["id"] != zadanie_id]
    return redirect(url_for('lista_zadan'))

if __name__ == "__main__":
    app.run(debug=True)