# Get data from google sheets
Проект содержит скрипт goosheets.py для выгрузки данных с google docs https://docs.google.com/spreadsheets/d/1Fr7PjXteEt7MzWHIycbwScs7hMOUCu4NzdPkNrYoccI/. Расположен скрипт в директории проекта django_react. Данный скрипт получает данные с google docs и вставляет их в базу данных Postgresql. Реализована проверка соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram. Данные для перевода $ в рубли получаем по курсу ЦБ РФ. В качестве бекенда используется Django, в качестве фронтенда React. Можно посмотреть работу по адресу http://paturaka.beget.app:8000/ (chrome)


## Создание крона для автоматического выполнения скрипта

```bash
* * * * * cd /root/channelservice && source venv/bin/activate && cd django_react && /usr/bin/python3 goosheets.py
```

## Установка backend
Предварительно установите Postgresql, Python3 (данный проект использует 3.8), python3-pip, python3-venv, git
Далее
* Склонировать репозиторий на локальную машину:
```bash
git clone git@github.com:iriderprokhorov/channelservice.git
cd channelservice
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source env/bin/activate
```

* Cоздайте файл `.env`  с содержанием:

```
SHEET_ID = id документа гугл
DB_NAME= имя базы данных
POSTGRES_USER=логин для подключения к базе данных
POSTGRES_PASSWORD= пароль для подключения к БД 
DB_HOST=
DB_PORT=порт для подключения к БД
TOKEN=telegram token
CHAT_ID= id канала
```

* Перейти в директирию и установить зависимости из файла requirements.txt:

```bash
cd backend/
pip install -r requirements.txt
```

* Выполните миграции:

```bash
python manage.py migrate
```

* Запустите сервер:
```bash
python manage.py runserver
```

## Установка frontend
Необходимо установить Node.js версии 6+ и npm версии 5.2 или выше
В данном проекте используется Node.js 16.17.0 , npm 8.15

Далее нужно установить зависимости и запустить сервер

```bash
npm install
npm run dev
```


## "To do"
- [x] Добавить крутое README
- [ ] Упаковать в докер
- [ ] ...

