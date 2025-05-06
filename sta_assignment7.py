# STA Assignment 7
questions = [
    "List pros/cons of hierarchical vs. flat STA for a 10M-cell SoC.",
    "How do you constrain timing at IP boundaries in a hierarchical run?",
    "Explain how flat STA reports differ from hierarchical for the same path.",
    "You must false-path through a hard macro; how differs by flow?",
    "In hierarchical mode, where do you collect all child SDCs?",
    "Quantify runtime/memory savings for hierarchical on a 500k-cell block.",
    "How ensure clock budgets top-down in a hierarchical tree?",
    "If child blocks use different mode settings, how coordinate parent constraints?",
    "Show how to treat isolation cells in hierarchical vs. flat runs.",
    "How does ECO insertion differ in hierarchical incremental?",
    "A violating path crosses two levels. How trace in hierarchical report?",
    "What inaccuracies arise when black-boxing leaf modules?",
    "Recommend tools to visualize hierarchical timing results.",
    "How sync async domains across levels in hierarchical STA?",
    "Outline a script to merge block reports into one summary.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
