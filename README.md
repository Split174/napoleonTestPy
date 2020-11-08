## Тестовое задание отдела DDC

#### Установка и запуск:
```
git clone https://github.com/Split174/napoleonTestPy ~/path_test/
cd ~/path_test/
python -m venv venv
source venv/bin/activate
python src/app.py 
```

#### Структура проекта

Api маршруты в директории src/blueprints/ \
Модели pydantic для валидации в директории src/scheme/ \
Сервисы в директории src/services/ \
Модели ORM src/models.py \
Конфиги src/config.py \
Контекстный менеджер для работы с бд src/database.py \
Базовый класс эксепшонов src/exception.py

##### Переменные окружения
- DATABASE_URL
- SECRET_KEY
