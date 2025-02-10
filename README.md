# DICOM-HL7-API 🏥📡

A simple **Flask-based API** that allows you to **upload, process, and extract metadata from DICOM files** while also **generating HL7 messages**. This project demonstrates interoperability between **DICOM (Digital Imaging and Communications in Medicine) and HL7 (Health Level 7) standards**, commonly used in medical imaging and healthcare systems.

## 🚀 Features

✅ Upload and store **DICOM** files.  
✅ Extract **metadata** (Patient ID, Name, Study Date, etc.).  
✅ Convert DICOM metadata into **HL7 v2.5** message format.  
✅ RESTful API with **Swagger documentation** for easy testing.  
✅ Fully tested with **unit tests for endpoints and core functions**.

## 🛠️ Technologies

- **Python** (Flask, pydicom, hl7, pytest)
- **Flasgger** (Swagger UI for API documentation)
- **Werkzeug** (File handling)

## 📌 Endpoints Overview

| **Method** | **Endpoint**             | **Description**                 |
| ---------- | ------------------------ | ------------------------------- |
| **POST**   | `/dicoms/`               | Upload a DICOM file             |
| **GET**    | `/dicoms/<filename>`     | Retrieve DICOM metadata         |
| **GET**    | `/dicoms/<filename>/hl7` | Generate HL7 message from DICOM |

## 📖 Setup & Usage

### 1️⃣ **Create and Activate Virtual Environment**

#### **On Bash (Linux/macOS)**

```bash
python -m venv env
source env/bin/activate
```

#### **On PowerShell (Windows)**

```powershell
python -m venv env
env\Scripts\Activate.ps1
```

### 2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt

```

### 3️⃣ **Set Environment Variable for Flask**

#### **On Bash (Linux/macOS)**

```bash
export FLASK_APP=main.py

```

#### **On PowerShell (Windows)**

```powershell
$env:FLASK_APP = "main.py"
```

```cmd
set FLASK_APP=main.py
```

4️⃣ **Run the API**

```bash
flask run
```
