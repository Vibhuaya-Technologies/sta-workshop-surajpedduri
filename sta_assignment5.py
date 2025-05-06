# STA Assignment 5
questions = [
    "Compare “lumped” vs. “true” OCV approaches. Which is more pessimistic?",
    "You need 3% derating on data nets, 1% on clocks. How and where do you apply these?",
    "Why might you derate rise nets differently than fall nets? Give an SDC snippet.",
    "Outline the workflow for a QuickStat run vs. a Classic STA run.",
    "You want 6σ coverage—how do you derive the added guardband?",
    "Explain how spatial PV variation across die is modeled in STA.",
    "Compare worst-case corner + OCV vs. an SPICE-based Monte Carlo sample.",
    "At hot-spot conditions you require extra derating. How do you script conditional derating?",
    "A new high-Vt cell library has different variation tables. Show how to swap libs per corner.",
    "How do transistor finger count changes reflect in OCV modeling?",
    "In a top-level block set global OCV; in leaf set local. How to set that up?",
    "Low-power mode uses 2% more guardband. How override mode-specific derates?",
    "Show how to report nominal vs. worst-case slack side by side.",
    "Why can OCV flip a hold-clean path into a violation? Illustrate with numbers.",
    "Differentiate derating strategies pre-ECO vs. post-sign-off.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
