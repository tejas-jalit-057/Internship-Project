# API Health Checker (CLI Tool)

## Problem Statement
In applications that depend on multiple microservices or third-party APIs, developers need a fast way to verify whether all APIs are online and responsive.

Manually checking each API is inefficient and error-prone.

## Solution
API Health Checker is a command-line tool that automatically checks the health of multiple APIs and displays a color-coded status report in the terminal.

## Features
- Checks multiple APIs at once
- Displays API status (UP / DOWN)
- Shows HTTP status codes
- Measures response time
- Color-coded terminal output
- Handles network errors and timeouts

## Tech Stack
- Python
- Requests library
- Colorama (for terminal colors)

## Project Structure


api-health-checker/
├── checker.py
├── apis.json
└── README.md



## How to Run
1. Install Python
2. Install dependencies:
3. Run the tool:


## Example Use Case
This tool is useful when working with:
- Microservices architectures
- Backend systems
- Third-party API integrations
- DevOps health monitoring

## Future Improvements
- Parallel API checks
- Slack / Email alerts
- Scheduled monitoring
- Export report to CSV
- CLI arguments for timeout