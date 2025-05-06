# STA Assignment 3
questions = [
    "Constrain a path to use 2 cycles for arrival with SDC. Explain tool behavior vs. single-cycle.",
    "Write SDC for a path that captures data two cycles early. How is hold analysis adjusted?",
    "A glitch path through an enable signal must be false-pathed. Provide the SDC and risk analysis.",
    "Given a PLL output divided by two inside a block, write the create_generated_clock SDC.",
    "Some macros have internal loops. How do you exclude them without masking real violations?",
    "A bus uses 3-cycle launch and 2-cycle capture. How do you express this dual-mode constraint?",
    "How do you lock out STA cross-domain checks for async APB bus signals?",
    "A generated clock from a DCM has 0.1 ns added jitter. How do you code that into SDC?",
    "Want a path to complete in exactly one cycle except on reset. Show SDC and justification.",
    "A safety path only matters during testing. How to enable then disable its timing checks programmatically?",
    "Paths gated by enable pulses must be timed differently. How do you handle in SDC?",
    "A pure capture path (external stimulus) needs setup only; show how to constrain it.",
    "A path only launches on test clock edges. How is hold ignored? Provide SDC.",
    "Use of hierarchical names in a false-path constraint for a deep instance.",
    "Combine a 3-cycle constraint with a generated clock at half frequency. Write the SDC commands.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
