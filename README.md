### **📌 Brent Oil Price Analysis – Task 1**  
**Task: Defining the Data Analysis Workflow & Understanding the Model**  

---

## **📖 Project Overview**  
This project aims to analyze how major political and economic events impact **Brent oil prices**. We will focus on identifying key events, measuring their effects on price fluctuations, and extracting meaningful insights for investors, policymakers, and energy companies.  

Task 1 specifically involves **defining the data analysis workflow** and **understanding the model and data** before deeper statistical modeling is applied.  

---

## **🎯 Objectives of Task 1**  
1️⃣ **Define the Data Analysis Workflow:**  
   - Plan the step-by-step analysis process.  
   - Ensure clarity on data sources, assumptions, and limitations.  
   - Identify statistical techniques to be used.  

2️⃣ **Understand the Model and Data:**  
   - Explore the historical **Brent oil price dataset** (May 20, 1987 – Sept 30, 2022).  
   - Review statistical models suitable for time series analysis (e.g., **ARIMA, GARCH, Bayesian models**).  
   - Identify how event-driven market changes can be detected.  

3️⃣ **Prepare for Further Analysis:**  
   - Identify key economic and political events.  
   - Understand how to communicate findings to stakeholders.  
   - Document insights for the **interim report**.  

---

## **📂 Folder Structure**  
The repository is structured as follows:  

```
brent_oil_task1/
│── data/                # Stores the dataset  
│   ├── raw/             # Original dataset (Brent oil prices)  
│   ├── processed/       # Cleaned/Formatted data  
│── notebooks/           # Jupyter notebooks for exploration  
│   ├── 01_data_exploration.ipynb  # Initial EDA & visualization  
│── src/                 # Scripts for data processing and modeling  
│   ├── data_loader.py   # Load and preprocess data  
│   ├── eda.py           # Functions for EDA & visualization  
│── reports/             # Interim report on workflow and model understanding  
│── README.md            # Task description and instructions  
│── requirements.txt     # Dependencies (pandas, matplotlib, ruptures, etc.)  
│── .gitignore           # Ignore unnecessary files  
```

---

## **📊 Dataset Overview**  
- **Source**: Historical Brent oil price dataset  
- **Time Span**: **May 20, 1987 – September 30, 2022**  
- **Columns**:  
  - `Date`: The recorded date (Format: `day-month-year`)  
  - `Price`: Brent oil price in **USD per barrel**  

---

## **🛠 Tools & Technologies**  
- **Programming Language**: Python 🐍  
- **Libraries**:  
  - `pandas` – Data handling  
  - `matplotlib` – Visualization  
  - `ruptures` – Change point detection  
  - `PyMC3` – Bayesian modeling  
  - `statsmodels` – Time series analysis  

---

## **🚀 Next Steps**  
✔ Load and explore the dataset in **Jupyter Notebook**.  
✔ Review key time series models (**ARIMA, GARCH, Bayesian models**).  
✔ Identify assumptions, limitations, and expected outputs.  
✔ Prepare the **Interim Report** covering workflow and model understanding.  

---

## **📢 Contribution Guidelines**  
1️⃣ Clone the repo:  
   ```bash
   git clone https://github.com/your-username/brent_oil_task1.git
   cd brent_oil_task1
   ```  
2️⃣ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3️⃣ Work on **notebooks/src/reports** as per task requirements.  
4️⃣ Commit and push updates:  
   ```bash
   git add .
   git commit -m "Added EDA and workflow documentation"
   git push origin main
   ```  


