# Lab 5: Static Code Analysis
## Society Dues Program

**Student Name:** Prashant Naik  
**Lab:** Software Engineering Lab — Lab 5  
**Repository:** L5_17_society_dues  
**Source File:** society_dues.py

---

## 1. Objective

The objective of this lab is to improve the quality, security, and style of the assigned Python program using three static analysis tools: Pylint, Bandit, and Flake8.

These tools analyze source code to identify programming issues, potential security vulnerabilities, and style violations without executing the code.

## 2. Program Overview

The society_dues.py program demonstrates a simple society maintenance-dues management system using SQLite.

The program provides the following functions:

- Add maintenance dues for flats.
- Record the month and amount of dues.
- Mark a due as paid.
- Calculate a late fee.
- Display flats with pending payments.

The program uses an in-memory SQLite database. Therefore, the data is temporary and is lost when the program exits.

## 3. Tools Used

### 3.1 Pylint

Pylint checks code quality, naming conventions, missing documentation, return statements, and potentially problematic programming practices.

### 3.2 Bandit

Bandit identifies common security problems in Python code, such as hardcoded passwords, potentially unsafe SQL construction, and dangerous function usage.

### 3.3 Flake8

Flake8 checks Python formatting and style, including line length, indentation, blank lines, and trailing whitespace.

---

## 4. Issues Identified and Fixes Applied

The following issues were identified from the original analysis reports and addressed during the code-cleaning process.

| No. | Tool | Issue Identified | Fix Applied |
|---|---|---|---|
| 1 | Pylint | Missing module docstring | Added a module docstring. |
| 2 | Pylint | Missing function docstrings | Added documentation to functions. |
| 3 | Pylint | Function name addDue did not follow snake_case | Renamed addDue to add_due and updated function calls. |
| 4 | Pylint | Mutable default argument history=[] | Changed the default argument to None and initialized a list inside the function. |
| 5 | Pylint | Inconsistent return statements in collect() | Added an explicit return None when no matching due exists. |
| 6 | Pylint | Comparison with None | Replaced comparison with an appropriate None check and simplified pending(). |
| 7 | Pylint/Bandit | Use of eval() and broad exception handling | Replaced string evaluation with numeric arguments to the penalty() function. |
| 8 | Bandit | Hardcoded password string | Removed the unused hardcoded password constant. |
| 9 | Bandit | SQL query constructed using an f-string | Replaced the query with a parameterized SQL statement using placeholders. |
| 10 | Flake8 | Lines exceeding the permitted length | Split long statements across multiple lines. |
| 11 | Flake8 | Incorrect blank-line spacing | Corrected blank lines between top-level functions. |
| 12 | Flake8 | Whitespace on blank lines | Removed trailing whitespace. |
| 13 | Flake8 | Incorrect multiline indentation | Corrected continuation-line indentation. |

### 4.1 Security Improvements

**Parameterized SQL queries:** Parameterized queries separate SQL instructions from supplied values and reduce the risk of SQL injection.

**Removal of eval():** The program now calculates the fee using numeric arguments rather than executing a string as Python code.

**Removal of the hardcoded password:** The unused password constant was removed from the source code.

**Mutable default argument correction:** Using None instead of a shared default list prevents unintended sharing of data between function calls.

---

## 5. Before-and-After Analysis Results

### 5.1 Before Analysis

The following results were recorded in the original reports.

| Tool | Before Result |
|---|---|
| Pylint | Score: 5.81/10 |
| Bandit | 3 findings: 1 low-severity and 2 medium-severity |
| Flake8 | 5 initial violations |

The original Bandit findings included:

1. B105 — Possible hardcoded password string.
2. B608 — Possible SQL injection through string-based query construction.
3. B307 — Use of the potentially insecure eval() function.

The original Flake8 report included line-length, blank-line, and None-comparison style issues.

### 5.2 After Analysis

The final results must be recorded after running the tools against the final saved source file.

| Tool | Final Result |
|---|---|
| Pylint | Enter the actual final score out of 10. |
| Bandit | Enter the actual remaining findings and severity counts. |
| Flake8 | Record whether any violations remain. |

The lab target is a Pylint score above 9.5/10, addressing Bandit findings, and correcting Flake8 formatting issues.

Do not claim that these targets have been achieved until the final reports confirm the results.

### 5.3 Report Files

The following reports are maintained for comparison:

- pylint_report_before.txt
- pylint_report_after.txt
- bandit_report_before.txt
- bandit_report_after.txt
- flake8_report_before.txt
- flake8_report_after.txt

---

## 6. Testing and Verification

The program and analysis tools should be tested from the project directory.

### 6.1 Run the Python Program

Command:

    python .\society_dues.py

Expected output for the supplied demonstration:

    2500
    100
    ['A-102']

This output assumes that the program adds dues for A-101 and A-102, marks A-101 as paid, calculates a fee using 50 and 2, and lists the remaining unpaid flat.

### 6.2 Run Pylint

Command:

    python -m pylint .\society_dues.py

Record the final score shown by Pylint.

### 6.3 Run Bandit

Command:

    python -m bandit .\society_dues.py

Review the final findings and severity counts.

### 6.4 Run Flake8

Command:

    python -m flake8 .\society_dues.py

If the command produces no output, Flake8 has not reported any violations for this file.

### 6.5 Verification Results

Program execution: Record the actual result.

Pylint final score: Record the actual score.

Bandit final findings: Record the actual findings and severity counts.

Flake8 final result: Record the actual result.

---

## 7. Git Commit Evidence

The lab requires three separate commits for changes associated with the three analysis tools.

Check the repository history using:

    git log -3 --oneline

Record the actual commit hashes below.

| Stage | Commit Message | Commit Hash |
|---|---|---|
| Pylint | Fix Pylint code quality issues | Enter actual hash |
| Bandit | Fix Bandit security findings | Enter actual hash |
| Flake8 | Fix Flake8 style violations | Enter actual hash |

The commits should contain real changes corresponding to each stage. Empty commits should not be created merely to reach three commits.

---

## 8. Reflection Questions and Answers

### 8.1 What is static code analysis?

Static code analysis examines source code without running the program. It helps identify potential programming errors, security risks, and style violations early in development.

### 8.2 What did Pylint help identify?

Pylint identified issues such as missing documentation, naming conventions, mutable default arguments, inconsistent return statements, comparisons with None, and unsafe programming practices.

### 8.3 Why is a mutable default argument a problem?

A mutable default list can be shared across multiple function calls. This can cause data from one call to affect another. Using None and creating a new list inside the function avoids this problem.

### 8.4 Why are parameterized SQL queries safer?

Parameterized queries keep SQL instructions separate from supplied values. This reduces the risk of user-supplied data being interpreted as SQL commands and helps prevent SQL injection.

### 8.5 Why should eval() be avoided?

The eval() function can execute Python expressions contained in a string. If the input is untrusted, this can lead to unsafe code execution. Performing calculations directly with numeric arguments is safer.

### 8.6 How did Flake8 improve the program?

Flake8 identified issues involving line length, blank-line spacing, trailing whitespace, and indentation. Fixing these issues makes the code easier to read and maintain.

### 8.7 Why should static analysis tools be rerun after making changes?

Rerunning the tools verifies whether the original findings have been resolved and identifies any remaining issues. It provides evidence of the final code quality.

### 8.8 What did you learn from this lab?

This lab demonstrated that code quality, security, and formatting require different types of checks. Pylint, Bandit, and Flake8 complement one another. Using them together helps improve readability, maintainability, and security awareness.

---

## 9. Conclusion

The society-dues program was reviewed using Pylint, Bandit, and Flake8. The changes addressed documentation, naming conventions, mutable default arguments, return behavior, unsafe string evaluation, hardcoded credentials, SQL query construction, and formatting violations.

The program must be tested and all three analysis tools rerun after the final edits. The actual final scores, findings, test results, and Git commit hashes should be recorded before submission.

The completed deliverables include the corrected Python source file, the before-and-after reports from all three tools, this lab report, and evidence of three meaningful Git commits.