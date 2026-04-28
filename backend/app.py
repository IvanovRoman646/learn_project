"""
Основное Flask приложение для API учёта товаров
"""

from flask import Flask, jsonify
from flask_cors import CORS
import os

# Создаём Flask приложение
app = Flask(__name__)

# Включаем CORS для работы с фронтендом
CORS(app)

# Основной маршрут
@app.route('/')
def home():
    """"Главная страница API"""
    return jsonify({'message': 'API система товаов',
                    'version': '1.0.o',
                    'endpoints': {
                        'GET /': 'Информация об API',
                        'GET /health': 'Проверка состаяния сервера'
                    }
    })

# Маршрут для проверки состаяния
@app.route('/health')
def health_check():
    """Проверка работоспособности серва=ера"""
    return jsonify({'status': 'OK'}),200

# Запуск приложения
if __name__ == '__main__':
    # Создаём папку для данных если её нет
    if not os.path.exists('data'):
        os.makedirs("'data'")
        print("Создана папку 'data'")

    print("=" * 40)
    print("Сервер запущен")
    print("API доступен по адресу: http://localhost:5000/")
    print("Фронтенд: frontend/index.html")
    print("=" * 40)

    # Запускаем сервер
    app.run(debug=True, host='0.0.0.0', port=5000)