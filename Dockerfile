FROM python:3.14-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CI=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
ENV STREAMLIT_SERVER_HEADLESS=true

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -m playwright install chromium --with-deps

COPY . .

EXPOSE 80 8501

CMD ["sh", "-c", "PORT=8501 python ui/server.py & PORT=80 python ui/server.py"]
