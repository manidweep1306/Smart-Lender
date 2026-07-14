# Smart Lender 🏦
**AI-Powered Loan Approval Prediction System**

Smart Lender is a machine learning-powered web application designed to predict the creditworthiness of loan applicants. By leveraging classification algorithms, this platform enables banks and financial institutions to make faster, data-driven, and unbiased loan approval decisions. 

---

## 🚀 Overview

Manual loan verification is often time-consuming and prone to inconsistency. Smart Lender automates this process by evaluating structured applicant inputs—such as gender, marital status, education, employment status, income, loan amount, credit history, and property area—to determine the likelihood of loan repayment or default. 

After training and evaluating multiple models, **XGBoost** emerged as the best-performing algorithm (94.7% training accuracy and 81.1% testing accuracy) and is integrated into this Flask-based web application for real-time predictions.

### Key Use Cases
* **Fast-Track Approval:** Automatically approve low-risk applicants with stable income and good credit history without manual review.
* **High-Risk Detection:** Flag applicants with irregular income or poor credit for further scrutiny and document verification.
* **Batch Evaluation:** Rapidly process multiple applications during high-volume periods, reducing evaluation time while maintaining compliance.

---

## 🛠️ Technology Stack

* **Core Programming:** Python 3.8+
* **Web Framework:** Flask
* **Machine Learning:** Scikit-learn, XGBoost, SciPy
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Frontend:** HTML, CSS

---

## 🏗️ System Architecture & Workflow

The system follows a three-tier modular architecture—separating the user interface, backend API, and ML modules—developed across five core epics:

1. **Data Collection & Architecture:** Leveraging open-source datasets and defining a scalable folder structure.
2. **Data Analysis:** Utilizing Univariate, Bivariate, and Multivariate analysis (via `seaborn` and `matplotlib`) to uncover feature patterns.
3. **Data Pre-processing:** Handling missing values, encoding categorical variables, scaling features, and addressing class imbalances using **SMOTE** (Synthetic Minority Over-sampling Technique).
4. **Model Building:** Training Decision Tree, Random Forest, K-Nearest Neighbors (KNN), and XGBoost models. Evaluated using confusion matrices and cross-validation.
5. **Application Building:** Deployment via a Flask routing structure connecting `home.html`, `predict.html`, and `submit.html` interfaces to the `predict()` backend function.

---

## 💻 System Requirements

**Hardware:**
* **Processor:** Intel i3 or above
* **RAM:** 4 GB (8 GB recommended)
* **Storage:** 10 GB free space
* **System Type:** 64-bit OS

**Software:**
* **OS:** Windows 10/11 / Linux / macOS
* **Environment:** Anaconda Navigator / standard Python environment
* **IDE:** PyCharm / VS Code

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/manidweep1306/Smart-Lender.git](https://github.com/manidweep1306/Smart-Lender.git)
   cd Smart-Lender

---

## ⚙️ Installation & Usage

1. **Install dependencies:**
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt

2. **Run the application:**
    python app.py


