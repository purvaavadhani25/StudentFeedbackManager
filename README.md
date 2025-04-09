# 📋 VersionForge – Student Feedback Manager

A lightweight CLI-based Student Feedback Manager built for EduTrack as part of the VersionForge Hackathon at PES University.

## 📌 Objective

To build a version-controlled system that:
- Collects student feedback
- Calculates and summarizes scores
- Allows searching and reporting
- Supports modular development and documentation practices

---

## 🗂️ Project Structure

```bash
feedback/
├── feedback_entry.py         # Collects feedback from users
├── score_calculator.py       # Computes average score
├── feedback_summary.py       # Summarizes feedback by grade
├── report_generator.py       # Exports feedback to .txt file
├── search_feedback.py        # Searches feedback by name
└── count_feedback.py         # Counts total feedback entries
