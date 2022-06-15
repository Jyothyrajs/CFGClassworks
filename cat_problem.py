#how many cans of cat food we need to feed 10 cats
number_of_cats = 10
cat_eat_can_per_day = 2
cans_per_day = number_of_cats*cat_eat_can_per_day
cans_week = 7 * cans_per_day
output_day = "My {} Cats eat {} cans per day"
output_week = "My {} cats eat {} cans per week"
print(output_day.format(number_of_cats,cans_per_day))
print(output_week.format(number_of_cats,cans_week))

guest = ['Mary','Jo','Dave']
result = '.'.join(guest)
print(result)


result = ','.join(guest)
print(result)
result = '____' \
         ''.join(guest)
print(result)

result = "We are going to cinema:{} and me"
print(result.format(','.join(guest)))

names = ', '.join(guest)
result = "we are going to cinema: {names} and me".format(
     names=', '.join(guest))
print(result)


print("ASCII of S:",ord('S'))
print("character equivalent of 83:",chr(83))
print()

name = "weclome to CFG. Its Awesome"
print(name[2:10:3])
print(name[2:-1])
print(name[-7:-1])
print(name[:-10])
print(name[-10:])

