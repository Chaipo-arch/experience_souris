"""
Fecal data analysis.

This module creates a line plot showing live bacteria
over time for fecal samples.
"""

import math
import os
import matplotlib.pyplot as plt


def process_fecal_data(data, output_dir, img_dir):
    """
    Filter fecal samples and generate:
    - a CSV file
    - a line plot (one line per mouse)
    """

    # Keep only fecal samples
    fecal_samples = [
        d for d in data
        if d.get("sample_type", "").lower() == "fecal"
    ]

    if not fecal_samples:
        print("No fecal data found")
        return

    mice = {}
    csv_rows = []

    for entry in fecal_samples:
        try:
            mouse_id = entry.get("mouse_ID", "")
            treatment = entry.get("treatment", "")
            day = float(entry.get("experimental_day", 0))
            raw_value = float(entry.get("counts_live_bacteria_per_wet_g", 0))
            log_value = math.log10(raw_value) if raw_value > 0 else 0
        except (ValueError, TypeError):
            continue

        csv_rows.append([mouse_id, treatment, day, log_value])

        if mouse_id not in mice:
            mice[mouse_id] = {
                "x": [],
                "y": [],
                "treatment": treatment
            }

        mice[mouse_id]["x"].append(day)
        mice[mouse_id]["y"].append(log_value)

    # Plot
    plt.figure(figsize=(10, 6))

    for mouse in mice.values():
        points = sorted(zip(mouse["x"], mouse["y"]))
        x = [p[0] for p in points]
        y = [p[1] for p in points]

        color = "red" if mouse["treatment"].upper() == "ABX" else "blue"
        plt.plot(x, y, color=color, alpha=0.5)

    plt.title("Fecal live bacteria")
    plt.xlabel("Washout day")
    plt.ylabel("log10(live bacteria / wet g)")
    plt.grid(True)

    img_path = os.path.join(img_dir, "fecal_plot.png")
    plt.savefig(img_path)
    plt.close()

    print(f"Fecal plot saved: {img_path}")
