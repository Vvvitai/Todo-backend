from entry import Entry
from entrymanager import EntryManager
from fastapi import FastAPI
from pydantic_settings import BaseSettings
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


class Settings(BaseSettings):
    data_folder: str = 'C:\\Users\\vital\\PycharmProjects\\Todo_list'


settings = Settings()
app = FastAPI(title='Todo backend', description='Приложение списка дел')

origins = [
    "http://localhost:8000",
    "https://wexler.io" # адрес на котором запускаете бэк-энд
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    # Список разрешенных доменов
    allow_credentials=True,   # Разрешить Cookies и Headers
    allow_methods=["*"],      # Разрешить все HTTP методы
    allow_headers=["*"],      # Разрешить все хедеры
)


@app.get("/api/entries/")
async def get_entries():
    entry_manager = EntryManager(settings.data_folder)
    entry_manager.load()
    return [entry.json() for entry in entry_manager.entries]

@app.post('/api/save_entries/')
async def save_entries(data: List[dict]):
    entry_manager = EntryManager(settings.data_folder)
    for item in data:
        new_entry = Entry.from_json(item)
        entry_manager.entries.append(new_entry)
    entry_manager.save()
    return {'status': 'success'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
