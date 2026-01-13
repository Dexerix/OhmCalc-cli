# OhmCalc-cli

## Description
OhmCalc-cli is a Python script that performs various electrical calculations based on Ohm's law and other electrical formulas. It provides an interactive menu interface to choose the type of calculation needed.

## Features
- Voltage calculation
- Resistance calculation (Ohm's law)
- Current calculation
- Resistivity calculation
- Cable section calculation
- Resistance calculation using resistivity
- Total resistance calculation for parallel resistors
- Total resistance calculation for serial resistors

## Usage
1. Run the `OhmCalc-cli.py` script
2. Choose your calculation from the menu by entering the corresponding letter:
   - U: Voltage
   - R: Resistance
   - I: Current
   - P: Resistivity
   - A: Section
   - O: Resistance (using ρ)
   - PR: Parallel Resistance
   - SR: Serial Resistance
   - Q: Quit

## Input Format
- For large numbers, you can use scientific notation: `2.5*10^3` instead of `2500`
- Units are automatically handled by the program
- All decimal numbers should use a point (.) as separator

## Example
To calculate voltage:
```
Enter R: 100
Enter I: 2.5
250.00 V
```

## Requirements
- Python 3.x
- math module (included in Python standard library)

## Executable Version
A standalone executable (.exe) version is available for Windows users who don't have Python installed. You can find it in the releases section. Simply download and run OhmCalc-cli.exe to use the program without any additional requirements.

## Notes
- All calculations provide results with 2 decimal precision
- The program uses a clear screen feature for better readability
- Press Enter after each calculation to return to the main menu

