# ✈️ Python Air Traffic Data Analyzer

This project is a command-line utility built in **Python 3** designed to process and analyze European air traffic departure data stored in structured CSV files. It validates user input, performs complex statistical calculations, saves reports, and visualizes the results.

The utility is capable of running multiple analyses sequentially without restarting, making it an efficient tool for batch data processing.

## ✨ Core Features

* **File Selection & Validation:** Prompts the user to input a 3-character airport code (e.g., LHR, CDG) and a year (2000-2025). The program validates both inputs for correct format, length, and range before loading the corresponding CSV file.
* **Statistical Reporting:** Calculates and displays 10 specific outcomes, including:
    * Total flights and flights departing from specific terminals.
    * Flights under a certain distance or departing below a temperature threshold.
    * Airline-specific metrics (e.g., average departures per hour, percentage of total traffic, delay rates).
    * Identification of the least common destination airport.
* **Report Generation:** Appends all calculated results to a running text file named `results.txt`, ensuring previous analyses are not overwritten.
* **Data Visualization:** Prompts the user for a 2-character airline code and plots a customizable **horizontal histogram** showing the selected airline’s departures broken down by the hour of the 12-hour survey period.
* **Program Looping:** After each full analysis (report and visualization), the user is asked if they wish to process a new CSV file, allowing for continuous analysis.

## 🛠️ Technology Used & Dependencies

* **Language:** Python 3
* **I/O:** Command-line input for file selection, file reading (CSV), and file writing (TXT report).
* **Graphics:** Relies on the **`graphics.py`** module (a simple, single-file Python graphics library) for rendering the histogram visualization.

## 🚀 How to Run

### Prerequisites

1.  **Python 3** installed on your system.
2.  The **`graphics.py`** module must be present in the same directory as your main script.
3.  The **CSV data files** (named in the format `[AirportCode][Year].csv`, e.g., `CDG2024.csv`) must be in the same directory.

### Execution Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/szthaarnav/Air-Traffic-Data-Analyzer.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd "Simple Data Processing with Histogram"
    ```
3.  **Run the main script:**
    ```bash
    python main.py
    ```
    *The program will then guide you through selecting the airport, year, and airline for analysis.*
