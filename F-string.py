# Python introduce it at 3.6 version.
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Krish"

print(letter.format(name,country))
print(letter.format(country,name))

print(f"Hey my name is {name} and I am from {country}.")

price = 1.22222
print(f"{price:.2f}")

print(f"{2 * 3}")   # It's type('str')

print(f"I want to use f-string like this: Hey my name is {{name}} and I am from {{country}}.")