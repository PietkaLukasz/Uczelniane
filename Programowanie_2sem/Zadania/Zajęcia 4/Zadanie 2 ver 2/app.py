from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def strona_glowna():
    """Zwraca stronę główną."""
    return render_template('index.html')

@app.route('/about')
def o_aplikacji():
    """Zwraca stronę 'O aplikacji'."""
    return render_template('about.html')

@app.route('/tasks')
def lista_zadan():
    """Zwraca stronę z listą zadań."""
    return render_template('tasks.html')

if __name__ == "__main__":
    app.run(debug=True)