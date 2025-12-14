# Используем готовый Playwright образ с Python и браузерами
FROM mcr.microsoft.com/playwright/python:v1.39.0-focal

WORKDIR /app

# Копируем зависимости Python и ставим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Команда по умолчанию — запуск тестов
CMD ["pytest", "--alluredir=reports"]
