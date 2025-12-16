"""
Input / Output utilities.

This module handles:
- Folder creation
- Reading CSV files
- Writing CSV output files
"""

import csv
import os


def ensure_directories(output_dir, img_dir):
    """
    Create output folders if they do not exist.

    This avoids errors when saving files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(img_dir):
        os.makedirs(img_dir)


def read_csv_data(input_dir, filename):
    """
    Read a CSV file and return a list of dictionaries.

    Each row of the CSV becomes one dictionary:
    {
        "column_name": "value"
    }

    The delimiter (',' or ';') is detected automatically.
    """
    data = []
    path = os.path.join(input_dir, filename)

    try:
        with open(path, "r", encoding="utf-8") as csvfile:
            sample = csvfile.read(4096)
            csvfile.seek(0)

            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter

            print(f"Detected CSV delimiter: '{delimiter}'")

            reader = csv.DictReader(csvfile, delimiter=delimiter)
            print("Detected columns:", reader.fieldnames)

            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []

    except Exception as e:
        print(f"Error while reading CSV: {e}")
        return []

    print(f"Loaded {len(data)} rows")
    return data


def save_csv(output_dir, filename, header, rows):
    """
    Save a CSV file in the output directory.
    """
    path = os.path.join(output_dir, filename)

    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Saved file: {path}")
