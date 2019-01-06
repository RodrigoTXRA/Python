lucky_numbers = [4,5,6,1,2,45,55]
lucky_numbers.reverse()
countries = ["Brazil", "Brazil", "Australia", "Bolivia", "NZ"]
countries.append("Mexico")
countries.insert(1, "Argentina")
countries.extend(lucky_numbers)
countries_copy = countries.copy()
print(countries)
print(lucky_numbers)
print(countries.index("Brazil"))
print(countries.count("Brazil"))
print(countries_copy)
