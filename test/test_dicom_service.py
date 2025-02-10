import os
import pytest
from werkzeug.datastructures import FileStorage
from src.dicom_service import save_dicom_file, get_dicom_metadata

DICOM_TEST_FOLDER = os.path.join(os.getcwd(), "test", "dicom_file_test")


@pytest.fixture
def dummy_dicom():
    """Use an existing DICOM file from dicom_file_test/"""
    dicom_file = os.path.join(DICOM_TEST_FOLDER, "test_dicom.dcm")

    if not os.path.exists(dicom_file):
        raise FileNotFoundError(f"Test DICOM file not found: {dicom_file}")

    return dicom_file


def test_save_dicom_file(dummy_dicom):
    """Test saving a DICOM file"""
    with open(dummy_dicom, "rb") as file:
        file_obj = FileStorage(stream=file, filename="test.dcm")
        saved_path = save_dicom_file(file_obj)

    assert os.path.exists(saved_path)


def test_get_dicom_metadata(dummy_dicom):
    """Test extracting metadata from a DICOM file"""
    metadata = get_dicom_metadata(dummy_dicom)

    assert "PatientID" in metadata
    assert "PatientName" in metadata
    assert "Modality" in metadata
