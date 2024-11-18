# Bot Todos: Ваш персональный менеджер заметок 🤖

## Описание

**Bot Todos** — это Telegram-бот, построенный с использованием фреймворка `aiogram`, который помогает пользователям управлять своими заметками. С этим ботом вы можете:
- Добавлять новые заметки.
- Просматривать существующие заметки.
- Удалять заметки с помощью интерфейса с инлайн-кнопками.

## Особенности

- **Добавление заметок**: Сохраняйте свои мысли или важную информацию, просто напечатав их.
- **Просмотр заметок**: Просматривайте все сохраненные заметки в удобном формате.
- **Удаление заметок**: Удаляйте устаревшие или ненужные заметки одним нажатием.

## Технологии

- **Язык**: Python
- **Фреймворк**: [aiogram](https://docs.aiogram.dev/en/latest/)
- **База данных**: на ваш выбор (SQLite, PostgreSQL и т. д.)
- **Управление состояниями**: finite state machine (FSM) от aiogram

## Установка

1. Клонируйте этот репозиторий:
   ```bash
   git clone https://github.com/your-username/bot-todos.git
   cd bot-todos
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```
3. Установите необходимые зависимости:
   ```bash
    pip install -r requirements.txt
   ```
4. Настройте вашу базу данных:
   - Убедитесь, что база данных правильно настроена в файле `database.py`.

5. Настройте вашего Telegram-бота:
  - Получите токен бота у BotFather.
  - Создайте файл `.env` в корне проекта и добавьте токен:
   ```bash
      BOT_TOKEN=your_bot_token_here
   ```
6. Запустите бота:
  ```bash
      python3 main.py
   ```

## Использование
1. Начните использование бота, отправив команду `/start`.
2. Используйте кнопки в клавиатуре для:
  - Добавления заметок.
  - Просмотра ваших сохраненных заметок.
  - Удаления заметок с помощью инлайн-кнопок.

## Структура файлов
```bash
├── main.py               # Точка входа для бота
├── router.py             # Содержит все команды и колбэки бота
├── database.py           # Обрабатывает операции с базой данных (добавление, получение, удаление)
├── requirements.txt      # Зависимости Python
└── README.md             # Документация проекта
```

## Как это работает
1. Добавление заметок: Пользователь может отправить команду `/start` или нажать на кнопку "Добавить заметку", после чего бот попросит ввести текст заметки.

2. Просмотр заметок: Пользователь может выбрать опцию "Посмотреть заметки" и бот отобразит все сохраненные заметки.

3. Удаление заметок: Пользователь может удалить заметку, выбрав ее через инлайн-кнопку, которая появляется при нажатии на кнопку "Удалить заметку".
