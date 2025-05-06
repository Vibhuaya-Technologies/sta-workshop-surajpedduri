# STA Assignment 2
questions = [
    "With clock jitter = 0.05 ns and insertion skew = 0.12 ns, how do you adjust the effective period for setup checks?",
    "You have 0.2 ns total uncertainty budget. Propose a split between on-chip clock distribution and external PLL.",
    "A 50 MHz clock’s high phase shrinks to 48%. How does that impact both setup and hold analyses?",
    "Two launch paths see clock early by 0.1 ns, two capture paths see clock late by 0.15 ns. Compute worst slack.",
    "If launch edge varies ±0.08 ns, derive the formula for adjusted setup and hold margins.",
    "Given a tree with max skew 0.25 ns across leaf nodes, how do you incorporate this in timing budgets?",
    "Explain how uncertain handshake clocks affect cross-domain data paths beyond standard setup/hold.",
    "You over-budget skew by 0.05 ns. What immediate impact on the most critical 10% of paths?",
    "A slow clock driver causes 0.03 ns additional uncertainty; quantify its timing impact.",
    "How do you handle an intentionally 40/60 duty cycle in your SDC constraints for setup and hold?",
    "You must derate clock nets by 5% for variation. Show the new uncertainty-adjusted period.",
    "A local PLL adds 0.04 ns rms jitter. Convert this into peak uncertainty for STA.",
    "Compare uncertainty implications of shared bus clock vs. dedicated routed clock to each block.",
    "Adding a clock buffer reduces skew but increases insertion delay. Analyze net effect on slack.",
    "Outline how you would verify your chosen uncertainty budget post-layout.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
