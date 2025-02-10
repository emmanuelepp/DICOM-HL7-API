import os
import pydicom

# Define the upload folder and ensure it exists
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def save_dicom_file(file):
    """
    Save a DICOM file in the uploads folder
    """
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return filepath


def get_dicom_metadata(filepath):
    """
    Extract metadata from a DICOM file
    """
    dicom_data = pydicom.dcmread(filepath)

    metadata = {
        "PatientID": dicom_data.PatientID,
        "PatientName": str(dicom_data.PatientName),
        "PatientBirthDate": dicom_data.PatientBirthDate,
        "Modality": dicom_data.Modality,
        "StudyDate": dicom_data.StudyDate
    }
    return metadata
