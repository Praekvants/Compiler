# Compiler
Compile the gnarliest of Excel Files

Verify Python 3 is installed
Open Terminal and run
python3 --version
You should see something like “Python 3.x.x”.

Install pip (if needed)
python3 -m ensurepip --upgrade

Install the required packages
python3 -m pip install pandas tkinterdnd2

Save the compiler script
• Create a new folder, e.g. ~/Projects/CSVCompiler/
• Inside that folder create a file named compiler.py
• Paste in your Python code

Run your code

Merge CSV files
• Drag-and-drop any number of .csv files onto the window
• Or click “Browse…” and select multiple files at once
What happens:
– Reads every dropped file end-to-end
– Keeps the header row only once
– Creates a folder on your Desktop named “Merged_<first-file-name>/”
– Writes the combined data into Merged_<first-file-name>.csv inside that folder

Repeat or Exit
• Drag more files anytime to merge another batch
• Close the window to quit

Intended output example
If you drop Q1.csv, Q2.csv, Q3.csv you’ll get on your Desktop:
Merged_Q1/
└─ Merged_Q1.csv (header plus all rows from Q1,Q2,Q3)
