from test import  db, human


db.create_all 
human1 = Human('Elvin', 36)
human2 = Human('Samir',41)
human3 = Human('Mehemmed', 28)

db.session.add_all([human1,human2,human3])
db.session.commit()

print(human1.id)
print(human2.id)
print(human3.id)
