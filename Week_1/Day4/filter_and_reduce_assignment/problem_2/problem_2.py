"""
2. Filter Students by Grade
Given a list of dictionaries, where each dictionary represents a student with
name and grade keys, use filter() to extract students with a grade of 90 or higher.
Example
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 95}
]
"""
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 95}
]

new_students_list = list(filter(lambda x: x["grade"] > 90, students))
print("Students with 90 score or more:")
print(new_students_list)