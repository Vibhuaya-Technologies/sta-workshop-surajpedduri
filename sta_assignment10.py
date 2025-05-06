# STA Assignment 10
questions = [
    "Explain how IR-aware timing uses voltage profiles in delay calculation.",
    "How model crosstalk in STA for a victim net worst-case scenario?",
    "Explain EM-induced resistance change effect on timing over time.",
    "Use switching activity data to refine STA scenarios.",
    "Translate a 20% overshoot into timing margin loss.",
    "Show slack impact of 5-year process drift reducing speed by 2%.",
    "Adjust STA corner definitions for AVS across PVT.",
    "Integrate an ML model to predict worst-case path delay.",
    "Partition timing regions for a 30 °C hotspot gradient.",
    "Include through-silicon-via delays in 3D-IC STA.",
    "Adapt STA for optical clock distribution with negligible jitter.",
    "How might STA change for QCA-based gates?",
    "Capture analog noise margin assignments in STA.",
    "Model soft-error recovery timing after ECC.",
    "Write SDC for a 3-phase clock network (φ1/φ2/φ3).",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
