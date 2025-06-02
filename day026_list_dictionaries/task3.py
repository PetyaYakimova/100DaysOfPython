student_dict = {
    "student": ["Adam", "Pamela", "Lilly"],
    "score": [56, 78, 98]
}

# Loop through dictionaries
for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through data frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
