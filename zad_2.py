result1 = 5
result2 = 7
result_git = 9

def fun1():
    result1 = 3
    return 'result1, result2: ' + str(result1) + str(result2)

print(fun1())
print('Result: ', result1)

def show_list(list_of_students=None):
    if list_of_students is None:  # koniecznie!
        list_of_students = []     # koniecznie!
    print("Lista jest pusta")
    print(list_of_students)
    return