const API_URL = "https://yaga7000-backend.onrender.com/api/ask";
console.log("🟢 YAGA7000 script loaded");

async function askYaga() {
  const input = document.getElementById("input");
  const output = document.getElementById("output");

  const message = input.value.trim();
  if (!message) return;

  output.innerText = "🧙‍♀️ Яга думает...";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    console.log("JSON DATA:", data);

    output.innerText = data.response || "⚠️ Яга молчит";
  } catch (err) {
    console.error(err);
    output.innerText = "🔥 Ошибка связи с Ягой";
  }
}
