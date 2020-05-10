# 5/8/2020
def counter(func):
      def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return wrapper.count
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))