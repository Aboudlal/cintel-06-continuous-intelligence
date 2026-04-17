# 🚀 Continuous Intelligence Portfolio
## 👤 Abdellah Boudlal
📅 2026-04

---

## 📌 Overview
This page summarizes my work on Continuous Intelligence (CI) projects.
Throughout this course, I built a complete pipeline to monitor systems, detect anomalies, analyze trends, and identify drift.

---

# 🧠 1. Professional Project
🔗 **Repository:**
👉 https://github.com/Aboudlal/cintel-06-continuous-intelligence

### ⚙️ Tools & Technologies
- Python
- Polars
- Logging system
- GitHub

### 📝 Description
This project implements a full continuous intelligence pipeline that monitors system performance using metrics like requests, errors, and latency.

---

# 🚨 2. Anomaly Detection
🔗 **Repository:**
👉 https://github.com/Aboudlal/cintel-02-static-anomalies

### 🧪 Techniques
Anomalies are detected using predefined thresholds.
For example, if `error_rate` or `latency` exceeds a limit → anomaly is triggered.

### 📂 Artifacts
👉 https://github.com/Aboudlal/cintel-02-static-anomalies/tree/main/artifacts

These files contain logs and anomaly reports.

### 💡 Insights
This helped identify when the system performance becomes unstable.

---

# 📊 3. Signal Design
🔗 **Repository:**
👉 https://github.com/Aboudlal/cintel-03-signal-design

### 🔍 Signals Created
- `error_rate = errors / requests`
- `avg_latency_ms = total_latency_ms / requests`

### 📂 Artifacts
👉 https://github.com/Aboudlal/cintel-03-signal-design/tree/main/artifacts

### 💡 Insights
Derived signals provide clearer insights than raw data.

---

# 📈 4. Rolling Monitoring
🔗 **Repository:**
👉 https://github.com/Aboudlal/cintel-04-rolling-monitoring

### 🔄 Techniques
Used rolling windows to compute:
- Rolling mean
- Rolling standard deviation

### 📂 Artifacts
👉 https://github.com/Aboudlal/cintel-04-rolling-monitoring/tree/main/artifacts

### 💡 Insights
Helped detect trends and reduce noise in the data.

---

# 🔁 5. Drift Detection
🔗 **Repository:**
👉 https://github.com/Aboudlal/cintel-05-drift-detection

### 📉 Techniques
Compared current data to a baseline.
Drift is detected when values stay above/below baseline for multiple windows.

### 📂 Artifacts
👉 https://github.com/Aboudlal/cintel-05-drift-detection/tree/main/artifacts

### 💡 Insights
Identified long-term system changes and performance degradation.

---

# 🤖 6. Continuous Intelligence Pipeline
🔗 **Repository:**
👉 https://github.com/Aboudlal/cintel-06-continuous-intelligence

### 🔗 Techniques Combined
- Signal design
- Anomaly detection
- Rolling monitoring
- Drift detection

### 📂 Artifacts
👉 https://github.com/Aboudlal/cintel-06-continuous-intelligence/tree/main/artifacts

### 📊 Assessment
The pipeline gives a clear view of system health and helps detect issues early for better decision-making.

---

# ✅ Final Thoughts
This project helped me understand how to monitor systems in real-time and make data-driven decisions using continuous intelligence.
