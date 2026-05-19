# Academic Calendar — User Guide

> **Note:** The Academic Calendar application itself is in **Greek**. This document is an English translation of its official usage guide.

---

## Initialization

The application requires no installation. All necessary Python libraries and modules are either pre-installed or custom-built. It consists of **three structural components**, which must all reside in the same directory for the application to work correctly:

1. **`utilities/` folder** — functions required by the program
2. **`data/` folder** — user data storage
3. **`AcademicCalendar.pyw` file** — the main application

> Launch the application by opening the `AcademicCalendar.pyw` file.

---

## Interface Overview

The workspace is divided into three sections: **Left**, **Right**, and **Center**.

---

### Left Panel

Contains buttons for the months of the current semester, as well as an option to switch semesters. Selecting a semester and a month displays the days of that month in the central area, organized by week in calendar format (weeks start on **Monday**).

There is an additional button above the University of Patras emblem labeled:

```
| Functionality |
|  (click me)   |
```

Clicking it displays instructions for the flair system and the *Organize Note* feature (described below under the Right Panel).

---

### Right Panel

This is where notes are written and read. In addition to the note text box, the following options are available:

1. **Organize Note** — Lines that begin with a time indicator (`HH:MM`) are sorted in chronological order. Lines without a time indicator are moved (in their original order) to the end of the note, after the time-stamped lines.

2. **Save Note** — Saves the note and turns the corresponding date cell **green**.
   If the note relates to an exam or a study session rather than a regular class, a color flair can be applied by typing a keyword anywhere in the note:
   - `##test` → cell turns **red** (exam)
   - `##study` → cell turns **purple** (study session)
   - Both keywords → cell turns **orange**

   To delete a note, clear its content and save — this also removes the color indicator from that date cell.

3. **Alternative date field** — Allows saving a note to a different date, entered in `DD/MM/YYYY` format.

4. **Recurrence dropdown menu** — Sets how often the note repeats *(see Saving Data section below)*.

---

### Center Panel

Displays the days of the month as individual cells. Clicking a cell opens the corresponding date's note in the Right Panel for reading or editing.

- On launch, the application always defaults to the **current day, month, and year**.
- Selecting a cell automatically fills in the date and loads any existing note.
- To enter data for a **different year**, type the desired year (in `YYYY` format) into the year input field next to the month selector.
  - *Example: type `2025` to enter data for the academic year 2025–2026.*
- **Weekends** are shown in **grey** (typically empty days, also for easier visual identification).
- **Public holidays** are shown in **blue**. Selecting a holiday date allows data to be saved on it, and its color will change accordingly.
  > When saving with a recurrence option, data will **not** be saved on public holidays — those cells remain blue.

---

## Saving Data (Recurrence Options)

| Option | Behavior |
|---|---|
| **Today** | Saves to the selected date only |
| **Weekly** | Saves weekly until January of the following year (e.g. Jan 1, 2023 → Jan 29, 2024) |
| **Every 2 Weeks** | Saves every two weeks until January of the following year — designed for special cases (e.g. first-year ECE labs in Semester 1) |
| **Weekly for Semester** | Saves weekly until the end of the current semester (Aug–Jan or Feb–Jun) |
| **Every 2 Weeks for Semester** | Saves every two weeks until the end of the current semester |

> Saving always starts from the **selected date** — data is never saved to dates in the past.
