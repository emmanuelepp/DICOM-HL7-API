from flask import Flask, request, jsonify, redirect
from flasgger import Swagger
from src.dicom_service import save_dicom_file, get_dicom_metadata
from src.hl7_service import generate_hl7_message
import os

# Define the upload folder and ensure it exists
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["SWAGGER"] = {
    "title": "DICOM-HL7 API",
    "description": "API for handling DICOM files and generating HL7 messages",
    "version": "1.0.0",
}

Swagger(app)


@app.route("/")
def redirect_to_docs():
    return redirect("/apidocs/")

# Endpoint to upload DICOM files


@app.route("/dicoms/", methods=["POST"])
def upload_dicom():
    """
    Upload a DICOM file
    ---
    operationId: uploadDicom
    tags:
      - DICOM
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: DICOM file to upload
    responses:
      201:
        description: File uploaded successfully
      400:
        description: No file provided
    """
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filepath = save_dicom_file(file)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": file.filename,
        "filepath": filepath
    }), 201

# Endpoint to retrieve DICOM metadata


@app.route("/dicoms/<filename>", methods=["GET"])
def get_metadata(filename):
    """
    Retrieve metadata from a DICOM file
    ---
    operationId: getDicomMetadata
    tags:
      - DICOM
    parameters:
      - name: filename
        in: path
        type: string
        required: true
        description: Name of the DICOM file
    responses:
      200:
        description: Extracted metadata
      404:
        description: File not found
    """
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    metadata = get_dicom_metadata(filepath)
    return jsonify(metadata)

# Endpoint to generate an HL7 message from a DICOM file


@app.route("/dicoms/<filename>/hl7", methods=["GET"])
def get_hl7_message(filename):
    """
    Generate an HL7 message from a DICOM file
    ---
    operationId: generateHl7FromDicom
    tags:
      - HL7
    parameters:
      - name: filename
        in: path
        type: string
        required: true
        description: Name of the DICOM file
    responses:
      200:
        description: HL7 message generated
      404:
        description: File not found
    """
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    metadata = get_dicom_metadata(filepath)
    hl7_message = generate_hl7_message(metadata)

    return jsonify({"hl7_message": hl7_message})
