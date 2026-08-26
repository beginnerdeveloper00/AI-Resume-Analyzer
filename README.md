# 🤖 AI Resume Analyzer

An AI-powered resume analyzer that evaluates resume quality, compares resumes with job descriptions, identifies matching and missing skills, and provides actionable improvement suggestions.

## 🚀 Live Demo

👉 [AI Resume Analyzer - Live Demo](https://ai-resume-analyzer-pfcyhmylf3kulzm6tgwtwr.streamlit.app/)

## ✨ Features

- 📄 Upload resume in PDF format
- 📊 Resume quality score
- 🎯 ATS match score
- ✅ Matching skills detection
- ❌ Missing skills detection
- 💡 Resume improvement suggestions
- 📝 Extract resume text from PDF
- 🔍 Compare resume with job description
- 📌 Identify important resume sections
- 📈 Highlight quantified achievements

## 🛠️ Tech Stack

- 🐍 Python
- 🎈 Streamlit
- 📄 PyMuPDF
- 🐼 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 🧠 Natural Language Processing (NLP)
- 🔧 Git & GitHub

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── screenshots/
│   ├── home.png
│   └── results.png
│
└── utils/
    ├── matcher.py
    ├── pdf_parser.py
    └── resume_analyzer.py
```

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 📊 Resume Analysis Results

![Resume Analysis Results](screenshots/results.png)

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/beginnerdeveloper00/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🔄 How It Works

1. 📄 Upload your resume in PDF format.
2. 📝 The application extracts text from the resume.
3. 🔍 Resume sections and important information are analyzed.
4. 🎯 The resume is compared with the provided job description.
5. ✅ Matching skills are identified.
6. ❌ Missing skills are detected.
7. 📊 Resume quality and ATS match scores are calculated.
8. 💡 Improvement suggestions are generated.

## 📊 Analysis Output

The application provides:

| Analysis | Description |
|---|---|
| Resume Quality | Evaluates the presence of important resume sections |
| ATS Match Score | Measures how well the resume matches the job description |
| Matching Skills | Skills found in both the resume and job description |
| Missing Skills | Relevant skills missing from the resume |
| Improvement Suggestions | Suggestions to improve resume relevance |

## 🎯 Use Cases

- 👨‍💻 Students preparing for placements
- 🎓 Freshers looking for jobs
- 💼 Job seekers optimizing resumes
- 📋 Candidates preparing ATS-friendly resumes
- 🔎 Comparing resumes with specific job descriptions

## 🔮 Future Improvements

- 🤖 Integration with advanced Large Language Models (LLMs)
- 📑 Support for DOCX resumes
- 🎨 Improved resume formatting analysis
- 📊 Advanced ATS scoring
- 💼 Job-role specific recommendations
- 📈 Resume score history and comparison
- ☁️ Additional deployment options

## 📌 Project Highlights

This project demonstrates practical experience with:

- Python application development
- Streamlit web application development
- PDF text extraction
- Natural Language Processing
- Resume parsing and analysis
- Text matching
- Machine Learning techniques
- Git and GitHub
- Application deployment

## 👨‍💻 Author

**Md. Salman**

GitHub: [beginnerdeveloper00](https://github.com/beginnerdeveloper00)

---

⭐ If you find this project useful, consider giving it a star!