async function askYaga() {
  const question = document.getElementById("question").value.trim();
  const answer = document.getElementById("answer");

  if (!question) {
    answer.textContent = "🧙‍♀️ Яга ждёт вопрос...";
    return;
  }

  answer.textContent = "🧙‍♀️ Яга размышляет…";

  try {
    const response = await fetch(
      "https://yaga7000-backend.onrender.com/api/ask",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: question })
      }
    );

    const data = await response.json();
    answer.textContent = data.response;
  } catch (e) {
    answer.textContent = "🔥 Яга потеряла связь с миром. Попробуй позже.";
  }
}
