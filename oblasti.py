def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
#inner_function()             её нельзя вызвать т.к. её пока что не существует
test_function()