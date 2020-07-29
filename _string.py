a = str("allen")
b = '  Ben  '

# multi-line string served as comments
c = """How are you?
Pretty good!"""

d = '''Hey what's up?
Nothing bro.'''

print(a[1])             # 'l'
print(a[-3:-1])         # 'le'
print(len(a))           # 5
print("----------------------------------")

print(b)
print(b.strip())        # remove any whitespace form the beginning and the end
print(b.lower())
print(b.upper())
print(b.replace("Be", "Alle"))      # '  Allen  '
print("----------------------------------")

print(d.split(" "))     # split the string with whitespace
print("what" in d)      # True
print("apple" not in d) #True
print(a + ' ' + b.strip())          #"allen Ben"
print("----------------------------------")

# string format
name, age, height = "Allen", 21, 177
text = "My name is {}, I'm {} years old and I'm {} centimeters tall."
print(text.format(name, age, height))

# escape character: "\"(backslash) + the character you want to insert
print("He is a so-called \"monster\". ")
print("----------------------------------")
