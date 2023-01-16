# Bot_screenshot.

Бот получает от пользователя сообщение содержащее текст ссылки, переходит по ней и 
делает и сохраняет скриншот, а так же получает код ответа страницы. 
Скриншот и код ответа отправляет обратно пользователю.
Скриншот сохраняется в директорию image с именем в формате "YYYY-MM-DD_HH:mm_<link>.jpg".
Вне зависимости от того какой пришел код ответа, программа делает скриншот станицы чтобы 
удостоверится активна ли данная ссылка. Сайт может вернуть код ответа отличный от двухсотых 
или трехсотых, а на скриншоте страницы видно, что данные по этому запросу возвращаются.

#####
![Image text](https://github.com/Anzhela-Namistyuk/Bot_screenshot/blob/main/hh.png)
#####

### Технологии:

> Python 3, selenium, requests, telebot, validators
###

### Создать бота и получить Токен.
```
Для создания нового бота необходимо открыть бота @BotFather 
и использовать команду /newbot. @BotFather запросит имя бота 
и имя пользователя бота (логин), а затем сгенерирует токен 
авторизации для вашего нового бота. 

```
### Создать файл .env и записать токен бота в переменную BOT_TOKEN. 
```
BOT_TOKEN=ВАШ_ТОКЕН
```
##

### Настройка и запуск приложения:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Anzhela-Namistyuk/Bot_screenshot.git 
```

```
cd  Bot_screenshot
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

```
source venv/bin/activate
```

* Если у вас windows

 ```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запуск бота
```
python bot.py
```

#####
Пример передачи сообщения в бот:
``` 
https://www.youtube.com/
```
 Пример ответа:
```
Kод ответа страницы - 200
```
![Image text](https://github.com/Anzhela-Namistyuk/Bot_screenshot/blob/main/image/2023-01-13_19:39_youtube.jpg)

#####
###  Запуск бота в докерконтейнере:

Создание образа:

```
docker build -t image_screen_bot .
```
Запуск контейнера.
#####
При запуске прокидываем токен бота в контейнер.
```
docker run --name screenshot_bot -e BOT_TOKEN=ТОКЕН_ВАШЕГО_БОТА image_screen_bot
```

Остановка контейнера:
```
docker stop screenshot_bot
```


### Автор
Намистюк Анжела 
#####
