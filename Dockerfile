FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl wget unzip libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 \
    libpango-1.0-0 libpangocairo-1.0-0 libasound2 \
    libxshmfence1 libwayland-client0 libwayland-cursor0 \
    fonts-liberation lsb-release xdg-utils && \
    apt-get clean

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN playwright install --with-deps

CMD ["pytest", "--alluredir=reports"]
