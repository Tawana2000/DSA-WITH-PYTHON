# You are working in a school's data team, you have a list of students, each with a name and score out of 100:
"""
data = [
    ["Ali", 85],
    ["Sara", 92],
    ["John", 78],
    ["Fatima", 92],
    ["Bilal", 85],
    ["Zara", 60]
]
"""
#Write a python program that: 1.Sorts the list first by score (descending), highest marks first, 2.If two students have the same score, sort them alphabetically by name, 3.Prints the full sorted list with both name and score clearly
class Selection_Sort:

    def school_data(self, data):
        self.data = data

        for i in range(len(data)):
            min_max = i

            for j in range(i + 1, len(data)):
                if data[j][1] > data[min_max][1]:
                    min_max = j
                
                elif data[j][1] == data[min_max][1] and data[j][0] < data[min_max][0]:
                    min_max = j

            data[i], data[min_max] = data[min_max], data[i]
        
        for name, score in data:
            print(f"{name}: ${score}")

        return data
    
data = [
    ["Ali", 85],
    ["Sara", 92],
    ["John", 78],
    ["Fatima", 92],
    ["Bilal", 85],
    ["Zara", 60]
]

SS = Selection_Sort()
SS.school_data(data)
