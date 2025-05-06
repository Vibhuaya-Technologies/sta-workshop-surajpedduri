import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("STA Assignment Scoring")

st.sidebar.header("Upload CSV Files")
answer_file = st.sidebar.file_uploader("Answer Key CSV", type="csv")
response_file = st.sidebar.file_uploader("Student Responses CSV", type="csv")

if answer_file and response_file:
    df_key = pd.read_csv(answer_file)
    df_resp = pd.read_csv(response_file)
    df = pd.merge(df_resp, df_key, on="QuestionID", how="left")

    def grade_numeric(resp, key, tol):
        try:
            s, k, e = float(resp), float(key), float(tol)
            diff = abs(s - k)
            return 1.0 if diff <= e else (0.5 if diff <= 2*e else 0.0)
        except:
            return 0.0

    def grade_conceptual(resp, keywords):
        resp_l = str(resp).lower()
        keys = [kw.strip().lower() for kw in str(keywords).split(';') if kw.strip()]
        return sum(1 for kw in keys if kw in resp_l) / len(keys) if keys else 0.0

    def grade_formula(resp, key):
        return 1.0 if str(key).lower() in str(resp).lower() else 0.0

    def compute_score(row):
        at = str(row['AnswerType']).lower(); w = float(row['Weight'])
        if at == 'numeric':
            base = grade_numeric(row['Response'], row['KeyAnswer'], row['Tolerance'])
        elif at == 'conceptual':
            base = grade_conceptual(row['Response'], row['Keywords'])
        elif at == 'formula':
            base = grade_formula(row['Response'], row['KeyAnswer'])
        else:
            base = 0.0
        return base * w

    df['Score'] = df.apply(compute_score, axis=1)
    report = df.groupby('StudentID').agg(Total=('Score','sum'),
                                         Max=('Weight','sum')).reset_index()
    report['Percent'] = report['Total']/report['Max']*100

    st.subheader("Scores by Student")
    st.dataframe(report)

    q_perf = df.groupby('QuestionID').Score.mean().reset_index()
    st.subheader("Avg Score per Question")
    fig, ax = plt.subplots()
    ax.bar(q_perf['QuestionID'].astype(str), q_perf['Score'])
    st.pyplot(fig)

    csv = report.to_csv(index=False).encode()
    st.download_button("Download Report", csv, "report.csv", "text/csv")
else:
    st.info("Upload both files to get started.")
