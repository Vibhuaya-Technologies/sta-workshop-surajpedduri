# STA Assignment 1
questions = [
    "A path launches from FF1 to FF2 with: clock period = 6 ns, FF1 tCQ = 0.7 ns, comb. delay = 4.1 ns, FF2 tSU = 0.6 ns. Compute the setup slack.",
    "Using the same path as Q1, but FF2 tH = 0.3 ns and clock insertion delay = 0.15 ns, compute the hold slack.",
    "You observe two failing paths: –0.08 ns and –0.22 ns setup slack. Describe how you’d rank and attack them.",
    "If input net rise time increases by 20%, explain quantitatively how setup slack on a critical path is affected.",
    "A cell’s output slew doubles due to loading. Qualitatively, how does that change hold margin downstream?",
    "Given a 5-stage buffer chain replacing a single inverter, analyze its impact on both setup and hold slack.",
    "A reconvergent branch has one long path and one short path; only the short branch fails hold. How do you isolate and fix it?",
    "A clock-gating cell adds 0.2 ns latency in the clock path. Show its effect on both setup and hold calculations.",
    "Explain how a combinational loop can manifest as a negative hold slack and how STA tools report it.",
    "Compare timing on two paths of equal net length, one through an XOR gate, one through two serial NANDs. Which is likely slower?",
    "A net fans out to 8 endpoints vs. 16. Quantify the delta in comb delay and resulting slack change.",
    "At 125 °C vs. 25 °C, gate delays increase by 15%. Recompute setup slack for a 5 ns budget path.",
    "If rail voltage drops from 1 V to 0.9 V, and cell delays scale by 20%, what’s the new worst-case slack?",
    "Given a slow-slow corner delay 10% above typical, show its effect on a 4 ns comb path.",
    "You can add a buffer to balance two unequal paths; explain pros/cons on slack and power.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
