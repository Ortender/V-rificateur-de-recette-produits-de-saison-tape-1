# 🥦 Recipe Season Feasibility Checker

> Discover the best months to cook your favorite recipes using seasonal ingredients — powered by [Greenpeace’s fruits and vegetables calendar](https://www.greenpeace.fr/guetteur/calendrier/).

---

## 💡 Overview

This project helps users understand when their recipes are most **seasonally feasible**.  
By analyzing the ingredients of a recipe, it matches them with **seasonal availability data** to suggest the **best months to cook it sustainably**.

The idea comes from my interest in **cooking, sustainability, and technology** — and my curiosity to see how data can help people make everyday choices that are better for the planet.

---

## 🎯 Personal Goals

I had already done a similar project in **Excel with VBA** and wanted to recreate it in **Python** to sharpen my skills (I’m fully aware that a single ChatGPT prompt could do this faster — but where’s the fun in that?).  

Here’s what I worked on in this project:
- Extracting data from a webpage using **Python** and **HTML tags**
- Practicing **basic Python programming**, table manipulations, conditions, and loops
- Anticipating **user experience** challenges and finding ways to improve navigation despite a simple console interface  
  *(For example, ingredient inputs are not case-insensitive, but I don’t yet handle typos or spaces. The user must type the ingredient exactly as listed in the calendar — something I plan to improve in a future web app version.)*

---

## ⚙️ Features

- 🥕 Input ingredients of a recipe and get their **months of feasibility**
- 💻 View the list of ingredients included in the calendar
- 📅 Extract Greenpeace’s **fruits & vegetables seasonal calendar** into a CSV file, organized either by month or by ingredient  

---

## 🧠 Tech Stack

- **Language:** Python  
- **Libraries:** BeautifulSoup, Requests  

---

## 🖼️ Demo

### 🧭 User Menu
<img width="1101" height="246" alt="User menu screenshot" src="https://github.com/user-attachments/assets/e806a972-57e1-43bb-8c75-447240469d25" />

### ✏️ User Inputs Ingredients
<img width="1474" height="338" alt="User input screenshot" src="https://github.com/user-attachments/assets/39dbc77a-ccfb-4497-9591-0361245715b3" />

### ⚠️ Invalid Ingredient — Consulting the Accepted List
<img width="1471" height="462" alt="Invalid input screenshot" src="https://github.com/user-attachments/assets/3cc28540-3f31-406f-9a1f-46804b87ddfe" />

### 🔁 User Corrects Input
<img width="790" height="266" alt="Correction screenshot" src="https://github.com/user-attachments/assets/0731dd63-a0d4-44fe-81bd-b2813ed7da5e" />

### ✅ Final Output — List of Feasible Months
<img width="458" height="50" alt="Output screenshot" src="https://github.com/user-attachments/assets/54cadbab-86da-425c-8970-dd08af422d26" />

---

## 🚀 Getting Started

### 🧩 Prerequisites
- **Python 3.14**
- Python packages:
  ```bash
  pip install bs4
  pip install requests

## 🪄 Run the Project

### Clone the repository

git clone https://github.com/Ortender/recipe-season-feasibility.git


### Navigate to the project folder

cd path/to/recipe-season-feasibility


### Launch the main script

python main.py
