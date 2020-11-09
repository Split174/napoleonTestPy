## Тестовое задание отдела DDC

#### Установка и запуск:
```
git clone https://github.com/Split174/napoleonTestPy ~/path_test/
cd ~/path_test/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/app.py 
```

#### Структура проекта

- Api маршруты в директории `src/blueprints/` 
- Модели pydantic для валидации в директории `src/scheme/`
- Сервисы в директории `src/services/`
- Модели ORM `src/models.py`
- Конфиги `src/config.py`
- Контекстный менеджер для работы с бд `src/database.py`
- Базовый класс эксепшонов `src/exception.py`
- Swagger `docs/`

##### Переменные окружения
- DATABASE_URL
- SECRET_KEY

##### Замечания по маршрутам
Создание офера требует наличие валидного jwt токена в headers.token

