async function askYaga(event) {
  if (event) event.preventDefault();

  const input = document.getElementById("questionInput");
  const output = document.getElementById("answer");

  const text = input.value.trim();
  if (!text) {
    output.textContent = "ведите вопрос";
    return;
  }

  output.textContent = "Yaga думает...";

  try {
    const res = await fetch("https://yaga7000-backend.onrender.com/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question: text })
    });

    const data = await res.json();
    output.textContent = data.answer;
  } catch (e) {
    console.error(e);
    output.textContent = "шибка связи с Ягой";
  }
}

console.log("YAGA frontend ready");
