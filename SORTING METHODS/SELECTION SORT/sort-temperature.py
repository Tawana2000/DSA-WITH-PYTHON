# You are given a list of temperatures (in C) recorded over a week: [23, 19, 25, 22, 18, 24, 20]
# Write a python function using selection sort to sort these temperatures from highest to lowest, and thenm print
# 1. The sorted list    2. The highest Temperature    3. The lowest temperature

def sort_temp(temps):

    for i in range(len(temps)):
        min_max_temp = i

        for j in range(i + 1, len(temps)):
            if temps[j] > temps[min_max_temp]:
                min_max_temp = j

        temps[i], temps[min_max_temp] = temps[min_max_temp], temps[i]

    return temps

temps = [23, 19, 25, 22, 18, 24, 20]
print(sort_temp(temps))
