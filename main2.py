from model import NoteInfoResponse, NoteTextResponse, NoteCreateResponse, NoteListResponse
from datetime import datetime

if __name__ == '__main__':
    response = NoteTextResponse(  # Получение текста заметки
        id = 4,  # id заметки
        text = " "  # текст заметки
    )

    response = NoteCreateResponse(  # Создание заметки
        id = 123,
        text = " "  # текст заметки
    )
    print(response.json())

    response = NoteListResponse(  # Получение списка заметок
        note_list = [1, 2, 3]
    )
    print(response.json())

    response = NoteInfoResponse(  # Получение информации о заметке
        created_at = datetime.now(),  # Дата создания
        updated_at = datetime.now()  # Дата обновления заметки
    )
    print(response.json())
