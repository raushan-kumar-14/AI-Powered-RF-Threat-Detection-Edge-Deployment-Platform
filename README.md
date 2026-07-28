# 📡 AI-Powered RF Threat Detection & Edge Deployment Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red?style=for-the-badge&logo=pytorch)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![ONNX](https://img.shields.io/badge/ONNX-Deployment-blue?style=for-the-badge)
![TensorRT](https://img.shields.io/badge/TensorRT-NVIDIA-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

### Intelligent RF Spectrum Monitoring • Deep Learning • Signal Intelligence • Edge AI

---

### 🚧 Project Status

**This project is currently under active development.**

The repository is being developed as a complete end-to-end platform for RF spectrum monitoring, AI-powered threat detection, deep learning model training, and edge deployment. New modules, datasets, documentation, and demonstrations will be added progressively.

</div>

---

# 📖 Overview

Modern wireless environments are becoming increasingly crowded due to the rapid growth of Wi-Fi, Bluetooth, LTE, 5G, IoT devices, commercial drones, satellite communication, and military communication systems.

Traditional RF monitoring systems primarily rely on manually engineered algorithms and threshold-based detection, which often struggle to identify unknown, adaptive, or rapidly evolving RF threats.

This project aims to develop a complete AI-powered RF threat detection platform capable of automatically analyzing radio frequency signals, identifying wireless technologies, detecting abnormal spectrum activity, and classifying potential threats using deep learning.

The platform combines modern Signal Processing techniques with Artificial Intelligence to create an intelligent spectrum monitoring solution suitable for research, education, telecommunications, defense applications, and edge deployment.

---

# 🎯 Project Objectives

The major objectives of this project are:

- Develop an end-to-end RF signal processing pipeline.
- Process complex IQ (In-phase & Quadrature) samples.
- Perform FFT and STFT analysis.
- Generate spectrogram datasets for AI training.
- Train deep learning models for RF signal classification.
- Detect RF interference and malicious spectrum activity.
- Identify drone communication signals.
- Detect jamming attacks.
- Detect spoofing attacks.
- Perform real-time RF spectrum monitoring.
- Export optimized AI models using ONNX.
- Accelerate inference using NVIDIA TensorRT.
- Deploy optimized models on edge AI devices.
- Visualize predictions through a modern dashboard.

---

# 🚀 Key Features

## RF Signal Processing

- IQ Sample Processing
- Digital Signal Processing
- FFT Analysis
- STFT Analysis
- Spectrogram Generation
- Signal Filtering
- Noise Analysis
- Frequency Domain Analysis
- Time Domain Analysis
- RF Signal Visualization

---

## Artificial Intelligence

- Deep Learning Models
- CNN-based RF Classification
- Transfer Learning
- Model Evaluation
- Model Comparison
- Hyperparameter Optimization
- Experiment Tracking
- Performance Benchmarking

---

## Threat Detection

- Drone Detection
- RF Jamming Detection
- RF Spoofing Detection
- Unknown Signal Detection
- Interference Classification
- Wireless Technology Classification
- Spectrum Occupancy Monitoring
- Signal Intelligence (SIGINT)

---

## Edge Deployment

- ONNX Export
- TensorRT Optimization
- Real-Time Inference
- Edge AI Deployment
- GPU Acceleration
- Low-Latency Prediction
- Production Deployment Pipeline

---

## Dashboard

- Live RF Monitoring
- Signal Visualization
- Spectrogram Viewer
- Prediction Dashboard
- Threat Alerts
- Confidence Scores
- Performance Metrics
- Interactive Charts

---

# 🏗️ System Architecture

```

                RF Signals
                     │
                     ▼
           Signal Acquisition
                     │
                     ▼
             IQ Sample Processing
                     │
                     ▼
              FFT / STFT Analysis
                     │
                     ▼
         Spectrogram Generation
                     │
                     ▼
            Deep Learning Model
                     │
                     ▼
            Threat Classification
                     │
                     ▼
          ONNX Model Conversion
                     │
                     ▼
         TensorRT Optimization
                     │
                     ▼
         Real-Time Edge Deployment
                     │
                     ▼
        FastAPI + React Dashboard

```

---

# 📂 Project Workflow

```

RF Signal

↓

IQ Samples

↓

Signal Processing

↓

FFT

↓

STFT

↓

Spectrogram Generation

↓

CNN Training

↓

Model Evaluation

↓

ONNX Export

↓

TensorRT Optimization

↓

Real-Time Prediction

↓

Dashboard Visualization

```

---
# 📁 Project Structure

```
AI-Powered-RF-Threat-Detection-Edge-Deployment-Platform
│
├── assets/                    # Images, icons and project resources
│
├── backend/                   # FastAPI backend
│
├── configs/                   # Configuration files
│
├── dashboard/                 # Monitoring dashboard
│
├── datasets/
│   ├── raw/                   # Original IQ datasets
│   ├── processed/             # Processed datasets
│   └── sample_data/           # Example datasets
│
├── docs/                      # Documentation
│
├── edge_deployment/           # ONNX & TensorRT deployment
│
├── frontend/                  # React frontend
│
├── inference/                 # Real-time inference
│
├── models/                    # Trained models
│
├── notebooks/                 # Research notebooks
│
├── scripts/                   # Utility scripts
│
├── signal_processing/         # RF signal processing modules
│
├── spectrogram_generation/    # Spectrogram generation
│
├── tests/                     # Unit tests
│
├── training/                  # Deep learning training pipeline
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 🛠️ Technology Stack

## Programming Languages

- Python
- JavaScript
- HTML
- CSS

---

## Artificial Intelligence & Deep Learning

- PyTorch
- TorchVision
- NumPy
- Scikit-Learn
- ONNX

---

## Signal Processing

- SciPy
- NumPy
- Matplotlib
- OpenCV
- FFT
- STFT

---

## Backend

- FastAPI
- Uvicorn
- Pydantic

---

## Frontend

- React
- Vite
- Axios
- Chart.js
- Recharts

---

## Edge AI

- ONNX Runtime
- NVIDIA TensorRT

---

## Development Tools

- Git
- GitHub
- VS Code
- Jupyter Notebook

---

# 📡 RF Technologies Covered

This project is designed to recognize and analyze various wireless communication technologies.

| Technology | Status |
|------------|---------|
| Wi-Fi | Planned |
| Bluetooth | Planned |
| LTE | Planned |
| 5G NR | Planned |
| GPS | Planned |
| Drone Communication | Planned |
| Radar Signals | Planned |
| Military RF Signals | Planned |
| IoT RF Signals | Planned |
| Unknown RF Signals | Planned |

---

# ⚠️ Threat Detection Modules

The platform is designed to detect multiple RF threats.

| Threat | Description |
|---------|-------------|
| Drone Detection | Detect commercial drone communication signals |
| RF Jamming | Detect intentional RF interference |
| GPS Spoofing | Detect spoofed navigation signals |
| RF Spoofing | Detect forged wireless transmissions |
| Unknown Signal Detection | Detect previously unseen RF activity |
| Spectrum Interference | Identify abnormal RF interference |
| Unauthorized Transmission | Detect unauthorized spectrum usage |
| Signal Classification | Identify wireless protocol automatically |

---

# 🔄 End-to-End AI Pipeline

The project follows a complete AI workflow.

```
RF Signal
      │
      ▼
Signal Acquisition
      │
      ▼
IQ Sample Collection
      │
      ▼
Noise Removal
      │
      ▼
Signal Processing
      │
      ▼
FFT Analysis
      │
      ▼
STFT Analysis
      │
      ▼
Spectrogram Generation
      │
      ▼
Dataset Creation
      │
      ▼
CNN Model Training
      │
      ▼
Model Evaluation
      │
      ▼
ONNX Export
      │
      ▼
TensorRT Optimization
      │
      ▼
Edge Deployment
      │
      ▼
Real-Time Threat Detection
```

---

# 🧠 Deep Learning Pipeline

The deep learning workflow consists of the following stages:

1. RF Signal Acquisition
2. IQ Sample Collection
3. Signal Preprocessing
4. Spectrogram Generation
5. Dataset Preparation
6. Data Augmentation
7. CNN Training
8. Hyperparameter Optimization
9. Model Validation
10. Performance Evaluation
11. ONNX Export
12. TensorRT Optimization
13. Real-Time Deployment

---

# 📊 Supported Signal Processing Techniques

The platform includes implementations of:

- Fast Fourier Transform (FFT)
- Short-Time Fourier Transform (STFT)
- Spectrogram Generation
- Digital Filtering
- IQ Signal Visualization
- Power Spectral Density Analysis
- Frequency Domain Analysis
- Time Domain Analysis
- Noise Reduction
- Signal Normalization
- Windowing Functions
- Feature Extraction

---

# 📦 Dataset Pipeline

The dataset preparation workflow consists of:

- RF Signal Acquisition
- IQ Sample Collection
- Data Cleaning
- Signal Segmentation
- Feature Extraction
- Spectrogram Generation
- Dataset Labeling
- Dataset Validation
- Dataset Augmentation
- Training/Validation/Test Split

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/raushan-kumar-14/AI-Powered-RF-Threat-Detection-Edge-Deployment-Platform.git
```

Enter the project directory

```bash
cd AI-Powered-RF-Threat-Detection-Edge-Deployment-Platform
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Backend

```bash
cd backend
uvicorn main:app --reload
```

Frontend

```bash
cd frontend
npm install
npm run dev
```

Training

```bash
python training/train.py
```

Inference

```bash
python inference/predict.py
```

---

# 📈 Current Development Status

| Module | Status |
|---------|---------|
| Repository Setup | ✅ Completed |
| Documentation | 🚧 In Progress |
| Signal Processing | 🚧 In Progress |
| Dataset Pipeline | 🚧 In Progress |
| Spectrogram Generation | 🚧 In Progress |
| CNN Training | 🚧 In Progress |
| Threat Detection | 🚧 In Progress |
| FastAPI Backend | 🚧 In Progress |
| React Dashboard | 🚧 In Progress |
| ONNX Export | 🚧 In Progress |
| TensorRT Optimization | 🚧 In Progress |
| Edge Deployment | 🚧 In Progress |

---
# 🧩 Core Modules

The platform is organized into modular components, allowing independent development, testing, and deployment.

| Module | Description |
|----------|-------------|
| RF Signal Processing | RF signal generation, filtering, FFT, STFT, and feature extraction |
| IQ Data Processing | Reading, preprocessing, normalization, and visualization of IQ samples |
| Spectrogram Generation | Conversion of RF signals into spectrogram images for deep learning |
| Dataset Management | Dataset preparation, preprocessing, augmentation, and labeling |
| Deep Learning | CNN-based RF signal classification and threat detection |
| Model Evaluation | Performance analysis, confusion matrix, ROC curves, and benchmarking |
| Experiment Tracking | Model comparison and experiment logging |
| Backend API | FastAPI-based inference and model
# 🗺️ Development Roadmap

The project is being developed incrementally. The roadmap below reflects the planned implementation.

## Phase 1 — RF Fundamentals

- [x] Repository Initialization
- [x] Project Structure
- [x] Documentation Setup
- [ ] RF Fundamentals
- [ ] Signal Generation
- [ ] IQ Sample Processing
- [ ] FFT Implementation
- [ ] STFT Implementation
- [ ] Spectrogram Generation

---

## Phase 2 — Dataset & AI Pipeline

- [ ] Dataset Preparation
- [ ] Data Augmentation
- [ ] CNN Architecture
- [ ] Model Training
- [ ] Hyperparameter Optimization
- [ ] Model Evaluation
- [ ] Experiment Tracking

---

## Phase 3 — RF Threat Detection

- [ ] Drone Signal Detection