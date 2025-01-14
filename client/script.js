const apiUrl = "http://localhost:8000"; // URL вашего FastAPI бэкенда
const app = document.getElementById("app");
const quizTitle = document.getElementById("quiz-title");
const quizContainer = document.getElementById("quiz-container");
const submitBtn = document.getElementById("submit-btn");

let quizData = null;
let userAnswers = {};

// Загрузка викторины с бэкенда

const retrieveQuiz = (quizId) => {
  axios
    .get(`${apiUrl}/quiz/${quizId}`)
    .then((response) => {
      quizData = response.data;
      renderQuiz(quizData);
    })
    .catch((error) => {
      quizTitle.textContent = "Failed to load quiz.";
      console.error("Error fetching quiz:", error);
    });

}
// Отображение викторины
function renderQuiz(data) {
  quizTitle.textContent = data.name;
  quizContainer.innerHTML = "";

  data.questions.forEach((question, index) => {
    const questionDiv = document.createElement("div");
    questionDiv.classList.add("question");

    // Вопрос
    const questionTitle = document.createElement("p");
    questionTitle.textContent = question.question;
    questionDiv.appendChild(questionTitle);

    // Ответы
    const optionsDiv = document.createElement("div");
    optionsDiv.classList.add("options");

    if (question.type === "single") {
      question.options.forEach((option, i) => {
        const label = document.createElement("label");
        label.style.display = "block";

        const radio = document.createElement("input");
        radio.type = "radio";
        radio.name = `question-${index}`;
        radio.value = option;

        radio.addEventListener("change", () => {
          userAnswers[index] = option;
        });

        label.appendChild(radio);
        label.appendChild(document.createTextNode(option));
        optionsDiv.appendChild(label);
      });
    } else if (question.type === "open") {
      const input = document.createElement("input");
      input.type = "text";
      input.placeholder = "Type your answer here...";
      input.addEventListener("input", (e) => {
        userAnswers[index] = e.target.value;
      });
      optionsDiv.appendChild(input);
    }

    questionDiv.appendChild(optionsDiv);
    quizContainer.appendChild(questionDiv);
  });

  submitBtn.style.display = "block";
}

// Отправка ответов
submitBtn.addEventListener("click", () => {
  axios
    .post(`${apiUrl}/submit`, userAnswers)
    .then((response) => {
      renderResults(response.data);
    })
    .catch((error) => {
      console.error("Error submitting answers:", error);
    });
});

// Отображение результатов
function renderResults(result) {
  quizTitle.textContent = "Quiz Results";
  quizContainer.innerHTML = `
    <p>You scored ${result.score} out of ${quizData.questions.length}.</p>
    <p>${result.passed ? "Congratulations, you passed!" : "Sorry, you failed."
    }</p>
  `;
  submitBtn.style.display = "none";
}


const quizSelector = document.querySelector("[name=quiz_chooser]")
quizSelector.addEventListener("change", (event) => { retrieveQuiz(event.target.value) })
console.log(quizSelector)