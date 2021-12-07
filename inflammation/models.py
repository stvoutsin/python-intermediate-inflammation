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


def daily_mean(data):
    """
    Calculate the daily mean of a 2D inflammation data array.

    :param list data: 2D array of data
    :returns: Array of mean values for the day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """
    Calculate the daily max of a 2D inflammation data array.

    :param list data:  2D array of data
    :returns: Array of max values for the day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """
    Calculate the daily min of a 2D inflammation data array.

    :param list data:  2D array of data
    :returns: Array of minimum values for the day
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.
    Any NaN values are ignored, and normalised to 0

    :param data: 2d array of inflammation data
    :type data: ndarray

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
