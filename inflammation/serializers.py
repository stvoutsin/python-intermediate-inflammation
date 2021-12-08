"""
Module to handle serialization of Patient &  Observation classes
"""
import json
import csv
from abc import ABC, abstractmethod
from inflammation import models


class Serializer(ABC):
    """Abstract Serializer class"""

    @classmethod
    @abstractmethod
    def serialize(cls, instances):
        """
        Serialize an instance
        """

    @classmethod
    @abstractmethod
    def deserialize(cls, data):
        """
        Deserialize data
        """


class ObservationSerializer(Serializer):
    """Observation Serializer class"""
    model = models.Observation

    @classmethod
    def serialize(cls, instances: list) -> list:
        """
        Serialize an Observation
        :param instances:
        :return: list of serialized observations
        """
        return [{
            'day': instance.day,
            'value': instance.value,
        } for instance in instances]

    @classmethod
    def deserialize(cls, data):
        """
        Deserialize a list of observations
        :param data:
        :return: list of deserialized observations
        """
        return [cls.model(**d) for d in data]


class PatientSerializer(Serializer):
    """Patient Serializer class"""
    model = models.Patient

    @classmethod
    def serialize(cls, instances: list) -> list:
        """
        Serialize a Patient
        :param instances:
        :return: list of serialized patients
        """
        return [{
            'name': instance.name,
            'observations': ObservationSerializer.serialize(instance.observations),
        } for instance in instances]

    @classmethod
    def deserialize(cls, data: list) -> list:
        """
        Deserialize a list of patients
        :param data:
        :return: list of deserialized patients
        """
        instances = []

        for item in data:
            item['observations'] = ObservationSerializer.deserialize(item.pop('observations'))
            instances.append(cls.model(**item))

        return instances


class PatientJSONSerializer(PatientSerializer):
    """Patient JSON Serializer class"""
    @classmethod
    def save(cls, instances: list, path: str) -> None:
        """
        Save a list of patients to a json file
        :param path: The path of the file
        :param instances: The list of patients
        :return: None
        """
        with open(path, 'w', encoding="utf-8") as jsonfile:
            json.dump(cls.serialize(instances), jsonfile)

    @classmethod
    def load(cls, path: str) -> list:
        """
        Load a json file
        :param path: The path of the file
        :return: The deserialized data
        """
        with open(path, encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        return cls.deserialize(data)


class PatientCSVSerializer(PatientSerializer):
    """Patient CSV Serializer class"""
    @classmethod
    def save(cls, instances: list, path: str) -> None:
        """
        Save a list of patients to a csv file
        :param path: The path of the file
        :param instances: The list of patients
        :return:
        """
        try:
            with open(path, 'w', encoding="utf-8") as csvfile:
                csvfile.write("name,")
                for i in range(len(instances)):
                    csvfile.write(f"{i},")

                csvfile.write("\n")
                for instance in instances:
                    csvfile.write(f"{instance.name},")
                    for observation in instance.observations:
                        csvfile.write(f"{observation},")
                    csvfile.write("\n")

        except IOError:
            print("I/O error")

    @classmethod
    def load(cls, path: str) -> list:
        """
        Load a csv file
        :param path: The path of the file
        :return: The deserialized data
        """
        data = []
        with open(path, encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                patient = {"observations": []}
                for key, val in row.items():
                    if key != "name" and val:
                        patient["observations"].append({"value": float(val), "day": int(key)})
                    elif key == "name" and val:
                        patient["name"] = val
                data.append(patient)

        return cls.deserialize(data)
