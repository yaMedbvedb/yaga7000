const API_URL = "https://yaga7000-backend.onrender.com/api/ask";
console.log("🟢 YAGA7000 script loaded");


async function askYaga() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");

  const message = input.value.trim();
  if (!message) return;

  output.innerText = "🧙‍♀️ Яга думает...";

  try {
    const response = await fetch("https://yaga7000-backend.onrender.com/api/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    console.log("RAW RESPONSE:", response);

    const data = await response.json();
    console.log("JSON DATA:", data);

    if (data && data.response) {
      output.innerText = data.response;
    } else {
      output.innerText = "⚠️ Ответ получен, но поле response пустое";
    }

  } catch (err) {
    console.error("FETCH ERROR:", err);
    output.innerText = "🔥 Ошибка связи с Ягой";
  }
}
