import os
import pytest
from src.app import app

DICOM_TEST_FOLDER = os.path.join(os.getcwd(), "test", "dicom_file_test")


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def dummy_dicom():
    """Use an existing DICOM file from dicom_file_test/"""
    dicom_file = os.path.join(DICOM_TEST_FOLDER, "test_dicom.dcm")

    if not os.path.exists(dicom_file):
        raise FileNotFoundError(f"Test DICOM file not found: {dicom_file}")

    return dicom_file


def test_upload_dicom(client, dummy_dicom):
    """Test uploading a DICOM file"""
    with open(dummy_dicom, "rb") as file:
        response = client.post("/dicoms/", data={"file": file})

    assert response.status_code == 201
    assert "File uploaded successfully" in response.get_json()["message"]
