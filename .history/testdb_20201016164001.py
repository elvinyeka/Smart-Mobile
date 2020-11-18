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


second_human = Human.query.get(2)
second_human.name = 'EliAbbas'
db.session.add(second_human)
db.session.commit()

print(second_human)









