# 5/7/2020
# Get the docstring with an attribute of count_letter()
docstring = count_letter.__doc__
# Use dir(count_letter) to determine the attributes in this function
border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

import inspect

# Get the docstring with a function from the inspect module
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

def build_tooltip(function):
      """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))