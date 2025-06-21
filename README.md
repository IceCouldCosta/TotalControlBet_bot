# TotalControlBet Bot

Бот публикует прогнозы на канал Telegram и принимает команды.

## Команды:
- /start — приветствие
- /статус — проверка статуса бота

## Переменные:
- `TOKEN` — токен Telegram Bot
- `CHANNEL_ID` — куда публикуются прогнозы
- `ADMIN_ID` — кому отправлять уведомления

## Деплой
1. Загрузите репозиторий на GitHub
2. Подключите к Render.com (тип: **Background Worker**)
3. Добавьте в корне: `Procfile`, `requirements.txt`, `bot.py`, `config.py`
