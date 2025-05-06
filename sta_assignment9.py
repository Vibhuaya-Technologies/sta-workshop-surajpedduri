# STA Assignment 9
questions = [
    "Contrast CDC checks vs. standard STA.",
    "A 4-phase handshake spans domains; verify both STA and CDC?",
    "Where insert a synchronizer, and exclude its internal paths from STA?",
    "How budget for MTBF-related timing slack in CDC paths?",
    "Two free-running clocks with unknown phase: how constrain?",
    "Write SDC to false-path crossing clock domains.",
    "Ensure CDC checks under voltage/temp corners.",
    "Constrain multi-cycle handshake across clocks.",
    "For a 32-bit bus CDC vs single-bit differences?",
    "Classify and fix 200 CDC violations approach.",
    "When to use formal CDC vs. STA?",
    "Constrain multi-rate path for 200/300 MHz clocks.",
    "Constrain CDC path through black-box IP.",
    "Check generated-clock CDC crossing domain.",
    "List three CDC-related check flags for your STA tool.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
