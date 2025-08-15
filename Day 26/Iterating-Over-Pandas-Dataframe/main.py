import pandas
student_dict={
    "students" : ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie'],
    "scores" : [37, 53, 82, 77, 84, 45]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#loop through the rows in dataframe
# .iterrows (Method):

for index, value in student_data_frame.iterrows():
    print(index)
    print(value)