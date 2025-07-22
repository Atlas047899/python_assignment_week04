grades = [55, 70, 65, 40, 90, 85, 50, 77]
filter_grade = lambda x: x > 60
filter_grade_list = list(filter(filter_grade ,grades ))
bonus = lambda x : x * 1.05
final = list(map(bonus , filter_grade_list))
my_formatted_list = [ '%.2f' % elem for elem in final ]
print(my_formatted_list)