import { useState } from "react";

export default function CCWC() {
  const [text, setText] = useState("");
  const [output, setOutput] = useState([]);

  const handleAnalyze = async (inputText) => {
    const response = await fetch("http://localhost:3000/analyze-text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: inputText }),
    });
    const result = await response.json();
    setOutput([
      `$ Lines: ${result.lines}`,
      `$ Words: ${result.words}`,
      `$ Characters: ${result.characters}`,
      `$ Bytes: ${result.bytes}`,
    ]);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleAnalyze(text);
      setText("");
    }
  };

  return (
    <div className="bg-black text-green-400 font-mono p-6 w-full h-screen">
      <div className="h-full max-w-2xl mx-auto">
        <div className="mt-4">
          {output.map((line, index) => (
            <div key={index}>{line}</div>
          ))}
        </div>
        <div className="flex">
          <span className="pr-2">$</span>
          <input
            className="bg-black text-green-400 border-none outline-none flex-1"
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={handleKeyDown}
            autoFocus
          />
        </div>
        
      </div>
    </div>
  );
}
