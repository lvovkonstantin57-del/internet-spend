<h1 align="center">Internet Spend</h1>

<div align="center">

![Python](https://img.shields.io/badge/Python-stdlib%20only-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML%20%2B%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![No deps](https://img.shields.io/badge/зависимости-0-2ea44f?style=for-the-badge)

</div>

```
Записываешь сервисы, за которые платишь (связь, хостинг, подписки), и видишь, сколько уходит в месяц и в год.
```

## 🧾 Особенности

- **Ноль зависимостей:** сервер на стандартной библиотеке Python, интерфейс — один `index.html`
- **Данные остаются у тебя:** всё хранится локально в `data.json` рядом с приложением
- **Запуск двойным кликом** на macOS через `start.command` — браузер откроется сам

## ▶️ Запуск

```bash
python3 server.py      # → http://127.0.0.1:8765
```

На macOS можно просто дважды кликнуть `start.command`.

## 📂 Файлы

```
server.py       локальный HTTP-сервер и API (stdlib)
index.html      интерфейс
start.command   запуск на macOS
data.json       твои данные — создаётся сам, в git не попадает
```

---

<sub>Автор — [Константин Львов](https://github.com/lvovkonstantin57-del) · [Telegram](https://t.me/l1ttleStich)</sub>
