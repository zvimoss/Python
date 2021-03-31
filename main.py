quantity = int(float(input('How Many Videos Are There? ')))
print(quantity)

time_shooting = int(float(input('How Many Hours Of Shooting Are There? ')))
print(time_shooting)

shooting_rate = int(float(input('What Is Your Hourly Shooting Rate? ')))
print(shooting_rate)

shooting_total = int(float(time_shooting * shooting_rate))

time_editing = int(float(input('How Many Hours Of Editing Are There? ')))
print(time_editing)

editing_rate = int(float(input('What Is Your Hourly Editing Rate? ')))
print(editing_rate)

editing_total = int(float(time_editing * editing_rate))

total_hours = int(float(time_editing+time_shooting))

unit_price = int(float(shooting_total+editing_total))

project_price = int(float(unit_price * quantity))

print(total_hours)
print(unit_price)
print(project_price)



