# Student Management System

A simple command-line student management program written in Python. Add student records, display all records, and search by roll number. Marks of 40 or more are a **Pass**; lower marks are a **Fail**.

## Requirements

- Python 3

## Run

From this folder, run:

```bash
python3 student_management.py
```

On Windows, run:

```powershell
python student_management.py
```

## Menu

1. **Add Student** — enter a student's name, roll number, and marks out of 100.
2. **Display Students** — show all records, percentage, and pass/fail result.
3. **Search Student** — find a record by roll number.
4. **Exit** — close the program.

## Data storage

Records are held in memory and are cleared when the program exits. The program does not currently save data to a file or database.
