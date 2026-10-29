# 🏦 CNAB Processing API

> A robust, automated backend API for parsing, validating, and processing CNAB (Centro Nacional de Automação Bancária) files.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/joaogdellagnolo/cnab-processing-api/graphs/commit-activity)

## 📌 Overview
Dealing with legacy bank remittance files (CNAB 240 / 400) is notoriously error-prone and time-consuming. This API automates the ingestion and validation of banking data, ensuring financial compliance, reducing manual operational overhead, and integrating seamlessly into modern ERPs or financial dashboards.

Built with **Python**, this system acts as a reliable middleware between legacy banking outputs and modern database structures.

## 🚀 Key Features
- **Multi-Format Parsing:** Supports parsing and structural validation for both CNAB 240 and CNAB 400 standards.
- **Data Sanitization & Validation:** Ensures data integrity (dates, monetary values, CPFs/CNPJs) before persisting to the database.
- **RESTful Endpoints:** Easy-to-use endpoints to upload files, check processing status, and retrieve parsed financial records.
- **Error Tracing:** Detailed logging and error mapping to quickly identify corrupted or malformed lines in the bank files.

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI (or Flask/Django - update as needed)
- **Database:** PostgreSQL / SQLite
- **Containerization:** Docker & Docker Compose
- **Data Processing:** Regex, Pandas (if applicable)

## ⚙️ Architecture

1. **Upload:** Client posts a `.TXT` CNAB file to the `/upload` endpoint.
2. **Parsing Pipeline:** The API reads the file sequentially, identifying headers, detailed batches, and footers based on standard banking layouts.
3. **Validation:** Field-level validation ensures no garbage data enters the financial pipeline.
4. **Persistence:** Validated records are normalized and stored in the SQL database.

## 💻 Getting Started

### Prerequisites
- Python 3.9+
- Docker (Optional, but recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/joaogdellagnolo/cnab-processing-api.git
cd cnab-processing-api
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Run the development server:
```bash
uvicorn main:app --reload
```

## 📡 API Endpoints (Example)

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/cnab/upload` | Upload a CNAB file for processing |
| `GET` | `/api/v1/cnab/transactions` | List all processed financial transactions |
| `GET` | `/api/v1/cnab/status/{job_id}` | Check the parsing status of a large file |

## 🤝 Contribution
This project was developed to automate financial routines and integrate complex systems. Feel free to open issues or submit pull requests if you want to improve the parsing logic for specific banks (e.g., Itaú, Bradesco, Banco do Brasil).

---
*Developed by [João Guilherme Dell'Agnolo](https://www.linkedin.com/in/joaogdellagnolo/) - Software Engineer focused on Backend & Automation.*