# STA Assignment 6
questions = [
    "How do you import an SDF into your STA tool for gate-level sign-off?",
    "Explain when to use “min” vs. “max” SDF in back-annotation.",
    "Show how you ensure your SDF corner aligns with STA corner volt/temp.",
    "How do you map flat SDF names into a hierarchical design?",
    "After an ECO buffer insertion, what’s different in the incremental run command?",
    "How do you limit incremental STA to only affected endpoints?",
    "What checks ensure your ECO didn’t introduce new violations?",
    "Which reports change most after SDF back-annotation?",
    "How reconcile delays reported in STA vs. SDF-based simulation?",
    "After ECO, derating factors may shift. How to reapply selectively?",
    "You insert a clock buffer as ECO. How re-generate uncertainty budgets?",
    "What is “slip-mode” incremental and when is it used?",
    "Manage multiple SDF files for different corners in one script.",
    "List five critical checks after an ECO-based incremental STA.",
    "Explain why incremental ECO slack is tighter than full-chip slack.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
