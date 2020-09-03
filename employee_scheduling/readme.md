## Employee Scheduler

This program is designed to read a csv output from Google Form responses along with *_shift_requirements.csv_*, and *_overlap.csv_*, then formulate the employee scheduling problem as an Integer Programming model. In order to use this program, you must supply:

* form_responses.csv
* overlap.csv
* shift_requirements.csv
* preference_scheme.json

Each file's example are included with this repository.

## preference_scheme.json

This file defines your own "preference" scheme, which will be a part of Google Form answer. An example of such scheme is as follow:

* 1 = The employee prefers this shift
* 2 = The employee is okay with this shift
* 3 = The employee dislikes this shift
* leave blank if the employee cannot make this shift

The bigger the number, the less likely that the employee will be assigned the shift.

The program will read in this preference scheme, then replace verbal response in the form response with the corresponding number before feeding to the integer programming model.
