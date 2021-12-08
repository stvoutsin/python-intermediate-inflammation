"""Tests for the Patient model."""
import pytest


def test_create_patient():
    """Test creating a patient"""
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_patient_equality():
    """Test comparison between Patients"""
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)
    p.add_observation(1,0)

    second_name = 'Alice'
    p2 = Patient(name=second_name)
    p2.add_observation(1,0)

    third_name = 'Alice'
    p3 = Patient(name=third_name)
    p3.add_observation(2,0)

    fourth_name = 'John'
    p4 = Patient(name=fourth_name)
    p4.add_observation(2,0)

    fifth_name = 'John'
    p5 = Patient(name=fifth_name)
    p5.add_observation(2,0)
    p5.add_observation(4,1)

    assert p == p2
    assert p2 != p3
    assert p3 != p4
    assert p4 != p5

def test_observation():
    """Test creating an Observation"""
    from inflammation.models import Observation
    obs_day = 0
    obs_value = 5
    observation = Observation(obs_value, obs_day)

    assert observation.value == obs_value
    assert observation.day == obs_day

def test_person():
    """Test Person comparison"""
    from inflammation.models import Person
    name = "Alice"
    p = Person(name)
    p2 = Person("Alice")
    p3 = Person("John")

    assert p.name == name
    assert p == p2
    assert str(p) == str(p2)
    assert p != p3

def test_observation_equality():
    """Test Observation comparison"""
    from inflammation.models import Observation
    obs_day = 0
    obs_value = 5
    third_obs_day = 1
    third_obs_value = 6
    observation = Observation(obs_value, obs_day)
    second_observation = Observation(obs_value, obs_day)
    third_observation =  Observation(third_obs_value, third_obs_day)
    assert observation.value == obs_value
    assert observation.day == obs_day
    assert observation == second_observation
    assert observation != third_observation


def test_add_observation():
    """Test process of adding an Observation"""
    from inflammation.models import Patient
    from inflammation.models import Observation

    name = 'Alice'
    p = Patient(name=name)
    obs_day = 0
    obs_value = 5
    second_obs_value = 7
    observation = Observation(obs_value, obs_day)
    second_observation = Observation(second_obs_value, 1)
    new_obs = p.add_observation(obs_value)
    second_new_obs = p.add_observation(second_obs_value)

    assert new_obs == observation
    assert second_new_obs == second_observation


def test_get_observation_by_day():
    """Test getting an observation by day"""
    from inflammation.models import Patient
    from inflammation.models import Observation

    name = 'Alice'
    p = Patient(name=name)
    obs_day = 0
    obs_value = 5

    with pytest.raises(Exception):
        p.get_observation_by_day(obs_day)

    p.add_observation(obs_value, obs_day)
    observation = Observation(obs_value, obs_day)

    with pytest.raises(IndexError):
        p.get_observation_by_day(-1)

    assert p.get_observation_by_day(obs_day) == observation


def test_create_doctor():
    """Test creating a doctor"""
    from inflammation.models import Doctor

    name = 'John'
    d = Doctor(name=name)

    assert d.name == name


def test_doctor_add_patient():
    """Test adding a patient to a doctor"""
    from inflammation.models import Doctor
    from inflammation.models import Patient

    doctor_name = 'John'
    d = Doctor(name=doctor_name)

    patient_name = 'Alice'
    p = Patient(name=patient_name)
    d.add_patient(p)

    patient_name_2 = 'Sarah'
    p2 = Patient(name=patient_name_2)
    d.add_patient(p2)

    # Add patient again
    d.add_patient(p2)

    assert d.patients[0] == p


def test_doctor_get_patient_by_name():
    """Test getting a patient from a doctor by name"""
    from inflammation.models import Doctor
    from inflammation.models import Patient

    doctor_name = 'John'
    d = Doctor(name=doctor_name)

    patient_name = 'Alice'
    p = Patient(name=patient_name)

    d.add_patient(p)

    assert d.get_patient_by_name(patient_name) == p


def test_doctor_get_patient_by_name_fails():
    """Test getting a patient from a doctor by name / when parameters are invalid"""
    from inflammation.models import Doctor
    from inflammation.models import Patient

    doctor_name = 'John'
    d = Doctor(name=doctor_name)

    patient_name = 'Alice'
    p = Patient(name=patient_name)

    second_patient_name = 'Sarah'
    d.add_patient(p)

    with pytest.raises(KeyError):
        d.get_patient_by_name(second_patient_name)
