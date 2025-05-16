# Aravind763-AirQuality-Vibration-S25-PANSLAB-Aravind
Air Quality and Vibration Monitoring System

Author
Aravind Balasubramaniam
Advisor: Professor Shijia Pan
Lab: Persuasive Autonomous Networks Lab
Masters Student: Dong Yoon Lee

---

Overview

This is my work for Spring 2025 for the PANS lab and mainly consists of a system for monitoring and visualizing indoor air quality and vibration data. This semester-long project integrates:

- Python-based feature extraction and classification experiments on vibration datasets (early semester work )
- Real-time data capture and waveform visualization using Python + matplotlib
- Interactive blueprint-based sensor placement and data visualization via React Native + Expo
- UDP/WebSocket communication for live data streaming between Python backend and React Native frontend

---

File & Component Breakdown

Early Semester Python Projects

vib.py
- Extracts statistical features (mean, peak, etc.) from raw vibration data
- Foundation for signal normalization methods later used in real-time waveform plotting
- Requires PyTorch:
  pip3 install torch

iris.py
- Trains a decision tree classifier on the Iris dataset
- Introduces concepts of supervised learning and accuracy evaluation
- Users can try to request a set amount of random or species- specific samples until they    
  are exhausted

irisCross.py
- Enhances iris.py with K-Fold cross-validation for robust evaluation
- Builds pipeline and model generalization skills using sklearn

---

React Native Web App (Expo)

App.js
- Displays 4 movable and renameable sensor nodes (Kitchen, Bath, Living, Bedroom) on a house blueprint
- Tabs for:
  - Static CSV-based graph visualization  with JSON format that displays on a website
  - Terminal view for live vibration waveform
- Edit mode allows drag-and-drop sensor placement
- Expo Web/WebSocket compatibility for real-time updates

---

Python UDP Backend

capture_udp_to_csv.py
- Receives live float values via UDP and logs to CSV
- User will have to be connected to same network as the device, the IP in the code can be changed to reflect this
- Drives static graph data for the frontend


plot_waveform.py
- Plots incoming sensor values in real time using matplotlib
-Outputs as a PNG after being on the proper UDP socket
- Index-based X-axis gives waveform-like signal view, reacting to changes in vibration
- Base64-encodes plot PNGs and broadcasts them for frontend visualization
- While PNGs sometimes fail to render correctly in the frontend, the matplotlib live waveform display continues functioning reliably after data collection completes. You can print this on the terminal

---

Build & Dependencies

Python
- Python 3.x
- Libraries required: matplotlib, socket, torch, scikit-learn
Install with:
  pip3 install matplotlib torch scikit-learn

React Native / Expo
- Node.js + npm
- Expo CLI:
  npm install -g expo-cli
- Required packages: react-native-chart-kit, react-native-svg, react-native-gesture-handler

Run with:
  npm install
  npx expo start

---

Features & Functionality

✅ Implemented & Working
- Early feature extraction and classification from vibration data
- Real-time UDP packet reception and graph rendering
- Z-score normalized vibration waveform with matplotlib
- React Native blueprint UI with interactive nodes
- WebSocket fallback for mobile UDP restrictions

⚠️ Known Issues 
- Sensor positions not yet persisted across sessions
- PNG waveform previews may fail intermittently on frontend terminal tab

---

How to Run

Python
  python3 capture_udp_to_csv.py
  python3 plot_waveform.py
  node udp‑ws‑bridge.js     

React Native
  npx expo start

---

Acknowledgements & License

Aravind Balasubramaniam
Professor Shijia Pan
Persuasive Autonomous Networks Lab, UC Merced
Masters Student: Dong Yoon Lee
License: MIT © Aravind Balasubramaniam
