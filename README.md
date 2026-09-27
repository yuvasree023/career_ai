# 🚀 Career AI - Resume Optimizer & ATS Enhancer

An AI-powered Resume Optimizer and ATS (Applicant Tracking System) Analyzer built with **Streamlit**, **Groq (Llama 3.3 70B)**, and **PyMuPDF**.

Tailor your resume to any job description, bridge keyword and skill gaps, rewrite impact bullets using the **STAR** method, and optimize your ATS match score in seconds.

---

## ✨ Features

- **📄 Smart PDF Parsing:** Extracts clean text from resume PDFs using PyMuPDF (`fitz`).
- **🎯 Job Description Alignment:** Pinpoints missing skills, technical qualifications, and domain keywords.
- **⭐ STAR Method Bullet Rewriting:** Rewrites experience bullets with high-impact Situation, Task, Action, and Result framing.
- **📊 ATS Scoring & Feedback:** Evaluates resume-to-job match rate and delivers actionable improvement recommendations.
- **🎨 Modern Interactive UI:** Clean, responsive pastel interface built with Streamlit.
- **💻 Dual Mode:** Run either as a full interactive **Streamlit Web Application** or as a lightweight **CLI Script**.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** (Web Application framework)
- **Groq Cloud API** (Llama 3.3 70B Versatile LLM for high-speed inference)
- **PyMuPDF (`fitz`)** (PDF extraction & manipulation)
- **python-dotenv** (Environment variable management)

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yuvasree023/career_ai.git
cd career_ai
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit pymupdf groq python-dotenv
```

### 4. Configure Your API Key
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
> Get a free API key from [Groq Console](https://console.groq.com/).

---

## 🚀 Running the Project

### Option A: Web App (Streamlit)
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### Option B: Command Line Interface (CLI)
```bash
python optimizer.py
```
Follow the interactive prompts to load your resume PDF, paste the job description, and generate an optimized resume.

---

## 📁 Project Structure

```
├── app.py                # Streamlit web application
├── optimizer.py          # Standalone CLI resume optimizer script
├── .env                  # API keys and environment variables (ignored by Git)
├── .gitignore            # Excluded files and folders
└── README.md             # Project documentation
```

---

## 🔒 Security & Privacy

- Sensitive credentials like `GROQ_API_KEY` are read exclusively from environment variables / `.env`.
- Ensure your `.env` file is never committed to version control.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
