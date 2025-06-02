# 🕵️‍♂️ s3cret_deobfuscator

**s3cret_deobfuscator** is a Python-based utility designed to assist malware analysts, cybersecurity researchers, and reverse engineers in deobfuscating malicious Python scripts. Specifically, it identifies and replaces dangerous `exec()` calls with `print()` statements, then executes the sanitized script to reveal its runtime behavior in a safe, observable way.

> ⚠️ This tool is intended strictly for educational and research purposes related to **malware analysis and cybersecurity defense**.

---

## 🚨 Legal Disclaimer

This project is provided for **educational and lawful use only**.

- You are **solely responsible** for how you use this tool.
- **Do not use it to analyze or run malware unless you're in a controlled, isolated environment** (e.g., sandbox or virtual machine).
- The author does **not condone** the use of this tool for malicious purposes and **will not be held liable** for any misuse.

---

## 🔍 Features

- Scans a Python script for `exec(...)` calls.
- Replaces each `exec()` call with `print()` to expose hidden behavior.
- Executes the modified script and captures its output.
- Saves the captured output to a `.txt` file for inspection.

---

## 🧪 Use Case

This tool was created to help cybersecurity professionals understand and safely unpack obfuscated or suspicious Python code by exposing its runtime behavior — **without executing unknown code directly**.

---

## ▶️ Usage

### 🔧 Command

```bash
python s3cret-deobfuscator.py <target_script.py>
