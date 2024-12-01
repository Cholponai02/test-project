fruits = ["банан","банан", "яблоко", "мандарин"] #спиок
print(fruits)
print(fruits[1])

colors = ("красный","красный", "белый" , "зеленый") #кортеж
print(colors)
print(colors[2])

students = {  # словарь
    "Алиса": 16,
    "Siri":10,
    "Максим": 15
}
print(students)
students["Максим"] = 20 #изменение значения по ключу
print(students)
del students["Максим"] # удаление
print(students)
print(students["Siri"])
# название_словаря = {
#     ключ:значение,
#     ключ:значение
# }
bestNumbers = {
    5 : "отлично",
    13: "что-то ожидается"
}
print(bestNumbers[13])
haha = {
    True: "Это правда",
    False:"Это ложь"
}
print(haha[False])
