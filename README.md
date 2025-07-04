# 🧠 PCOS Detection & AI-Based Recommendation System  
**An End-to-End AI Solution for Women’s Health**

![PCOS Detection](https://img.shields.io/badge/AI-PCOS%20Detection-blue.svg) ![Gradio UI](https://img.shields.io/badge/UI-Gradio-yellowgreen) ![Tech](https://img.shields.io/badge/Built%20With-Python%20%7C%20ML%20%7C%20CNN%20%7C%20Gradio%20%7C%20EDA-blue)

## 📌 Overview

**Polycystic Ovary Syndrome (PCOS)** is a hormonal disorder that affects 1 in 10 women of reproductive age. Early diagnosis is critical—but often missed.

This project is a **complete AI-powered PCOS detection assistant**, built using:
- 🧪 Logistic Regression on patient health records
- 🧠 CNN-based classification on ultrasound images
- 💬 AI-driven medical & lifestyle suggestions via prompt-based GenAI
- 🎛️ Gradio-based UI for interactive healthcare diagnostics

> 🚀 Built to combine **machine learning**, **deep learning**, and **generative AI** with a **user-friendly interface** for impactful, real-world healthcare solutions.

---

## 🔬 Core Features

- ✅ **Exploratory Data Analysis (EDA)**: Understanding patient patterns and risk factors
- 🧪 **Logistic Regression Classifier**: For structured health & lab data
- 🖼️ **CNN Classifier**: Trained on ultrasound images to assess PCOS visually
- 💬 **AI Recommendation Engine**: GenAI-powered diet, lifestyle & treatment advice
- 🧑‍⚕️ **Gradio Interface**: Clean and intuitive UI for patient inputs & predictions
- 🗂️ **Notebook-based Execution**: Jupyter Notebooks for reproducibility and exploration

---

## 🧰 Tech Stack

| Layer              | Tools & Frameworks                                      |
|-------------------|----------------------------------------------------------|
| 📊 EDA & ML        | Pandas, Seaborn, Scikit-learn (Logistic Regression)     |
| 🧠 CNN Model       | TensorFlow / Keras                                       |
| 🧪 Image Data       | Ultrasound scans (preprocessed)                         |
| 🎛️ Interface       | Gradio (for interactive demos)                          |
| 📓 Development     | Jupyter Notebook                                         |
| 💬 AI Recommendations | Prompt Engineering with OpenAI (optional extension) |

---

## 🧠 Project Architecture
──────────────┐
│ Patient │
│ Inputs via │
│ Gradio UI │
└──────┬───────┘
│
▼
📊 Logistic Regression ← Structured Features (e.g., BMI, FSH, LH)
🖼️ CNN Image Classifier ← Ultrasound Images
│
▼
💬 GenAI Suggestions (Diet / Lifestyle / Risk Assessment)
│
▼
📈 Output Results on Gradio Interface (Probability + Advice)


## 📂 Key Files & Structure

📁 pcos-ai-detection/
├── 📄 PCOS_EDA_Logistic_Regression.ipynb # EDA + Logistic Model
├── 📄 PCOS_CNN_ImageClassifier.ipynb # CNN on ultrasound scans
├── 📄 gradio_app.py # Gradio interface logic
├── 📁 models/ # Saved model weights
├── 📁 images/ # Sample ultrasound images
├── 📁 data/ # Dataset files
├── 📄 requirements.txt # Dependencies



## 🚀 How to Run

### 🔧 Setup

```bash
git clone https://github.com/yourusername/pcos-ai-detection.git
cd pcos-ai-detection
pip install -r requirements.txt
▶️ Launch Gradio App
bash
Copy code
python gradio_app.py
Then open the local Gradio link in your browser to interact with the model.

🎯 Results
Component	Metric	Value
Logistic Regression	Accuracy	~91%
CNN Model (Ultrasound)	Validation Accuracy	~88%
End-to-End Latency	UI to Output	~1s
GenAI Suggestions	Semantic Match Score	~95% (manual eval)

👨‍💼 Why This Project?
✅ Combines ML + Deep Learning + GenAI
✅ Real-world healthcare use case with social impact
✅ Full-stack AI with frontend demo (Gradio)
✅ Modular and extensible for production healthcare apps

"As an aspiring AI engineer, this project reflects my ability to architect, train, and deploy complete ML systems. It’s aimed to solve real-world challenges and aligns with product-oriented thinking expected at Microsoft, Flipkart, and similar companies."

🧑‍💻 Author
Prateeksha Khichi
AI | ML | Deep Learning | GenAI | HealthTech Innovator


🙌 Acknowledgements

Kaggle PCOS Dataset – patient data

Gradio – for rapid prototyping & deployment

TensorFlow – for CNN model training



