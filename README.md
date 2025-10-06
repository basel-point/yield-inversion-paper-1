# Yield Inversion — Paper 1: FRED API Pipeline

Minimal, reproducible pipeline to pull 30Y, 10Y, 2Y, and 3M Treasury yields from FRED and compute common inversion spreads.

---

## Quick Start (Novice-Friendly)

### 1️⃣ Clone the Repository
Open Command Prompt (Windows) or Terminal (Mac), then type:  
`git clone https://github.com/syk-hub/yield-inversion-paper-1.git`  
`cd yield-inversion-paper-1`

### 2️⃣ Create a `.env` File
Inside your project folder (`yield-inversion-paper-1`), create a **new text file** named `.env`.  
Make sure the file name is exactly `.env` (with no `.txt` at the end).  

Inside this file, add one line:  
`FRED_API_KEY=your_api_key_here`  

Replace `your_api_key_here` with your actual FRED API key.  
If you don’t have one, get a free key here: [https://fredaccount.stlouisfed.org/apikey](https://fredaccount.stlouisfed.org/apikey)

### 3️⃣ Install Dependencies
In the same Command Prompt or Terminal window, type:  
`pip install pandas matplotlib python-dotenv fredapi`  

This installs the required Python packages.

### 4️⃣ Run the API Script
Navigate into the `notebook` folder and run:  
`python api_pull.py`  

This will:  
- Connect to the FRED API  
- Pull data for 30Y, 10Y, 2Y, and 3M Treasury yields  
- Compute the spreads  
- Save the results as `treasury_yields.csv`

### 5️⃣ Plot the Yield Curve Spreads
Still in the `notebook` folder, run:  
`python plot_spreads.py`  

This will:  
- Read the `treasury_yields.csv` file  
- Plot the 10Y–2Y and 10Y–3M spreads  
- Save the chart as `spreads.png`

---

## Files Overview
| File | Purpose |
|------|----------|
| `notebook/api_pull.py` | Fetches yield data from FRED |
| `notebook/plot_spreads.py` | Creates the spread chart |
| `.env` | Stores your secret API key (not shared) |
| `.gitignore` | Prevents CSVs and PNGs from being uploaded |
| `treasury_yields.csv` | Auto-generated output file |
| `spreads.png` | Auto-generated chart |

---

## Common Issues
- **File not found:** Check you’re inside the `notebook` folder.  
- **API error:** Recheck `.env` file and make sure there’s no space before/after the key.  
- **Permission denied:** Use `python3` instead of `python` on macOS/Linux.  
- **CSV not appearing on GitHub:** That’s expected — it’s ignored locally.




