# STA Assignment 8
questions = [
    "Explain how time borrowing through latches affects slack calculations.",
    "How define launch vs. capture for level-sensitive latches in SDC?",
    "Describe hold analysis differences when using latches.",
    "Write constraints for a master/slave latch scheme (φ1/φ2).",
    "You allow up to 0.5 ns borrowing per latch stage; enforce this?",
    "If latch enable line has 0.1 ns jitter, incorporate into checks.",
    "How to false-path certain latch-transparent chains?",
    "In a hybrid FF/latch design, set constraints for both types?",
    "How to capture asynchronous latch release in STA?",
    "Show SDC for a 2-cycle loan in latch-based path.",
    "What STA risks arise from data-dependent clocking?",
    "Include reset timing in STA for reset-first latches?",
    "Walk through timing for path spanning φ1 to φ2 through latches.",
    "Which report flags negative borrowing and interpretation?",
    "How does gating a latch clock differ from gating an FF clock?",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
