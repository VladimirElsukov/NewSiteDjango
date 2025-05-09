function submitQuestion(event) {
    event.preventDefault();  // Предотвращаем отправку формы

    var questionText = document.getElementById('question_text').value;
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('{% url "ask_question" %}', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken,
        },
        body: 'question_text=' + encodeURIComponent(questionText)
    })
    .then(response => response.json())
    .then(data => {
        if (data.answer) {
            document.getElementById('answer-text').textContent = data.answer;  // Устанавливаем текст ответа
            document.getElementById('answer-container').style.display = 'block';  // Отображаем контейнер с ответом
        } else {
            console.error('Ошибка:', data.error);
        }
    })
    .catch((error) => {
        console.error('Ошибка:', error);
    });
}
