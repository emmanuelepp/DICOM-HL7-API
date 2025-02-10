import hl7
from datetime import datetime


def generate_hl7_message(dicom_metadata):
    """Generate a correctly formatted HL7 message from DICOM metadata."""
    msg = hl7.Message()
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")

    # Segment MSH
    msh = hl7.Segment()
    msh.append("MSH")
    msh.append("|")
    msh.append("^~\\&")
    msh.append("FlaskDICOMApp")
    msh.append("Hospital")
    msh.append("ReceivingApp")
    msh.append("ReceivingFac")
    msh.append(current_datetime)
    msh.append("")
    msh.append("ADT^A01")
    msh.append("MSG0001")
    msh.append("P")
    msh.append("2.5")
    msg.append(msh)

    patient_id = dicom_metadata.get("PatientID", "UNKNOWN")
    patient_name = dicom_metadata.get(
        "PatientName", "UNKNOWN").replace(",", "^")
    patient_birthdate = dicom_metadata.get("PatientBirthDate", "UNKNOWN")

    # Segment PID
    pid = hl7.Segment()
    pid.append("PID")
    pid.append("1")
    pid.append("")
    pid.append(f"{patient_id}^^^DICOM")
    pid.append("")
    pid.append(patient_name)
    pid.append("")
    pid.append(patient_birthdate)
    pid.append("M")

    msg.append(pid)

    return str(msg)
