# If statements are either true or false
# If condition is true it will action something otherwise it action sth else
# boolean variable below
is_male = True
is_tall = True
# Using OR one of the condition can be true
# Using AND both conditions must be true
if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male and is tall")
else:
    print("You are neither male or tall")