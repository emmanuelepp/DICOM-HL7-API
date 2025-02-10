import hl7


def generate_hl7_message(dicom_metadata):
    """
    Generate an HL7 message based on DICOM metadata
    """
    msg = hl7.Message()

    # Segment MSH (Message Header)
    msh = hl7.Segment("|")
    msh.append("MSH")
    msh.append("^~\\&")
    msh.append("FlaskDICOMApp")
    msh.append("Hospital")
    msh.append("ReceivingApp")
    msh.append("ReceivingFac")

    # Date/Time of Message
    msh.append(dicom_metadata.get("StudyDate", "UNKNOWN"))
    msh.append("")
    msh.append("ADT^A01")
    msh.append("MSG0001")
    msh.append("P")
    msh.append("2.5")

    msg.append(msh)

    # Segment PID (Patient Identification)
    pid = hl7.Segment("|")
    pid.append("PID")
    pid.append("1")
    pid.append(dicom_metadata.get("PatientID", "UNKNOWN"))
    pid.append("")
    pid.append("")
    pid.append(dicom_metadata.get("PatientName", "UNKNOWN"))
    pid.append("")
    pid.append(dicom_metadata.get("PatientBirthDate", "UNKNOWN"))
    pid.append("M")

    msg.append(pid)

    return str(msg)
