import express from "express";
import multer from "multer";
import fs from "fs";
import cors from "cors";

const PORT = 3000;

const app = express();
const upload = multer({ dest: "uploads/" });
app.use(cors());
app.use(express.json());

// Function to analyze text
const analyzeText = (text) => ({
  lines: text.split("\n").length,
  words: text.match(/\S+/g)?.length || 0,
  characters: text.length,
  bytes: Buffer.byteLength(text, "utf-8"),
});

// Endpoint for text input
app.post("/analyze-text", (req, res) => {
  const { text } = req.body;
  if (!text) return res.status(400).json({ error: "No text provided" });
  res.json(analyzeText(text));
});

// Endpoint for file uploads
app.post("/upload", upload.single("file"), (req, res) => {
  if (!req.file) return res.status(400).json({ error: "No file uploaded" });
  const fileContent = fs.readFileSync(req.file.path, "utf-8");
  fs.unlinkSync(req.file.path); // Cleanup uploaded file
  res.json(analyzeText(fileContent));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
