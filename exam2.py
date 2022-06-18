#Для массива целых чисел найдите непрерывный подмассив
#(содержащий хотя бы одно число), который имеет наибольшую сумму, и верните его сумму.


def calculate(array): #type hint to return an int value
    sum = 0 #keeps the total sum
    result = 0 #return value
    for i in array:
        sum = max(0, sum) + int(i)
        result = max(result, sum)
    if result == 0:
        print(max(array))
    else:
        print(result)


array = input("Enter sequence of numbers: ").split(" ")
sum = 0
result = 0
for i in array:
    sum = max(0, sum) + int(i)
    result = max(result, sum)
if result == 0:
    print(max(array))
else:
    print(result)

#На вход подается натуральное число n(0 < n <= 1000).Вернуть строковое
#значение 'true', если число простое, иначе вернуть 'false'.

#Простое число - это натуральное число, единственными делителями
#которого являются только оно само и единица.(1 - не является простым числом)

number = input("Enter a number: ")
is_simple = "true"

for i in range(2, 10, 1):
    if int(number) % i == 0:
        is_simple = "false"
if int(number) == 1:
    is_simple = "false"
if int(number) == 2 or int(number) == 3 or int(number) == 5 or int(number) == 7:
    is_simple = "true"
print(is_simple)



#Дано 2 строки, переданные через пробел. Вернуть строковое значение 'true',
# если строки являются анаграммами, иначе вернуть 'false'.

#Анаграмма – это слово или фраза, образованная путем перестановки букв другого слова или фразы,
# с использованием всех исходных букв ровно один раз.

#Sample Input 1:
#австралопитек ватерполистка
#адстралопитек ватерполистка
#Sample Output 1:
#чертог горечь

#true
#Sample Input 2:

#пенсионерка покраснение
#Sample Output 2:
#true

letters = input("Enter letters: ").split(" ")
left_array = list(letters[0])
right_array = list(letters[1])
print(left_array)
print(right_array)
state = "true"

if len(left_array) != len(right_array):
    state = "false"

for letter_1 in left_array:
    if letter_1 in right_array:
        right_array.remove(letter_1)
    else:
        state = "false"

print(state)





#Дано целое положительное число. Вернуть сумму всех цифр этого числа.

number = input("Enter number: ")
result = 0
list = list(number)
for number in list:
    result += int(number)
print(result)

#Написать программу для нахождения площади поверхности цилиндра по его радиусу основания и высоте.
#На вход программе подается 2 дробных числа - радиус основания цилиндра и его высота.
#Ответ округлить строго до 2х знаков после запятой.
#Число пи считать равным 3.14

#Sample Input 1:
#1.80 10.69
#Sample Output 1:

#141.19
#Sample Input 2:

#0.00 44.95
#Sample Output 2:
#0.00

numbers = input("Enter numbers: ").strip().split(" ")
pi = 3.14
radius = float(numbers[0])
height = float(numbers[1])
square = 2 * pi * radius * height + 2 * pi * radius ** 2
print("{:.2f}".format(square))

#print("{:10.4f}".format(x))