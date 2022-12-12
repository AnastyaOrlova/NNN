from typing import List

import fastapi
import os
from model import NoteInfoResponse
from model import NoteTextResponse
from model import NoteCreateResponse
from model import NoteListResponse
from model import NoteDeleteResponse
from model import NoteUpdateResponse
import datetime

api_router = fastapi.APIRouter()

@api_router.post("/create_note", response_model = NoteCreateResponse)
def create_note(text: str, token: str):
    f1 = os.listdir("notes")
    m_id = []
    for i in range(len(f1)):
        a: list[str] = f1[i].split(".")
        m_id.append(a[0])
        p = int(max(m_id))
        id = p + 1

    my_file = open('notes/' + str(id) + ".txt", "w+")
    my_file.write(text)
#    my_file.created_at = datetime.datetime.now()
    my_file.close()

    return NoteCreateResponse(
    id = int(id),
    )

@api_router.get("/read_note", response_model = NoteTextResponse)
def read_note(id: str):
    my_file = open('notes/' + str(id) + ".txt", "r")
    text = my_file.read()

    return NoteTextResponse(
    id = int(id),
    text = str(text)
    )

@api_router.delete("/delete_note", response_model = NoteDeleteResponse)
def delete_note(id: int):
    os.remove('notes/' + str(id) + ".txt")

    return NoteDeleteResponse(
    id = int(id)
    )

@api_router.put("/update_note", response_model = NoteUpdateResponse)
def update_note(id: int, text: str):
    my_file = open('notes/' + str(id) + ".txt", "w+")
    my_file.write(text)
#    my_file.created_at = datetime.datetime.now()
    my_file.close()

    return NoteUpdateResponse(
    id = int(id),
    text = " "
    )

@api_router.get("/list_note", response_model = NoteListResponse)
def list_note():
    f1 = os.listdir("notes")
    m_id = []
    for i in range(len(f1)):
        a = f1[i].split(".")
        m_id.append(int(a[0]))

    return NoteListResponse(
    note_list = m_id
    )

#@api_router.get("/info_note", response_model = NoteInfoResponse)
#def info_note(id: int):

#    my_file = open('notes/' + str(id) + ".txt", "r")

#    return NoteInfoResponse(
#    created_at =
#    updated_at =
#    )




# 'r' - открытие на чтение
# 'w' - открытие на запись(содержимое существующего файла удаляется),
# если файла не существует, создается новый
# 'x' - открытие на запись
# 'a' - открытие на дозапись(информация добавляется в конец файла)
# '+' - открытие на чтение и запись
