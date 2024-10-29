def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()  #происходит вызов фунцкии inner_function
inner_function() #вызов функции не происходит, т.к. она находится в области видимости функции test_function