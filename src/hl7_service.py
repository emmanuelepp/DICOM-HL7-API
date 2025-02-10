import hl7


def generate_hl7_message(dicom_metadata):
    """
    Generate an HL7 message based on DICOM metadata
    """
    msg = hl7.Message([
        hl7.Segment("MSH", [
            "|", "^~\\&", "FlaskDICOMApp", "Hospital", "ReceivingApp",
            "ReceivingFac", "20240209", "", "ADT^A01", "MSG0001", "P", "2.5"
        ]),
        hl7.Segment("PID", ["1", dicom_metadata["PatientID"], "", "",
                    dicom_metadata["PatientName"], "",
                    dicom_metadata["PatientBirthDate"], "M"]),
    ])

    return msg.to_er7()
