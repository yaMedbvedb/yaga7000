async function askYaga() {
    const input = document.getElementById("questionInput");
    const output = document.getElementById("answer");

    if (!input) {
        console.error("questionInput not found");
        return;
    }

    if (!input.value.trim()) {
        output.textContent = "???+? веди вопрос";
        return;
    }

    output.textContent = "???+? яга думает...";

    try {
        const response = await fetch(
            "https://yaga7000-backend.onrender.com/ask?question=" +
            encodeURIComponent(input.value),
            { method: "POST" }
        );

        const data = await response.json();
        output.textContent = data.answer ?? "?? ет ответа";

    } catch (err) {
        console.error(err);
        output.textContent = "? шибка св€зи с сервером";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("YAGA frontend ready");
});
