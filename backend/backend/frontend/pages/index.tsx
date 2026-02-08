import { useState } from "react";

export default function Home() {
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState("");

  const run = async () => {
    const res = await fetch("http://localhost:8000/run?goal=" + goal, {
      method: "POST"
    });
    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>YAGA7000</h1>
      <textarea
        rows={5}
        cols={50}
        onChange={e => setGoal(e.target.value)}
      />
      <br />
      <button onClick={run}>Run</button>
      <pre>{result}</pre>
    </div>
  );
}
