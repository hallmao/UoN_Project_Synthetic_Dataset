
## Introduction

This project is a Python script that generates a dataset of mock medical appointments. It uses the `icalendar`, `datetime`, `faker`, and `random` libraries to create a set of appointments with random patient names, reasons for appointments, dates and times within working hours, and locations. The output is an iCalendar file that can be used for testing or demonstration purposes in healthcare software.

## Dependencies

Before running the script, you need to install the required dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

To generate a dataset, run the `generate_dataset.py` script with the `-n` option to specify the number of appointments and the `-f` option to specify the output filename. For example:

```bash
python generate_dataset.py -n 1000 -f appointments.ics
```

This will generate an iCalendar file named `appointments.ics` with 1000 mock medical appointments.

Each appointment includes a random patient name, reason for appointment, date and time within working hours, and location.

Here are some more examples of how to use the script:

```bash
python generate_dataset.py -n 500 -f small_dataset.ics
python generate_dataset.py -n 5000 -f large_dataset.ics
python generate_dataset.py -n 100 -f test_dataset.ics
```

These commands will generate datasets with 500, 5000, and 100 appointments respectively.
