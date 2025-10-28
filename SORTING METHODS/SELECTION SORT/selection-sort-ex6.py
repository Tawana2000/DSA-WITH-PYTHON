# You are given a list of students with their name, major, and GPA
"""Write a Python program using Selection Sort to arrange the students from highest to lowest GPA
If two students have the same GPA, sort them alphabetically by name:
students = [
    ["Zara", "Physics", 3.8],
    ["Liam", "Math", 3.9],
    ["Ava", "Biology", 3.8],
    ["Noah", "Computer Science", 3.5],
    ["Mia", "Engineering", 3.9]
]
"""

class Selection_Sort:

    def student_gpa(self, gpa):

        for i in range(len(gpa)):
            min_max_gpa = i

            for j in range(i + 1, len(gpa)):
                if gpa[j][2] > gpa[min_max_gpa][2]:
                    min_max_gpa = j
                elif gpa[j][2] == gpa[min_max_gpa][2] and gpa[j][0] < gpa[min_max_gpa][0]:
                    min_max_gpa = j

            gpa[i], gpa[min_max_gpa] = gpa[min_max_gpa], gpa[i]
        
        return gpa
    
gpa = [
    ["Zara", "Physics", 3.8],
    ["Liam", "Math", 3.9],
    ["Ava", "Biology", 3.8],
    ["Noah", "Computer Science", 3.5],
    ["Mia", "Engineering", 3.9]
]

SS = Selection_Sort()
print(SS.student_gpa(gpa))
