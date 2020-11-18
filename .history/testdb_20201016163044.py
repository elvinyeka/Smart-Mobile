from test import  db, Human

#Create
''' db.create_all() 
human1 = Human('Elvin', 36)
human2 = Human('Samir',41)
human3 = Human('Mehemmed', 28)

db.session.add_all([human1,human2,human3])
db.session.commit()

print(human1.id)
print(human2.id)
print(human3.id) '''

#read

# all_humans = Human.query.all()
# print(all_humans)

# humanx = Human.query.get(2)
# print(humanx.age)


####Update


# first_human = Human.query.get(1)
# first_human.age = 100
# db.session.add(first_human)
# db.session.commit()

# print(first_human)

second_human = Human.query.get(2)
second_human.age = 85
db.session.add(second_human)
db.session.commit()

print(second_human)







