# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/stvoutsin/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

[Debian] For Debian machines, the following system libraries are required if they are not already installed:

- libjpeg-dev 
- zlib1g-dev
- gcc 
- libpq-dev -y

To install these run: 
```
apt-get install libjpeg-dev zlib1g-dev gcc libpq-dev -y
```

## Installation

  - Clone the repository:
    
    ```
    git clone https://github.com/stvoutsin/python-intermediate-inflammation
    cd python-intermediate-inflammation/
    ```

  - Create a virtual Environment

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

  - Install requirements
    ```
    pip3 install -r requirements.txt
    ```   

  - Install Inflam library
    ```
    python3 setup.py install
    ```

## Usage

python inflammation-analysis.py [--view visualize|record] [--patient <patient number>] <data/datafile>

## Contact Information

You can contact me for any questions, issues or information on this project at my github account: @stvoutsin

## Credits

Credits to the Carpentry Incubator project & team at: https://github.com/carpentries-incubator/python-intermediate-inflammation

## Licence
Inflam is available under the GNU license. See the LICENSE file for more info.


