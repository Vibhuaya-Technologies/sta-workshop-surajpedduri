# STA Assignment 4
questions = [
    "Define two corners (“typical” 1 V/25 °C, “worst-case” 0.9 V/125 °C) in your STA flow.",
    "“Low-power” mode uses a gated clock; how do you differentiate its SDC from “normal” mode?",
    "Describe how to aggregate setup/hold reports for both modes into one unified Excel.",
    "A debug path is only active in test mode. How do you false-path it only under that mode?",
    "How does STA treat cell lib voltages vs. actual supply network analysis?",
    "Show how you’d script a “all-corners” run vs. “per-corner” runs. Pros/cons?",
    "When mode pins toggle, clock tree capacitance changes. Explain its timing implications.",
    "On-chip hotspots create local 20 °C differences. How can you model this in corner setups?",
    "Certain paths use special high-speed macros. How to assign them their own corner?",
    "Show how sign-off RC deck for worst-case vs. typical changes timing results.",
    "Derating factors differ per corner; how do you assign these in your STA tool?",
    "Multi-threaded corner runs: distribute three corners across six cores.",
    "A path launches in one mode and captures in another. How to constrain across modes?",
    "Explain how you’d incorporate IR-drop-aware delays into the worst-case corner.",
    "Sketch a YAML/JSON config that enumerates modes, corners, and their specific SDC files.",
]

def main():
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()
