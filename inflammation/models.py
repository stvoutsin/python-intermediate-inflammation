"""
Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """
    Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data: np.ndarray) -> np.ndarray:
    """
    Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D array of data
    :returns: Array of mean values for the day
    """
    return np.mean(data, axis=0)


def daily_max(data: np.ndarray) -> np.ndarray:
    """
    Calculate the daily max of a 2D inflammation data array.

    :param data:  2D array of data
    :returns: Array of max values for the day
    """
    return np.max(data, axis=0)


def daily_min(data: np.ndarray) -> np.ndarray:
    """
    Calculate the daily min of a 2D inflammation data array.

    :param data:  2D array of data
    :returns: Array of minimum values for the day
    """
    return np.min(data, axis=0)


def patient_normalise(data: np.ndarray) -> list:
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.
    Any NaN values are ignored, and normalised to 0

    :param data: 2d array of inflammation data
    :returns: np.ndarray
    """
    if len(data) == 0:
        raise ValueError('Data should not be empty')

    if not isinstance(data, np.ndarray):
        raise TypeError('Data should be of type ndarray')

    if len(data.shape) != 2:
        raise ValueError('Data should be 2D')

    if np.any(data < 0):
        raise ValueError('Data values should not be negative')

    patient_max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / patient_max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


class Observation:
    """An observation of a patient's inflammation at a given day """
    def __init__(self, value, day):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if self.value == other.value and self.day == other.day:
            return True
        return False


class Person:
    """A person"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value: float, day: int = None) -> Observation:
        """
        Add an observation to a Patient

        :param value:  The value of the observation
        :param day:  The day of the observation
        :returns: Observation, The Observation that was added
        """
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)
        self.observations.append(new_observation)
        return new_observation

    def get_observation_by_day(self, day: int) -> list:
        """
        Get an observation given a specific day

        :param day:  The day
        :returns: Observation, The Observation for the given day
        """

        if not self.observations:
            raise Exception("Observations for this patient are empty")

        if day >= len(self.observations) or day < 0:
            raise IndexError("This day is out of bounds for this patient's observation list")

        return self.observations[day]

    def __eq__(self, other):
        if self.name != other.name:
            return False

        if len(self.observations) != len(other.observations):
            return False

        for i, val in enumerate(self.observations):
            if val != other.observations[i]:
                return False

        return True


class Doctor(Person):
    """A doctor in an inflammation study."""
    def __init__(self, name, patients=None):
        super().__init__(name)
        self.patients = patients

    def add_patient(self, patient: Patient) -> Patient:
        """
        Associate a patient with a doctor, i.e. add to his list

        :param patient:  The Patient to add
        :returns: Patient, The Patient that was added
        """
        if self.patients:
            for existing_patient in self.patients:
                if patient.name == existing_patient.name:
                    return patient
            self.patients.append(patient)
        else:
            self.patients = [patient]
        return patient

    def get_patient_by_name(self, name: str) -> Patient:
        """
        Get a patient by name

        :param name:  The name of the patient
        :returns: Patient, The Patient that matches the name
        """
        for patient in self.patients:
            if patient.name == name:
                return patient
        raise KeyError("Patient with name:" + str(name) + " not found")
