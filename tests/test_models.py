"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [-3, 4], [-5, 6]], [1, 6]),
    ])
def test_daily_max(test, expected):
    """Test max function works for array of zeroes and positive integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [-3, 4], [5, -6]], [-3, -6]),
    ])
def test_daily_min(test, expected):
    """Test min function works for array of zeroes and positive integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected, raises",
    [
        (
                np.array([[-1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                np.array([[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
                ValueError,
        ),
        (
                np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                np.array([[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
                None,
        ),
        (
                np.array([["Test", 2, 3], [4, 5, 6], [7, 8, 9]]),
                np.array([[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
                TypeError,
        ),
        (
                np.array([]),
                np.array([]),
                ValueError,
        ),
        (
                np.array([3]),
                np.array([3]),
                ValueError,
        ),
        (
                "Alice",
                [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
                TypeError,
        ),

    ])
def test_patient_normalise(test, expected, raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if raises:
        with pytest.raises(raises):
            npt.assert_almost_equal(patient_normalise(test), expected, decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(test), expected, decimal=2)


def test_load_txt():
    """Test Loading Numpy array from a CSV"""
    from inflammation import models

    filename = "https://raw.githubusercontent.com/stvoutsin/" \
               "python-intermediate-inflammation/" \
               "c8713a17cd7303a0e83d598a4c69cdf78fdb7624/data/inflammation-01.csv"
    inflammation_data = models.load_csv(filename)
    assert (len(inflammation_data) > 0)
