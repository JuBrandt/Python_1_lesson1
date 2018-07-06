# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print("Здравствуйте, вы вошли в программу медицинская анкета. Начинаем опрос.")

name = input("Введите ваше имя:")
surname = input("Введите вашу фамилию:")
age = int(input("Введите Ваш возраст:"))
i = int(input("Введите ваш вес:"))

while (i > 50 and i < 120) and age < 30:
    print("Вы в хорошем состоянии")
    break
if (i < 50 or i > 120) and age > 40:
    print("Вам следует обратится к врачу!")
if (i < 50 or i > 120) and (age > 30 or age < 40):
    print("Вам следует вести правильный образ жизни")
else:
    print("Вы в хорошем состоянии")



