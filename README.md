# Bacterial Microbiota Analysis - Python Project

## Project Description

This project analyzes the impact of antibiotic treatment on bacterial microbiota in mice at the beginning of their life. The program processes experimental data from CSV files and automatically generates graphs and filtered datasets.

The experiment compares two groups of mice:
- **ABX group**: Treated with antibiotics
- **Placebo group**: Control group without antibiotic treatment

All mice start the experimental phase at day 14 of life, receive treatment for 7 consecutive days, and enter the washout phase at day 21.

## Project Structure

```
project_root/
│
├── file.py                 # Main Python script
├── README.md              # This file
│
├── input/                 # Input folder (CSV data files)
│   ├── data_small.csv
│   ├── data_medium.csv
│   ├── data_large.csv
│   └── data_huge.csv
│
├── output/                # Output folder (filtered CSV files - auto-generated)
│   ├── fecal_data.csv
│   ├── cecal_data.csv
│   └── ileal_data.csv
│
└── images/                # Images folder (generated graphs - auto-generated)
    ├── fecal_plot.png
    ├── cecal_plot.png
    └── ileal_plot.png
```

## Prerequisites

- **Python 3.x** (tested with Python 3.13+)
- **Required libraries**:
  - `matplotlib`

### Installation of Dependencies

```bash
pip install matplotlib
```

## Usage Instructions

### 1. Prepare Input Data

1. Place your CSV data file in the `input/` folder
2. The CSV file should follow the standard structure with these columns:
   - mouse_strain
   - experiment_ID
   - sample_type
   - timepoint
   - mouse_ID
   - treatment
   - frequency_live_bacteria_%
   - experimental_day
   - counts_live_bacteria_per_wet_g
   - mouse_age_days
   - mouse_sex

### 2. Configure the Script

Open `file.py` and modify line 10 to specify your input file:

```python
INPUT_FILE = 'data_medium.csv'  # Change to your filename
```

### 3. Run the Program

```bash
python file.py
```

### 4. Check Results

After execution:
- **3 PNG graphs** will be generated in the `images/` folder
- **3 CSV files** with filtered data will be generated in the `output/` folder

## Generated Outputs

### Graphs

1. **fecal_plot.png**: Line chart showing bacterial counts over time in fecal samples
   - One line per mouse
   - Blue lines = Placebo group
   - Red lines = ABX group
   - X-axis: Washout day (experimental_day)
   - Y-axis: log10(live bacteria/wet g)

2. **cecal_plot.png**: Violin plot showing bacterial distribution in cecal samples
   - Displays both Placebo and ABX groups
   - Taken at the first available experimental day for organ samples

3. **ileal_plot.png**: Violin plot showing bacterial distribution in ileal samples
   - Same format as cecal plot

### Filtered CSV Files

1. **fecal_data.csv**: Contains mouse_id, treatment, experimental_day, log10_count for fecal samples
2. **cecal_data.csv**: Contains mouse_id, treatment, log10_count for cecal samples
3. **ileal_data.csv**: Contains mouse_id, treatment, log10_count for ileal samples

All output CSV files use semicolon (`;`) as delimiter.

## Features Implemented

### ✅ Core Features
- [x] Automatic CSV parsing with delimiter detection (`,` or `;`)
- [x] Dynamic handling of variable number of mice
- [x] Dynamic handling of variable number of experimental days
- [x] Case-insensitive treatment matching (ABX, abx, Placebo, placebo)
- [x] Automatic directory creation (output/ and images/)
- [x] Log10 transformation of bacterial counts
- [x] Color-coded visualization (Blue = Placebo, Red = ABX)

### ✅ Graphs
- [x] Fecal line plot with all mice trajectories
- [x] Cecal violin plot with distribution visualization
- [x] Ileal violin plot with distribution visualization
- [x] Proper titles, labels, legends, and units on all graphs
- [x] Scatter points overlaid on violin plots for detail
- [x] Grid lines for better readability

### ✅ Data Processing
- [x] Filtering by sample_type (fecal, cecal, ileal)
- [x] Filtering by experimental_day for organ samples
- [x] Handling of missing or invalid data
- [x] Export of filtered data to CSV

## Functional Limitations

### ⚠️ Known Limitations

1. **Scientific Notation Handling**
   - The program correctly handles scientific notation (e.g., `1.27E+09`) in CSV files
   - However, values must be in standard scientific notation format
   - Non-standard formats may cause parsing errors

2. **Experimental Day for Organ Samples**
   - The program automatically uses the **first available experimental day** for cecal and ileal samples
   - In the current datasets, this is typically day 1
   - If your data has organ samples at multiple days, only the first day will be used
   - **Workaround**: Manually modify line 166 in the code to specify a different target day

3. **Empty Treatment Groups**
   - If a dataset has only ABX or only Placebo samples for organ plots, the graph will still display both labels on the x-axis
   - The violin plot will only show data for the group(s) present
   - This is intentional for consistency across graphs

4. **Performance with Very Large Files**
   - Files with 500,000+ rows (like `data_huge.csv`) may take 10-30 seconds to process
   - Memory usage increases linearly with file size
   - No progress bar is implemented
   - **Limitation**: The entire CSV is loaded into memory at once

5. **Error Handling**
   - Invalid numeric values are silently skipped
   - No detailed error reporting for malformed CSV rows
   - If a CSV has structural issues (wrong number of columns), processing may fail without clear error messages

6. **Column Name Flexibility**
   - Column names must match exactly (after stripping whitespace): `mouse_ID`, `sample_type`, etc.
   - Alternative column names are not supported
   - **Workaround**: Rename columns in your CSV to match the expected format

7. **Output Overwriting**
   - Each run overwrites previous output files without warning
   - No backup or versioning of outputs
   - **Workaround**: Manually copy output files to another location before re-running

8. **Encoding Issues**
   - The program uses UTF-8 encoding
   - Files with other encodings (e.g., Latin-1, Windows-1252) may cause errors
   - **Workaround**: Convert your CSV to UTF-8 before processing

9. **Missing Data Handling**
   - Rows with zero or negative bacterial counts are converted to log10(0) = 0
   - This may not be scientifically accurate (should be undefined or -infinity)
   - Missing values (empty cells) are treated as 0
   - **Limitation**: No distinction between "zero bacteria" and "missing measurement"




---

**Last Updated**: December 2024  
**Version**: 1.0
