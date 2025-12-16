"""
Main entry point of the program.

This file orchestrates the full analysis.
"""

from config import INPUT_DIR, OUTPUT_DIR, IMG_DIR, INPUT_FILE
from io_utils import ensure_directories, read_csv_data
from fecal_analysis import process_fecal_data
from organ_analysis import process_organ_data


def main():
    print("Starting analysis")

    ensure_directories(OUTPUT_DIR, IMG_DIR)

    data = read_csv_data(INPUT_DIR, INPUT_FILE)
    if not data:
        print("No data to process")
        return

    process_fecal_data(data, OUTPUT_DIR, IMG_DIR)
    process_organ_data(data, "cecal", OUTPUT_DIR, IMG_DIR)
    process_organ_data(data, "ileal", OUTPUT_DIR, IMG_DIR)

    print("Analysis complete")


if __name__ == "__main__":
    main()
