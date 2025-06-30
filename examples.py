my_string = "Hello, World!"

length = len(my_string)
print("Length:", length)

# Lowercase and Uppercase
lower_case = my_string.lower()
upper_case = my_string.upper()
print("Lowercase:", lower_case)
print("Uppercase:", upper_case)

# Stripping whitespace
stripped_string = my_string.strip()
print("Stripped:", stripped_string)

# Counting occurrences
count_hello = my_string.count("Hello")
print("Count of 'Hello':", count_hello)

# Finding and Replacing
index_world = my_string.find("World")
replaced_string = my_string.replace("World", "Universe")
print("Index of 'World':", index_world)
print("Replaced:", replaced_string)

# Startswith and Endswith
starts_with_hello = my_string.startswith("Hello")
ends_with_world = my_string.endswith("World!")
print("Starts with 'Hello':", starts_with_hello)
print("Ends with 'World':", ends_with_world)
