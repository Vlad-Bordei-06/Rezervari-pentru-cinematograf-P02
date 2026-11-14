# API-ul ar trebui sa faca conexiunea intre frontend (utilizator) si baza de date:
# verifica cererile si citeste din/modifica baza de date pe baza acestuia

# Ce ar trebui sa poata sa faca API-ul:
# GET/SET proiectiile disponibile
# GET lista de scaune a unei proiectii
# GET/SET rezervarea unui scaun dintr-o proiectie, in urma verificarilor desigur
# poate altele

# Ca sa pornesti aplicatia: uv run fastapi dev (desigur uv trebuie sa fie instalat)

from fastapi import FastAPI, HTTPException  # Folosim FastAPI pentru administrarea API-ului
# from pydantic import BaseModel  # Folosim Pydantic pentru modelele de date necesare pentru request body

app = FastAPI()

# lista asta trebuie eventual inlocuita cu intrarile dintr-o baza de date
lista_filme_placeholder = [
    [{"titlu": "omul paianjen calea catre casa"}, {"durata": 1234}],
    [{"titlu": "darth vlader"}, {"durata": 5678}],
    [{"titlu": "abcdefghi"}, {"durata": 67676767}]
]

# cred ca vom folosi POST pentru a rezerva un scaun
# in rest GET

@app.get("/")
def root():  # todo: afla ce inseamna keywordu 'async'
    return {"message": "Hello World"}

@app.get("/proiectii")
def get_lista_proiectii():
    return lista_filme_placeholder

@app.get("/proiectii/{id_proiectie}")
def get_proiectie(id_proiectie: int):
    if id_proiectie >= len(lista_filme_placeholder) or id_proiectie < 0:
        raise HTTPException(status_code = 404, detail = "Proiectia nu exista")
    return {"id": id_proiectie, "info": lista_filme_placeholder[id_proiectie]}
