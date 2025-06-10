
# ScholarOps Classic - Form Automation System

This legacy-compatible system simulates the scholarship nomination document automation process as used between 2016–2018 using Microsoft Excel, Access, and VBA.

## Features
- Auto-generates nomination letters from Excel input
- Uses VBA macro to populate and output letters
- Designed to match original tools (Access, Excel, Outlook)
- Structured for GitHub as a demo/portfolio

## File Structure
- `data/`: Sample scholar nomination data (CSV)
- `templates/`: Template for nomination letter (TXT used instead of DOCX for simplicity)
- `scripts/`: VBA macro for Excel automation
- `docs/`: Output folder for generated letters

## Usage
1. Open the Excel file with data from `data/`
2. Insert the `generate_nomination_letter.vba` macro
3. Run `GenerateNominationLetter` from Developer Tools
4. Check the `docs/` folder for the generated text file

## Requirements
- Microsoft Excel 2016 or later
- Macro-enabled file format (.xlsm)



---

## ✉️ Outlook Email Integration

You can now automatically send the generated nomination letter as an attachment using Outlook.

### Steps:
1. Ensure `Sheet1` has recipient email in cell **G2**
2. Add the macro from `scripts/send_nomination_outlook.vba` to your Excel VBA editor
3. Run `SendNominationViaOutlook`
4. Outlook will open a draft email with the attachment

You can modify `.Display` to `.Send` in the macro to skip the draft step and send directly.


---

## 📄 Generate Nomination Letter as PDF

This version uses a Word DOCX template with placeholder tags and converts the filled content to a PDF file.

### Steps:
1. Place your data in `Sheet1` of your Excel file (from `data/`)
2. Ensure Word is installed on your system
3. Add the macro from `scripts/generate_nomination_pdf.vba` to your Excel file
4. Run `GenerateNominationPDF`
5. The letter will be saved as a PDF inside the `docs/` folder



---

## 🗂️ Log Sent Nomination to Excel

To enable audit tracking and history, the macro in `scripts/log_nomination_sent.vba` will append a new record to a sheet called `Logs`.

### Steps:
1. Open your Excel file and add the macro from `log_nomination_sent.vba`
2. Run the macro after sending/generating the nomination
3. It creates or appends a row to the `Logs` worksheet

### Log Fields:
- Scholar_ID
- Full_Name
- Form_Type
- Sent_Time
- Status

This enables tracking, dashboard reporting, and basic auditing.


---

## 🔄 Logging with Access (Forms_Log Table)

To track all sent forms, create a table using the SQL script in `scripts/create_forms_log.sql`.

### Table: Forms_Log
- `Log_ID` (AutoNumber, Primary Key)
- `Scholar_ID` (Number, linked to Scholars table)
- `Form_Type` (Text)
- `Action_Date` (Date/Time)
- `Status` (Text)

The updated macro in `generate_completion_letter_with_log.vba` will:
- Generate the letter
- Send the email
- Insert a new log record automatically

Use this for auditing and reporting later.



---

# 📘 ScholarOps Classic – Full System Overview

ScholarOps Classic is a legacy-compatible automation and form tracking system designed for scholarship offices using Microsoft Access, Word, Excel, and Outlook (2016–2018).

## 🧱 Architecture Overview
- Microsoft Access (.accdb) as the central database
- Word templates with placeholders for document generation
- VBA macros for PDF export, Outlook dispatch, and Access logging
- Optional Excel-based dashboard for visualization

## 📦 Key Modules
- 📄 Form Generators (Nomination, Completion, Upgrade)
- 📨 Email Automation via Outlook
- 📁 Central `Forms_Log` audit table
- 📊 Excel & Access Reports for analytics

## 📂 Folder Structure
- `/templates/` – DOCX templates with placeholders
- `/scripts/` – VBA macros for Access + SQL setup
- `/docs/` – Output files, dashboards, or logs

## 🛠 Setup Steps
1. Create Access file and import `Scholars`, `Forms_Log` tables
2. Load macros into Access Module
3. Assign macros to Form Buttons
4. Run letters, emails, logs
5. Use `Forms_Log` for reports

## 📄 Reporting
Use the SQL in `scripts/report_queries.sql` to create printable Access reports:
- Monthly form activity
- Scholar history
- Form distribution summary

## 🤖 Automations
Each macro:
- Generates a PDF
- Sends via Outlook
- Logs to Access

---
