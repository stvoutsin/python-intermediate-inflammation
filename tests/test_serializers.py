# file: tests/test_serializers.py

from inflammation import models, serializers
from inflammation.serializers import PatientJSONSerializer
from inflammation.serializers import PatientCSVSerializer


def test_patients_json_serializer():
    """Test JSON Serializer"""

    # Create some test data
    patients = [
        models.Patient('Alice', [models.Observation(i + 1, i) for i in range(3)]),
        models.Patient('Bob', [models.Observation(2 * i, i) for i in range(3)]),
        models.Patient('Sarah', [])
    ]

    # Save and reload the data
    output_file = 'patients.json'
    serializers.PatientJSONSerializer.save(patients, output_file)
    patients_new = PatientJSONSerializer.load(output_file)

    # Check that we've got the same data back
    for patient_new, patient in zip(patients_new, patients):
        assert patient_new == patient


def test_patients_csv_serializer():
    """Test CSV Serializer"""

    # Create some test data
    patients = [
        models.Patient('Alice', [models.Observation(i + 1, i) for i in range(3)]),
        models.Patient('Bob', [models.Observation(2 * i, i) for i in range(3)]),
        models.Patient('Sarah', [])
    ]

    # Save and reload the data
    output_file = 'patients.csv'
    serializers.PatientCSVSerializer.save(patients, output_file)
    patients_new = PatientCSVSerializer.load(output_file)

    # Check that we've got the same data back
    for patient_new, patient in zip(patients_new, patients):
        assert patient_new == patient
