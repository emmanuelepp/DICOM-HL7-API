import pytest
from src.hl7_service import generate_hl7_message


@pytest.fixture
def dicom_metadata():
    """Dummy metadata extracted from a DICOM file"""
    return {
        "PatientID": "12345",
        "PatientName": "John Doe",
        "PatientBirthDate": "19800101",
        "Modality": "MRI",
        "StudyDate": "20240209"
    }


def test_generate_hl7_message(dicom_metadata):
    """Test HL7 message generation from DICOM metadata"""
    hl7_message = generate_hl7_message(dicom_metadata)

    print(f"\nGenerated HL7 Message:\n{hl7_message}")

    assert "MSH" in hl7_message
    assert "PID" in hl7_message
    assert "12345" in hl7_message
    assert "John Doe" in hl7_message
    assert "19800101" in hl7_message
