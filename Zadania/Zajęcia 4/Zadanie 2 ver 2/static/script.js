document.addEventListener('DOMContentLoaded', () => {
    // Ładujemy zadania z localStorage
    let zadania = JSON.parse(localStorage.getItem('zadania')) || [];
    let nastepneId = zadania.length ? Math.max(...zadania.map(z => z.id)) + 1 : 1;

    const listaZadan = document.getElementById('lista-zadan');
    const form = document.getElementById('dodaj-form');
    const trescInput = document.getElementById('tresc');

    // Funkcja renderująca listę zadań
    function renderujZadania() {
        listaZadan.innerHTML = '';
        zadania.forEach(zadanie => {
            const li = document.createElement('li');
            li.textContent = zadanie.tresc;
            if (zadanie.czyWykonane) {
                li.classList.add('wykonane');
            }

            // Przycisk "Oznacz jako wykonane"
            const wykonajBtn = document.createElement('button');
            wykonajBtn.textContent = zadanie.czyWykonane ? 'Cofnij' : 'Wykonane';
            wykonajBtn.onclick = () => {
                zadanie.czyWykonane = !zadanie.czyWykonane;
                zapiszZadania();
                renderujZadania();
            };

            // Przycisk "Usuń"
            const usunBtn = document.createElement('button');
            usunBtn.textContent = 'Usuń';
            usunBtn.onclick = () => {
                zadania = zadania.filter(z => z.id !== zadanie.id);
                zapiszZadania();
                renderujZadania();
            };

            li.appendChild(wykonajBtn);
            li.appendChild(usunBtn);
            listaZadan.appendChild(li);
        });
    }

    // Funkcja zapisująca zadania do localStorage
    function zapiszZadania() {
        localStorage.setItem('zadania', JSON.stringify(zadania));
    }

    // Obsługa formularza
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const tresc = trescInput.value.trim();
        if (tresc) {
            zadania.push({ id: nastepneId++, tresc: tresc, czyWykonane: false });
            zapiszZadania();
            renderujZadania();
            trescInput.value = '';
        }
    });

    // Początkowe renderowanie
    renderujZadania();
});