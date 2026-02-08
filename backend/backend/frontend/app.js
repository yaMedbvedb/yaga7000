async function send() {
  const input = document.getElementById("input").value;
  const output = document.getElementById("output");

  output.textContent = "Агент думает...";

  const res = await fetch("http://127.0.0.1:8000/api/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: input })
  });

  const data = await res.json();
  output.textContent = data.response;
}
