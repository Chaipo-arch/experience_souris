"""
Organ data analysis (cecal and ileal).

This module creates violin plots to compare
live bacteria counts between treatments (Placebo vs ABX)
for a given organ.
"""

import math
import os
import matplotlib.pyplot as plt
import numpy as np


def process_organ_data(data, organ_name, output_dir, img_dir):
    """
    Create a violin plot for one organ (cecal or ileal).

    Parameters:
    - data: list of dictionaries (CSV rows)
    - organ_name: "cecal" or "ileal"
    - output_dir: folder where CSV files are saved
    - img_dir: folder where images are saved
    """

    # Select only rows corresponding to the given organ
    organ_samples = [
        row for row in data
        if row.get("sample_type", "").lower() == organ_name.lower()
    ]

    if not organ_samples:
        print(f"No {organ_name} samples found")
        return

    # Identify all experimental days present in the organ data
    experimental_days = sorted(
        set(row.get("experimental_day", "") for row in organ_samples)
    )

    print(
        f"{organ_name.capitalize()} samples found at day(s): {experimental_days}"
    )

    # Use the first available experimental day
    # (usually day 1 for organ samples)
    target_day = experimental_days[0]

    # Keep only samples from the selected day
    day_samples = [
        row for row in organ_samples
        if row.get("experimental_day", "") == target_day
    ]

    print(
        f"Using experimental day {target_day} "
        f"({len(day_samples)} samples)"
    )

    placebo_values = []
    abx_values = []
    csv_rows = []

    # Extract numeric values
    for row in day_samples:
        try:
            raw_value = float(
                row.get("counts_live_bacteria_per_wet_g", 0)
            )
            log_value = math.log10(raw_value) if raw_value > 0 else 0
        except (ValueError, TypeError):
            continue

        treatment = row.get("treatment", "")
        mouse_id = row.get("mouse_ID", "")

        csv_rows.append([mouse_id, treatment, log_value])

        if treatment.lower() == "placebo":
            placebo_values.append(log_value)
        elif treatment.upper() == "ABX":
            abx_values.append(log_value)

    if not csv_rows:
        print(f"No valid data for {organ_name}")
        return

    print(
        f"{organ_name.capitalize()} - "
        f"Placebo: {len(placebo_values)} | "
        f"ABX: {len(abx_values)}"
    )

    # Save extracted data to CSV
    csv_path = os.path.join(output_dir, f"{organ_name}_data.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        import csv
        writer = csv.writer(csvfile)
        writer.writerow(["mouse_id", "treatment", "log10_count"])
        writer.writerows(csv_rows)

    print(f"Saved CSV: {csv_path}")

    # ---- Create the violin plot ----

    plt.figure(figsize=(8, 6))

    plot_data = []
    positions = []
    colors = []

    # Always keep fixed x positions:
    # 1 = Placebo, 2 = ABX
    if placebo_values:
        plot_data.append(placebo_values)
        positions.append(1)
        colors.append("blue")

    if abx_values:
        plot_data.append(abx_values)
        positions.append(2)
        colors.append("red")

    if plot_data:
        parts = plt.violinplot(
            plot_data,
            positions=positions,
            showmeans=False,
            showmedians=True
        )

        # Style each violin
        for i, body in enumerate(parts["bodies"]):
            body.set_facecolor(colors[i])
            body.set_edgecolor("black")
            body.set_alpha(0.5)

        # Add individual data points (scatter)
        for i, values in enumerate(plot_data):
            x = np.random.normal(
                positions[i], 0.04, size=len(values)
            )
            plt.scatter(x, values, alpha=0.6, color=colors[i])

    # X-axis always shows both treatments
    plt.xticks([1, 2], ["Placebo", "ABX"])
    plt.xlim(0.5, 2.5)

    plt.title(f"{organ_name.capitalize()} live bacteria")
    plt.xlabel("Treatment")
    plt.ylabel("log10(live bacteria / wet g)")
    plt.grid(axis="y", alpha=0.3)

    img_path = os.path.join(img_dir, f"{organ_name}_plot.png")
    plt.savefig(img_path, dpi=150)
    plt.close()

    print(f"Saved plot: {img_path}")
