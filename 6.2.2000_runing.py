from timeit import default_timer


# define a function that get a function and her parameter as a parameter and check the time it takes to run
def timer(func,*args ,**kwargs):
    start = default_timer()
    func(*args,**kwargs)
    end = default_timer()
    return end - start



'''x =timer("Hi {name}".format, name="Bug")
print(x)
Y =timer(zip, [1, 2, 3], [4, 5, 6])
print(Y)'''