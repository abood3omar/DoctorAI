<div align="center">

# 🩺 Doctor AI
### Intelligent Medical Diagnostic Assistant
### نظام التشخيص الطبي الذكي

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

<br />

<p align="center">
  <b>🏆 Finalist at Jordan Students Pitch Competition 2025 (JSPC) 🏆</b>
  <br />
  <i>Queen Rania Center for Entrepreneurship (QRCE)</i>
  <br />
  <br />
  <i>"Bridging the gap between algorithmic precision and medical expertise using Explainable AI."</i>
</p>

</div>

---

## 📖 Overview | نبذة عن المشروع

**Doctor AI** is a comprehensive medical diagnostic platform designed to support doctors, not replace them. We pitched this project at the **JSPC 2025**, highlighting our focus on **Explainable AI (XAI)**.

The system analyzes medical imaging using Deep Learning models to detect diseases with **>95% accuracy** across 8 critical pathways, providing interpretable results to help physicians make informed decisions.

---

## 🧠 AI Models & Disease Pathways | النماذج والأمراض
The system integrates **8 specialized Deep Learning models**, each trained for a specific diagnostic pathway:

| Disease / Condition | Model Architecture | Accuracy |
| :--- | :--- | :--- |
| **Brain Tumor Detection** | CNN / ResNet | **98.4%** |
| **Pneumonia (X-Ray)** | VGG16 | **96.2%** |
| **Skin Cancer (Melanoma)** | EfficientNet | **95.8%** |
| **Diabetes Retinopathy** | CNN Custom | **97.1%** |
| **Alzheimer's MRI** | DenseNet | **94.5%** |
| **Breast Cancer** | ResNet50 | **96.0%** |
| **Heart Disease** | ANN | **95.5%** |
| **Kidney Stone** | CNN | **95.0%** |

*(Note: The models are wrapped via a Flask API to ensure fast inference and modularity.)*

---

## 📸 Screenshots | صور من النظام

<div align="center">
  <h3>🏠 Home & Dashboard</h3>
  <img src="screenshots/home.png" alt="Home Page" width="800"/>
  
  <br/><br/>

  <h3>📊 Diagnosis & XAI Results</h3>
  <img src="screenshots/result.png" alt="Diagnosis Result" width="800"/>
</div>

---

## ⚙️ Technical Architecture | البنية التقنية

I designed the system using a **Microservices-oriented architecture**:

* **Backend (My Role):** Built with **Python (Flask)**. It acts as the API Gateway that receives images from the frontend, processes them, and routes them to the correct AI model.
* **Frontend:** Developed using **HTML, Tailwind CSS, and JavaScript**. It connects to the Flask API via AJAX for real-time, asynchronous predictions.
* **AI Integration:** Models are loaded into memory efficiently to handle concurrent requests without latency.

---

## 🚀 Key Features

* ✅ **Explainable AI (XAI):** Visualizing the "Why" behind the diagnosis.
* ✅ **High Precision:** Accuracy exceeding 95% on validation datasets.
* ✅ **Real-time Processing:** Optimized Flask APIs for instant feedback.
* ✅ **Secure & Scalable:** Designed to handle sensitive medical data securely.

---

## 👨‍💻 My Contribution

**Abdalrhman Hamed - Backend Architect & Lead Developer**

* **Architected** the entire Flask infrastructure to support multiple AI models.
* **Developed** RESTful APIs to bridge the Deep Learning engine with the web interface.
* **Built** the responsive dashboard using Tailwind CSS.
* **Implemented** the logic for handling medical image uploads and validation.

---

## 📬 Contact

**Abdalrhman Hamed**
<br />
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdalrhman-hamed-5b929725b/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/abood3omar)
