#resume 
from PyPDF2 import PdfReader
import re
import matplotlib.pyplot as plt

# Extract text from PDF
def extract_text(pdf):
    reader = PdfReader(pdf)
    text = "".join(p.extract_text() or "" for p in reader.pages)
    # remove digits & punctuation, lowercase
    return re.sub(r"[\d\W]+", " ", text.lower())

# PDF path
pdf_path = r"c:\files\INDHUUUU RESUME.pdf"
text = extract_text(pdf_path)

# Keyword categories
skills = {
    "Quality": ["quality", "improve", "check", "standard", "control"],
    "Operations": ["work", "process", "production", "operation", "machine"],
    "Supply Chain": ["supply", "store", "transport", "stock", "delivery"],
    "Project Mgmt": ["plan", "time", "cost", "team", "project"],
    "Data Analytics": ["data", "analysis", "python", "numbers", "computer"],
    "Healthcare": ["health", "hospital", "doctor", "patient", "medical"]
}

# Count keyword matchesC
scores = {area: sum(text.count(word) for word in words) for area, words in skills.items()}

# Print Area scores
for area, score in scores.items():
    print(f"{area}: {score}")

# Pie chart
plt.pie(scores.values(), labels=scores.keys(), autopct="%1.0f%%")
plt.title("Resume Skill Distribution")
plt.show()
