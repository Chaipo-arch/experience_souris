
---

# 🧫 Microbiome Data Analysis Project

## Overview

This project analyzes microbiome data from mice. It reads CSV files containing bacterial counts from different sample types (fecal, cecal, ileal) and generates **plots** and **CSV outputs** for each type.

---

## 🔹 Features

* Reads CSV data automatically, detects delimiters (`;` or `,`)
* Processes **fecal data** and generates **line plots** over time
* Processes **organ data** (cecal and ileal) and generates **violin plots** to compare Placebo vs ABX treatments
* Saves filtered data in CSV files
* Creates all necessary folders automatically
* Fully modular and commented for beginners

---

## 📂 Project Structure

```text
project/
│
├── main.py              # Entry point for running the analysis
├── config.py            # Configuration for input/output paths and filenames
├── io_utils.py          # Functions to read/write CSV files and create folders
├── fecal_analysis.py    # Functions to process and plot fecal data
├── organ_analysis.py    # Functions to process and plot organ data (cecal & ileal)
├── input/               # Folder for input CSV files
├── output/              # Folder where CSV outputs are saved
└── images/              # Folder where plots are saved
```

---

## ⚙️ Installation & Requirements

1. **Python 3.10+** is required.
2. Install required packages:

```bash
pip install matplotlib
```

3. Place your CSV files in the `input/` folder.

---

## 📝 CSV File Format

Your CSV should include at least the following columns:

* `mouse_ID` → unique identifier for each mouse
* `sample_type` → type of sample (`fecal`, `cecal`, `ileal`)
* `treatment` → treatment applied (`Placebo` or `ABX`)
* `experimental_day` → day of the experiment (integer)
* `counts_live_bacteria_per_wet_g` → bacterial count

> Example:

```csv
mouse_ID;sample_type;treatment;experimental_day;counts_live_bacteria_per_wet_g
M1;fecal;ABX;1;12000
M2;cecal;Placebo;1;8000
```

---

## 🚀 How to Run

Run the main script:

```bash
python main.py
```

### What happens when you run it:

1. The program checks and creates necessary folders (`output/`, `images/`)
2. It reads the input CSV file
3. Generates:

   * **Fecal line plot** and CSV
   * **Cecal violin plot** and CSV
   * **Ileal violin plot** and CSV
4. Saves outputs in `output/` and `images/`

---

## 📊 Output

### CSV Files

* `fecal_data.csv` → all fecal samples with log10 counts
* `cecal_data.csv` → all cecal samples with log10 counts
* `ileal_data.csv` → all ileal samples with log10 counts

### Images

* `images/fecal_plot.png` → line plot of fecal bacteria
* `images/cecal_plot.png` → violin plot of cecal bacteria
* `images/ileal_plot.png` → violin plot of ileal bacteria

---

## 🖼️ Plots Explained

### Fecal Plot (Line Plot)

* Each mouse has a line showing bacterial counts over time
* Red = ABX treatment, Blue = Placebo
* X-axis = experimental day, Y-axis = log10(live bacteria per wet gram)

### Organ Plots (Violin Plot)

* Compares treatments at a single experimental day
* Blue = Placebo, Red = ABX
* Shows median values and distribution of bacterial counts

---

## 🧩 How the Code is Structured

* **config.py** → All settings (input/output paths, filenames)
* **io_utils.py** → Handles folder creation, reading and writing CSVs
* **fecal_analysis.py** → Fecal-specific processing & line plots
* **organ_analysis.py** → Organ-specific processing & violin plots
* **main.py** → Coordinates everything

---

## 💡 Notes

* Make sure your CSV file has **no extra spaces** in headers for best results
* The program automatically handles missing or invalid data
* All numeric data is converted to **log10** scale before plotting
* You can change `INPUT_FILE` in `config.py` to analyze a different CSV

---

## 📈 Example Workflow

1. Put `data_medium.csv` in `input/`
2. Run `python main.py`
3. Check `output/` for CSV results
4. Check `images/` for plots
