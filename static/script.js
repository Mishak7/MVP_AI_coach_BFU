document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('uploadBtn');
    const audioInput = document.getElementById('audioFile');
    const resultContainer = document.getElementById('result');
    const loadingContainer = document.getElementById('loading');
    const errorContainer = document.getElementById('error');
    const scoreValue = document.getElementById('scoreValue');
    const feedbackText = document.getElementById('feedbackText');
    const errorText = document.querySelector('.error-text');

    if (uploadBtn) {
        uploadBtn.addEventListener('click', function() {
            if (audioInput.files.length === 0) {
                showError('Пожалуйста, выберите аудиофайл');
                return;
            }

            // Скрываем предыдущие результаты и ошибки
            resultContainer.style.display = 'none';
            errorContainer.style.display = 'none';

            // Показываем загрузку
            loadingContainer.style.display = 'block';

            const formData = new FormData();
            formData.append('audio', audioInput.files[0]);

            fetch('/upload_audio', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Скрываем загрузку
                loadingContainer.style.display = 'none';

                if (data.error) {
                    showError(data.error);
                } else if (data.success) {
                    // Показываем результат
                    scoreValue.textContent = Math.round(data.score * 100);
                    feedbackText.textContent = data.feedback;
                    resultContainer.style.display = 'block';

                    // Прокручиваем к результату
                    resultContainer.scrollIntoView({ behavior: 'smooth' });
                }
            })
            .catch(error => {
                loadingContainer.style.display = 'none';
                console.error('Error:', error);
                showError('Произошла ошибка при загрузке файла');
            });
        });
    }

    function showError(message) {
        errorText.textContent = message;
        errorContainer.style.display = 'block';
        errorContainer.scrollIntoView({ behavior: 'smooth' });
    }

    // Показываем имя выбранного файла
    if (audioInput) {
        audioInput.addEventListener('change', function() {
            const fileName = this.files[0]?.name || 'Файл не выбран';
            document.querySelector('.file-label').textContent = `📁 ${fileName}`;

            resultContainer.style.display = 'none';
            errorContainer.style.display = 'none';
        });
    }
});