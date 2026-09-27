import fitz  # pymupdf
import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("Set GROQ_API_KEY in the environment before running the optimizer.")
client = Groq(api_key=api_key)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def optimize_resume(resume_text, job_description):
    prompt = f"""You are an expert resume coach. 

Analyze this resume against the job description and do the following:
1. Identify missing skills or keywords
2. Rewrite ALL bullet points using the STAR method (Situation, Task, Action, Result)
3. Suggest improvements to make it stronger

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Format your response like this:
## MISSING SKILLS
(list them here)

## IMPROVEMENTS NEEDED
(list them here)

## OPTIMIZED RESUME
(full rewritten resume here)
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- MAIN PROGRAM ---
print("=== RESUME OPTIMIZER ===\n")

# Step 1: Get PDF path
pdf_path = input("Enter the full path to your resume PDF: ").strip()

# Step 2: Extract text
print("\nReading your resume...")
resume_text = extract_text_from_pdf(pdf_path)
print("Resume loaded successfully!")

# Step 3: Get job description
print("\nPaste the job description below.")
print("When done, press Enter twice:\n")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
job_description = "\n".join(lines)

# Step 4: Optimize
print("\nOptimizing your resume... please wait...")
result = optimize_resume(resume_text, job_description)

# Step 5: Save output
output_file = "optimized_resume.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result)

print(f"\n✅ Done! Your optimized resume saved to: {output_file}")
input("\nPress Enter to exit...")