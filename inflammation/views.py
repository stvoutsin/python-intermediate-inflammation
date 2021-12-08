"""Module containing code for plotting inflammation data."""

import json
from matplotlib import pyplot as plt
from inflammation import serializers
from inflammation.models import Patient


def display_patient_record(patient: Patient) -> None:
    """
    Display data for a single patient

    :param patient: The patient to display
    :returns: None
    """
    print(patient.name)
    for obs in patient.observations:
        print(obs.day, obs.value)


def display_patient_as_json(patient: Patient) -> None:
    """
    Display data for a single patient in json format.

    :param patient: The patient to display
    :returns: None
    """
    output = serializers.PatientJSONSerializer.serialize([patient])
    print(json.dumps(output, indent=4, sort_keys=True))


def display_patient_as_csv(patient: Patient) -> None:
    """
    Display data for a single patient in json format.

    :param patient: The patient to display
    :returns: None
    """
    output = serializers.PatientCSVSerializer.deserialize([patient])
    print(output)


def visualize(data_dict: dict) -> None:
    """
    Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    :returns: None
    """

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()
