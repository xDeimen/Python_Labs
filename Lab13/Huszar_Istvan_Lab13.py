import sqlite3

# Creează o conexiune către baza de date
conn = sqlite3.connect('hr_database.db')  # Numele bazei de date poate fi modificat

# Creează tabelul pentru datele despre personal
conn.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    nume TEXT,
                    varsta INTEGER,
                    gen TEXT,
                    departament TEXT,
                    denumire_post TEXT,
                    data_angajarii TEXT,
                    id_dosar_cu_acte TEXT,
                    adresa_acasa TEXT,
                    telefon_mobil_privat TEXT,
                    telefon_mobil_serviciu TEXT,
                    numar_birou TEXT,
                    email_serviciu TEXT,
                    email_privat TEXT,
                    studii TEXT,
                    certificari_si_specializari TEXT,
                    date_personale_buletin TEXT,
                    salariu_lunar REAL,
                    hobby TEXT,
                    stare_civila TEXT,
                    competente_cheie TEXT,
                    proiecte_lucrate TEXT,
                    puncte_delicate TEXT,
                    nevoi_de_instruire TEXT,
                    teste_si_rezultate TEXT,
                    evaluari_anuale TEXT,
                    fisa_post TEXT,
                    tip_contract_munca TEXT,
                    vechime_in_munca INTEGER,
                    locuri_de_munca_anterioare TEXT,
                    rezultate_deosebite TEXT,
                    diverse TEXT
                )''')

# Introduceți date fictive în tabelul employees
conn.execute("INSERT INTO employees VALUES (1, 'John Doe', 30, 'Masculin', 'HR', 'Manager HR', '2022-01-01', 'ID123', 'Adresa1', '1234567890', '0987654321', 'B123', 'john.doe@companie.com', 'john.doe@gmail.com', 'Studii1', 'Certificari1', '1234567890', 5000, 'Ciclism', 'Căsătorit', 'Competențe1', 'Proiect1', 'Puncte delicate1', 'Nevoi de instruire1', 'Teste și rezultate1', 'Evaluări anuale1', 'Fisa post1', 'Full-time', 3, 'Locuri de muncă anterioare1', 'Rezultate deosebite1', 'Diverse1')")
# Introduceți și alte date fictive în același mod


# Exemplu de interogare pentru a selecta toate datele despre personal
cursor = conn.execute("SELECT * FROM employees")
for row in cursor:
    print(row)

# Exemplu de interogare pentru a actualiza datele unui angajat
conn.execute("UPDATE employees SET salariu_lunar = 5500 WHERE id = 1")

# Exemplu de interogare pentru a șterge un angajat din baza de date
conn.execute("DELETE FROM employees WHERE id = 1")

conn.close()


