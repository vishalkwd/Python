# def add_name(func):
#     def wrapper():
#         print("This is an inner function")
#         func()
#     return wrapper

# # @add_name
# def say_hello():
#     print("hello world!")

# # message = add_name(say_hello) # Either use this or decorator symbol

# message()

# -------------------------------------------------------------------------------------------------
# def pretty_sumab(func):
#     def inner(a,b):
#         print(str(a) + " + " + str(b) + " is ", end="")
#         return func(a,b)
#     return inner

# @pretty_sumab
# def sumab(a,b):
#     summed = a + b
#     print(summed)

# if __name__ == "__main__":
#     sumab(5,3)

# -------------------------------------------------------------------------------------------------

# import time

# def measure_time(func):
#     def wrapper(*args):
#         t = time.time()
#         res = func(*args)
#         print(f"Time took for execution is: {time.time()-t} seconds")
#         return res
#     return wrapper

# @measure_time
# def my_func(n):
#     time.sleep(n)

# if __name__ == "__main__":
#     my_func(2)