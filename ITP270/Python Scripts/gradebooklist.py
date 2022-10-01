
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]
print(gradebook)

gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
print(gradebook)

gradebook.remove([subjects[2], grades[2]])
gradebook.append(['poetry', 'pass'])
print(gradebook)

ls_subjects = ["political science", "spanish", "english literature", "ceramics"]
ls_grades = [80, 92, 91, 100]
ls_gradebook = [[ls_subjects[0], ls_grades[0]], [ls_subjects[1], ls_grades[1]], [ls_subjects[2], ls_grades[2]], [ls_subjects[3], ls_grades[3]]]

full_gradebook = gradebook + ls_gradebook
print(full_gradebook)
