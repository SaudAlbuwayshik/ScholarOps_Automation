# Scholarship Specialization Planner (ML-Based)

This project simulates a real-world machine learning system designed to support data-driven scholarship planning decisions. It uses a decision tree classifier trained on a composite dataset reflecting real academic and market foresight data.

## 🎯 Objective
To assist faculty-level decision-makers in identifying future-proof specializations for scholarship nominations based on:
- Global university trends
- Local institutional priorities
- Labor market demand
- Academic research directions

## 🧩 Data Collection Approach
The original production model was built using a diverse range of sources, including:
- Strategic plans from top-ranked global universities
- Direct communication with local and international academic institutions
- Labor market reports and forecasts (e.g., Vision 2030, OECD)
- High-credibility blogs and industry foresight reports

This recreated dataset reflects the structure and logic of that system while protecting private or institutional data.

## 🛠 Features
- Decision Tree Classifier for specialization recommendation
- Data preprocessing and categorical encoding
- Evaluation metrics and confusion matrix
- Visualized decision tree output
- Clean, modular, and documented code

## 🧪 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute:
   ```bash
   python main.py
   ```
3. Output:
   - Check `outputs/decision_tree.png` for model visualization
   - Console output includes performance report and confusion matrix

## 📁 Project Structure
- `main.py` – ML model and pipeline logic
- `data/` – Simulated training dataset and documentation
- `outputs/` – Visual output (decision tree plot)
- `requirements.txt` – Python dependencies
- `data_dictionary.md` – Description of dataset fields

## ⚠️ Note
This project is a recreated version of a real production-grade system developed and deployed by the author. Due to data privacy constraints, original datasets are not included, but the structure, logic, and business goals are faithfully represented.
