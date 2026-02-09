async function askYaga() {
  const input = document.getElementById("questionInput");
  const output = document.getElementById("answer");

  if (!input || !input.value.trim()) {
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
      body: JSON.stringify({
        question: input.value.trim()
      })
    });

    if (!res.ok) {
      throw new Error("HTTP " + res.status);
    }

    const data = await res.json();
    output.textContent = data.answer;
  } catch (e) {
    console.error(e);
    output.textContent = "шибка связи с сервером";
  }
}

console.log("YAGA frontend ready");
