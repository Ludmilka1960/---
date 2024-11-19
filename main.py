

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()# здесь ничего не возвращает


#inner_function()# здесь выдает ошибку
# (вызов функции inner_function() вне функции test_function() приводит к появлению ошибки
#вследствие различия пространства имен)
test_function()# здесь работает