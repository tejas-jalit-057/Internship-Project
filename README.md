# 🚀 API Health Checker – CLI Networking Tool

A powerful command-line tool to monitor the health of multiple APIs and microservices with a **clean, color-coded terminal report**.  
Built to solve a real-world backend problem faced during microservice and API-based development.

---

## 📌 Problem Statement

Modern applications heavily depend on:
- Multiple microservices
- Third-party APIs

If any API becomes slow or unavailable, it can impact the entire system.  
Manually checking each API in a browser is inefficient, time-consuming, and not scalable.

---

## ✅ Solution

**API Health Checker** is a CLI-based networking tool that:
- Checks the availability of multiple APIs at once
- Measures response time (latency)
- Identifies slow, failed, or unreachable services
- Displays a clear and color-coded health report in the terminal

This enables developers to quickly diagnose API health issues.

---

## ✨ Key Features

- 🔍 Monitor multiple APIs in one execution
- 🎨 Color-coded terminal output for quick visibility
- ⏱ Measure API response time (latency)
- 🚦 Latency-based health classification
- ⚠ Graceful handling of timeouts and network errors
- 🧩 Configurable via CLI arguments
- 📊 Summary report for overall system health

---

## 📊 Health Status Logic

| Status | Meaning |
|------|--------|
| 🟢 FAST | API is healthy and responsive |
| 🟡 SLOW | API is reachable but slow |
| 🔴 DOWN | API is unavailable or failed |

---

## 🗂 Project Structure

api-health-checker/
├── checker.py # Main CLI script
├── apis.json # List of APIs to monitor
└── README.md # Project documentation




---

## ⚙️ Tech Stack

- **Python**
- **Requests** – HTTP networking
- **Colorama** – Color-coded terminal output
- **Argparse** – CLI argument handling

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install requests colorama





🧪 Sample Output

API Health Report
--------------------------------------------------
[FAST]     GitHub API          200   120ms
[SLOW]     Google              200   980ms
[DOWN]     Invalid API         NETWORK ERROR

Summary
--------------------------------------------------
Total APIs : 3
Healthy   : 1
Slow      : 1
Down      : 1



🟢 Green → Healthy
🟡 Yellow → Slow
🔴 Red → Down



🎯 Use Cases

Monitoring microservices architecture
Verifying third-party API availability
Backend development and debugging
DevOps-style health checks
Internship and networking-focused projects


🧠 Engineering Concepts Demonstrated

HTTP status code handling
Network error and timeout management
Latency-based performance analysis
CLI tool design
Clean code structure and reporting



🚀 Future Improvements

Parallel API checks using multithreading
Email or Slack alert notifications
Scheduled health monitoring
Export reports to CSV or JSON
Retry mechanism for failed APIs



---