#Coding Exercise: Create a dictionary that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {word:len(word) for word in sentence_list}
print(result)

# Coding Exercise: Create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day : ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)