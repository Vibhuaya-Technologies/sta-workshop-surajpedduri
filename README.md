# STA Assignments Template

This repository contains:

- `assignments/sta_assignment1.py` … `sta_assignment10.py`: ten scripts of 15 STA questions each.
- `streamlit_app.py`: Streamlit scoring app.
- `responses_template.csv`: blank template for student answers.
- `requirements.txt`, `.gitignore`, `README.md`.

## Usage

1. Clone the repo:
   ```
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Install:
   ```
   pip install -r requirements.txt
   ```
3. Run your assignment:
   ```
   python assignments/sta_assignment${YOUR_NUMBER}.py > questions.txt
   ```
4. Fill `responses.csv` based on `responses_template.csv`.
5. Score locally:
   ```
   streamlit run streamlit_app.py
   ```
6. Commit & push your `responses.csv` for grading via Classroom.

