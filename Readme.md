# 🏦 Smart-Lender: AI-Powered Loan Approval Prediction

**Smart-Lender** is a premium, automated credit underwriting and loan eligibility assessment system. Leveraging a machine learning classifier wrapped in a responsive Flask web application, it automates standard mortgage credit profiling—assessing demographic and financial risk variables in under 2 seconds.

---

## 🚀 Key Features

*   **Premium Web Interface**: An interactive, responsive client dashboard for inputting applicant parameters.
*   **Predictive Inference Engine**: Implements a serialized, fine-tuned **XGBoost Classifier** achieving **85.6% Accuracy**.
*   **Imbalance Handling (SMOTE)**: Integrated Synthetic Minority Over-sampling Technique to balance historical risk biases.
*   **Real-time Output Visualization**: Clean HTML visual feedback indicating loan approval with dedicated outcomes.
*   **Structured Lifecycle Documentation**: Includes a complete set of 22 professional-grade design, requirement, and testing documents mapped across 8 phases.

---

## 🛠️ Technology Stack

| Layer | Component | Justification |
| :--- | :--- | :--- |
| **Logic & Backend** | Python 3.10+, Flask | Lightweight, performant WSGI micro-framework for running serialized ML models. |
| **Machine Learning** | XGBoost, Scikit-Learn | Extreme Gradient Boosting classifier for high-accuracy tabular datasets. |
| **Preprocessing & Scaling** | Pandas, NumPy, StandardScaler | Pipeline normalization and label dictionary translations. |
| **Model Serialization** | Joblib | Low-overhead loading of model binary structures on application startup. |
| **Documentation Pipeline** | ReportLab | Programmatic generation of standardized company-grade PDF documents. |

---

## 📂 Repository Layout

The project adheres to the standardized **AI/ML & Gen-AI Track Project Template** layout, organizing comprehensive documentation across 8 distinct phases:

```text
📁 Smart-Lender
│
├── 📁 1. Brainstorming & Ideation
│   ├── 📄 Brainstorming & Idea Prioritization.pdf
│   ├── 📄 Define Problem Statements .pdf
│   └── 📄 Empathy Map.pdf
│
├── 📁 2. Requirement Analysis
│   ├── 📄 Customer Journey Map.pdf
│   ├── 📄 Data Flow Diagram.pdf
│   ├── 📄 Solution Requirements.pdf
│   └── 📄 Technology Stack.pdf
│
├── 📁 3. Project Design Phase
│   ├── 📄 Problem-Solution Fit.pdf
│   ├── 📄 Proposed Solution.pdf
│   └── 📄 Solution Architecture.pdf
│
├── 📁 4. Project Planning Phase
│   └── 📄 Project Planning.pdf
│
├── 📁 5. Project Development Phase
│   ├── 📄 Code-Layout, Readability and Reusability.pdf
│   ├── 📄 Coding & Solution.pdf
│   └── 📄 No. of Functional Features Included in the Solution.pdf
│
├── 📁 6.Project Testing
│   └── 📄 Performance Testing.pdf
│
├── 📁 7.Project Documentation
│   ├── 📄 Project Executable Files.pdf
│   └── 📄 Sample Project Documentation.pdf
│
└── 📁 8.Project Demonstration
    ├── 📄 Communication.pdf
    ├── 📄 Demonstration of Proposed Features.pdf
    ├── 📄 Project Demo Planning.pdf
    ├── 📄 Scalability & Future Plan.pdf
    └── 📄 Team Involvement in Demonstration.pdf
```

---

## ⚙️ Setup & Local Execution

### 1. Clone the Repository
```bash
git clone https://github.com/dharani756/Smart-Lender.git
cd Smart-Lender
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000` to interact with the interface.

---

## 👥 Submitted By

*   **Team Leader**: Palli Dharani
*   **Team Members**:
    *   Yarabarla Manidweep
    *   Saikiran Kudipudi
    *   Sita Rama Raju Datla
    *   Thota Leela Sai Krishna
