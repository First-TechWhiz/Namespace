
a = int(input('Введите целое число: '))

def test_function(x):
    global a
    a = x ** 5
    def inner_function():
        global a
        if a % 2 == 0:
            print('Я в области видимости функции tect_function, а число четное!')
        else:
            print('Все не так уж хорошо, число нечетное!')
    inner_function()

test_function(a)

print(a)

# Вызвать функцию inner_function вне пространства функции test_function невозможно, т.к. функция
# inner_function является локальной: "name 'inner_function' is not defined. Did you mean: 'test_function'?".