from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)

# Заглушки для данных (в реальном приложении будут из БД)
levels = [
    {"id": 1, "name": "Начинающий 🟢", "emoji": "👶"},
    {"id": 2, "name": "Элементарный 🟠", "emoji": "🙂"},
    {"id": 3, "name": "Средний 🟡", "emoji": "😊"},
    {"id": 4, "name": "Продвинутый 🔴", "emoji": "💪"},
    {"id": 5, "name": "Эксперт 🟣", "emoji": "🎓"}
]

lessons = {
    1: [
        {"id": 1, "name": "Алфавит и звуки 🔤", "emoji": "🔤", "content": """
        <h2>Русский алфавит 📚</h2>
        <p>Русский алфавит состоит из 33 букв:</p>
        <div class="alphabet">
            <p>А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я</p>
        </div>
        <h3>Особые звуки 🔊</h3>
        <ul>
            <li><strong>Ё</strong> - звук [йо] как в слове "ёлка"</li>
            <li><strong>Ж</strong> - звук [ж] как в слове "жук"</li>
            <li><strong>Ш</strong> - звук [ш] как в слове "шар"</li>
            <li><strong>Щ</strong> - звук [щ] как в слове "щука"</li>
            <li><strong>Ц</strong> - звук [ц] как в слове "цветок"</li>
        </ul>
        <h3>Практика 🎯</h3>
        <p>Попробуйте произнести: "Мама мыла раму"</p>
        <p>Повторите за диктором: "Привет, как дела?"</p>
        """},
        {"id": 2, "name": "Приветствия 👋", "emoji": "👋", "content": "Содержание урока приветствий..."},
        {"id": 3, "name": "Цифры и числа 1-10 🔢", "emoji": "🔢", "content": "Содержание урока цифр..."},
        {"id": 4, "name": "Цвета 🌈", "emoji": "🌈", "content": "Содержание урока цветов..."},
        {"id": 5, "name": "Семья 👨‍👩‍👧‍👦", "emoji": "👨‍👩‍👧‍👦", "content": "Содержание урока семьи..."}
    ],
    2: [
        {"id": 1, "name": "Еда и напитки 🍎", "emoji": "🍎", "content": "Содержание урока еды..."},
        {"id": 2, "name": "Дни недели 📅", "emoji": "📅", "content": "Содержание урока дней недели..."},
        # ... остальные уроки
    ],
}


# Заготовка для интеграции с БД
class DatabaseManager:
    def __init__(self):
        # Здесь будет подключение к реальной БД
        pass

    def get_levels(self):
        # Заглушка - в реальности будет запрос к БД
        return levels

    def get_lessons(self, level_id):
        # Заглушка - в реальности будет запрос к БД
        return lessons.get(level_id, [])

    def get_lesson_content(self, level_id, lesson_id):
        # Заглушка - в реальности будет запрос к БД
        level_lessons = lessons.get(level_id, [])
        for lesson in level_lessons:
            if lesson['id'] == lesson_id:
                return lesson
        return None


# Инициализация сервисов
db_manager = DatabaseManager()


@app.route('/')
def index():
    return render_template('index.html', levels=levels, show_lessons=False, show_lesson=False)


@app.route('/level/<int:level_id>')
def show_lessons(level_id):
    lesson_list = db_manager.get_lessons(level_id)
    return render_template('index.html', levels=levels, lessons=lesson_list,
                           current_level=level_id, show_lessons=True, show_lesson=False)


@app.route('/level/<int:level_id>/lesson/<int:lesson_id>')
def show_lesson(level_id, lesson_id):
    lesson = db_manager.get_lesson_content(level_id, lesson_id)
    lesson_list = db_manager.get_lessons(level_id)
    return render_template('index.html', levels=levels, lessons=lesson_list,
                           current_level=level_id, current_lesson=lesson,
                           show_lessons=False, show_lesson=True)


from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Создаем папку для загрузок, если её нет
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Заглушки для данных
levels = [
    {"id": 1, "name": "Начинающий 🟢", "emoji": "👶"},
    {"id": 2, "name": "Элементарный 🟠", "emoji": "🙂"},
    {"id": 3, "name": "Средний 🟡", "emoji": "😊"},
    {"id": 4, "name": "Продвинутый 🔴", "emoji": "💪"},
    {"id": 5, "name": "Эксперт 🟣", "emoji": "🎓"}
]

lessons = {
    1: [
        {"id": 1, "name": "Алфавит и звуки 🔤", "emoji": "🔤", "content": """
        <h2>Русский алфавит 📚</h2>
        <p>Русский алфавит состоит из 33 букв:</p>
        <div class="alphabet">
            <p>А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я</p>
        </div>
        <h3>Особые звуки 🔊</h3>
        <ul>
            <li><strong>Ё</strong> - звук [йо] как в слове "ёлка"</li>
            <li><strong>Ж</strong> - звук [ж] как в слове "жук"</li>
            <li><strong>Ш</strong> - звук [ш] как в слове "шар"</li>
            <li><strong>Щ</strong> - звук [щ] как в слове "щука"</li>
            <li><strong>Ц</strong> - звук [ц] как в слове "цветок"</li>
        </ul>
        <h3>Практика 🎯</h3>
        <p>Попробуйте произнести: "Мама мыла раму"</p>
        <p>Повторите за диктором: "Привет, как дела?"</p>
        """},
        {"id": 2, "name": "Приветствия 👋", "emoji": "👋", "content": "Содержание урока приветствий..."},
        {"id": 3, "name": "Цифры и числа 1-10 🔢", "emoji": "🔢", "content": "Содержание урока цифр..."},
        {"id": 4, "name": "Цвета 🌈", "emoji": "🌈", "content": "Содержание урока цветов..."},
        {"id": 5, "name": "Семья 👨‍👩‍👧‍👦", "emoji": "👨‍👩‍👧‍👦", "content": "Содержание урока семьи..."}
    ],
    2: [
        {"id": 1, "name": "Еда и напитки 🍎", "emoji": "🍎", "content": "Содержание урока еды..."},
        {"id": 2, "name": "Дни недели 📅", "emoji": "📅", "content": "Содержание урока дней недели..."},
    ],
}


@app.route('/')
def index():
    return render_template('index.html', levels=levels, show_lessons=False, show_lesson=False)


@app.route('/level/<int:level_id>')
def show_lessons(level_id):
    lesson_list = lessons.get(level_id, [])
    return render_template('index.html', levels=levels, lessons=lesson_list,
                           current_level=level_id, show_lessons=True, show_lesson=False)


@app.route('/level/<int:level_id>/lesson/<int:lesson_id>')
def show_lesson(level_id, lesson_id):
    lesson = None
    for l in lessons.get(level_id, []):
        if l['id'] == lesson_id:
            lesson = l
            break

    lesson_list = lessons.get(level_id, [])
    return render_template('index.html', levels=levels, lessons=lesson_list,
                           current_level=level_id, current_lesson=lesson,
                           show_lessons=False, show_lesson=True)


@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'Файл не выбран'})

    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'Файл не выбран'})

    if file:
        # Простая проверка типа файла
        if not file.filename.lower().endswith(('.wav', '.mp3', '.ogg', '.m4a')):
            return jsonify({'error': 'Поддерживаются только аудиофайлы (WAV, MP3, OGG, M4A)'})

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            file.save(filepath)
            print(f"Файл сохранен: {filepath}")

            # Имитация анализа произношения
            feedback_options = [
                "Отличное произношение! Вы говорите как носитель языка!",
                "Хорошее произношение, но нужно поработать над интонацией.",
                "Неплохо! Попробуйте четче произносить согласные звуки.",
                "Нужно поработать над произношением гласных звуков.",
                "Попробуйте говорить медленнее и четче."
            ]

            score = round(random.uniform(0.6, 0.95), 2)  # Случайная оценка от 60% до 95%
            feedback = random.choice(feedback_options)

            return jsonify({
                'success': True,
                'score': score,
                'feedback': feedback,
                'filename': filename
            })

        except Exception as e:
            return jsonify({'error': f'Ошибка при сохранении файла: {str(e)}'})

    return jsonify({'error': 'Неизвестная ошибка'})

@app.route('/telegram_webapp', methods=['GET', 'POST'])
def telegram_webapp():
    return render_template('telegram_webapp.html')

if __name__ == '__main__':
    app.run(debug=True)