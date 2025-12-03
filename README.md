# 🚗 Vehicle Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/Interface-Tkinter-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

A GUI-based desktop application developed in Python to manage vehicle parking, track slot availability, and maintain entry/exit history. This project demonstrates the use of **Tkinter** for frontend design and logical data structures for backend management.

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Future Improvements](#-future-improvements)

---

## 🧐 About the Project

This **Vehicle Management System** is a project designed to automate the parking process. It replaces manual paper-based logs with a digital interface. The system creates a visual grid of 40 parking slots (8 rows x 5 columns), allowing the administrator to easily identify empty and occupied spots.

---

## ✨ Features

* **Dynamic Dashboard (Home):**
    * Visual representation of 40 parking slots.
    * **🔴 Red:** Slot Occupied (Shows Vehicle Number).
    * **🟢 Green:** Slot Available.
* **Add Vehicle:**
    * User-friendly form to input Owner Name, Mobile Number, and Vehicle Number.
    * **Validation:** Ensures Mobile Number is 10 digits.
    * **Auto-Allocation:** Automatically finds the next available slot.
* **Manage Vehicles:**
    * Tabular view of all currently parked vehicles.
    * **One-Click Exit:** An "EXIT" button to check out a vehicle, freeing up the slot immediately.
* **History Tracking:**
    * Maintains a log of all vehicles that have left the premises.
    * Records specific **Entry Time** and **Exit Time**.
* **Navigation:**
    * Sidebar navigation to switch between modules seamlessly.

---

## 📸 Screenshots

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3 |
| **GUI Framework** | Tkinter (Standard Python Library) |
| **Time Management** | Datetime Module |
| **Data Structure** | Lists & Dictionaries (for in-memory storage) |

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites
Make sure you have Python installed. You can check by running:
```bash
python --version
