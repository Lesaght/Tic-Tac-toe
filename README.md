# 🎮 Tic-Tac-Toe: Играй с другом или против бота! 🤖

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub repo size](https://img.shields.io/github/repo-size/Lesaght/Tic-Tac-toe-with-and-without-a-bot)](https://github.com/Lesaght/Tic-Tac-toe-with-and-without-a-bot)

Классическая игра в крестики-нолики с двумя режимами: против друга или против умного бота! Написана на чистом Python 🐍 без внешних зависимостей.

## ✨ Особенности
- **👥 Два режима игры**
  - Против другого игрока
  - Против компьютерного бота
- **🎯 Умный алгоритм бота**
  - Непобедимая стратегия с использованием алгоритма минимакс
- **🎨 Простой текстовый интерфейс**
  - Интуитивно понятное управление
  - Цветовые подсказки
- **🏆 Система подсчёта побед**
  - Отслеживание статистики для каждого игрока

## 📸 Скриншоты

| Главное меню | Игровой процесс | Победа! |
|--------------|-----------------|---------|
| ![Меню](https://raw.githubusercontent.com/Lesaght/Tic-Tac-toe-with-and-without-a-bot/main/menu.png) | ![Геймплей](https://raw.githubusercontent.com/Lesaght/Tic-Tac-toe-with-and-without-a-bot/main/gameplay.png) | ![Победа](https://raw.githubusercontent.com/Lesaght/Tic-Tac-toe-with-and-without-a-bot/main/victory.png) |

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Lesaght/Tic-Tac-toe-with-and-without-a-bot.git
cd Tic-Tac-toe-with-and-without-a-bot
```

2. Запустите нужный режим:
```bash
# Против друга
python tictactoe_human.py

# Против бота
python tictactoe_bot.py
```

## 🕹 Как играть
1. Выберите режим игры в главном меню
2. Вводите координаты ячейки в формате `строка столбец` (например: `1 2`)
3. Первый игрок всегда ❌, второй ⭕
4. Побеждает тот, кто первым соберёт линию из 3 своих символов!

## 🛠 Технологии
- Python 3.8+
- Алгоритм минимакс для AI
- Модуль `colorama` для цветного вывода

## 📜 Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

---

<div align="center">
  <p>Сделано с ❤️ и 🐍</p>
  <p>Вопросы и предложения: <a href="https://github.com/Lesaght">Lesaght</a></p>
</div>
```