n = int(input())
students = input().strip()
g6 = students.count('H')
students_extended = students + students
min_swaps = g6
for i in range(n):
    segment = students_extended[i:i+g6]
    g7 = segment.count('T')
    min_swaps = min(min_swaps, g7)
print(min_swaps)