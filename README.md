<div align="center">

# 🩺 Doctor AI
### Intelligent Medical Diagnostic Assistant

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![AI](https://img.shields.io/badge/AI-Deep_Learning-FF6F00?style=for-the-badge)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

<br />

<p align="center">
  <b>🏆 Finalist at Jordan Students Pitch Competition 2025 (QRCE) 🏆</b>
  <br />
  <i>Bridging the gap between algorithmic precision and medical expertise.</i>
</p>

</div>

---

## 📖 Overview

**Doctor AI** is an advanced web-based diagnostic tool designed to assist healthcare professionals by providing accurate, AI-driven disease detection. Unlike black-box models, Doctor AI focuses on **Explainable AI (XAI)**, offering insights into *why* a diagnosis was made, ensuring doctors remain in the driver's seat.

The system integrates robust Deep Learning models with a scalable **Flask Backend**, achieving **>95% accuracy** across 8 critical disease pathways.

---

## ⚙️ System Architecture

The project follows a **Microservices-oriented architecture** where the AI models are decoupled from the core logic via RESTful APIs.

* **Backend:** Python (Flask) serving as the API Gateway and Model Wrapper.
* **AI Engine:** Deep Learning models trained on medical imaging datasets.
* **Frontend:** Responsive Web Interface (HTML, Tailwind CSS, JS) communicating via AJAX.
* **Integration:** REST API endpoints for real-time inference.

---

## 🚀 Key Features

* **Multi-Disease Diagnosis:** Capable of detecting 8 different disease pathways (e.g., Pneumonia, Brain Tumors, Skin Cancer) from medical images.
* **High Precision:** Trained on verified datasets achieving 94.5% - 98% accuracy.
* **Fast Inference:** Optimized API response time for real-time usage.
* **Secure Data Handling:** Stateless API design ensures patient data privacy during processing.
* **User-Friendly Dashboard:** A clean interface for doctors to upload scans and view reports.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | **Flask (Python)** | Handles API routing, request validation, and model serving. |
| **AI / ML** | **TensorFlow / PyTorch** | Deep Learning models for image classification. |
| **Frontend** | **HTML5, Tailwind CSS** | Responsive and modern UI design. |
| **Client Logic** | **JavaScript (AJAX)** | Asynchronous API consumption without page reloads. |
| **Data Processing** | **Pandas, NumPy** | Pre-processing medical images before inference. |

---

## 🔌 API Documentation (Sample)

The backend exposes several endpoints for disease prediction. Here is an example of the Prediction Endpoint:

### `POST /api/predict`

Receives an image file and returns the diagnostic result with confidence score.

**Request:**
```json
Content-Type: multipart/form-data
Body: { "image": "scan_file.jpg", "model_type": "brain_tumor" }
Response:
{
  "status": "success",
  "prediction": "Positive",
  "confidence": 98.4,
  "explanation": "High density region detected in upper quadrant..."
}

📸 Screenshots
(Add screenshots of your dashboard here)

<div align="center"> <img src="https://www.google.com/search?q=https://via.placeholder.com/800x400%3Ftext%3DDoctor%2BAI%2BDashboard%2BPreview" alt="Dashboard" width="800"/> </div>

👨‍💻 My Contribution
As the Backend Architect & Lead Developer, my role focused on:

API Development: Building robust Flask APIs to wrap AI models and serve predictions to the frontend.

System Integration: Connecting the Deep Learning engine with the user interface using AJAX.

Optimization: Ensuring fast inference times and handling concurrent requests efficiently.

UI Implementation: Developing the responsive web dashboard using Tailwind CSS.

📬 Contact
Abdalrhman Hamed - Software Engineer <br />
