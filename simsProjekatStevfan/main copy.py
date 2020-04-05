from student import Student
from nepolozeni_predmet import NepolozeniPredmet
from polozeni_predmet import PolozeniPredmet
import pickle
from serial_file_handler import SerialFileHandler


# oop = PolozeniPredmet("Objektno Orjentisano Programiranje", "Bla Bla BlA", 10)
# mat = PolozeniPredmet("Matematika 2", "Bla Bla BlA", 10)
# stp = PolozeniPredmet("Strukture Podataka I Algoritme", "Bla Bla BlA", 10)
# mreze = PolozeniPredmet("Mreze", "Bla Bla BlA", 10)

# npoop = NepolozeniPredmet("Objektno Orjentisano Programiranje", "Bla Bla BlA", 2)
# npmat = NepolozeniPredmet("Matematika 2", "Bla Bla BlA", 3)
# npstp = NepolozeniPredmet("Strukture Podataka I Algoritme", "Bla Bla BlA", 4)
# npmreze = NepolozeniPredmet("Mreze", "Bla Bla BlA", 5)



# # Inicijalnoi podaci o Studentu
# data = []
# data.append(Student("2018/123", "Marko Markovic", [oop, mat, stp, mreze], []))
# data.append(Student("2018/456", "Pera Peric", [oop], [npmat, npstp, npmreze]))
# data.append(Student("2018/789", "Stanko Stankovic", [mat], [npoop, npstp, npmreze]))

# #Inicijalnoi podaci o Nastavniku



# #Poenta sa pickleom je da se podaci upisu u fajl u binarnom formatu. Zasto binarnom? Jer ih nije moguce procitati.
# with open("student_data", 'wb') as data_file:
#     pickle.dump(data, data_file) #koristimo pickle da bismo serijalizovali u binarnu datoteku

# #Isto to je uradjeno i sam nastavnicima.

serial_file_handler_for_students = SerialFileHandler("student_data", "student_metadata.json") #pri instanciranju samo prosledimo putanje do datoteka sa podacima i sa metapodacima
# #ovo bi se moglo smanjiti na jedan argument za konstrukciju filehandler-a, ukoliko uvedemo neku konvenciju za imenovanje datoteka

# # print(serial_file_handler_for_students.get_one("2018/123").ime)

# serial_file_handler_for_students.insert(Student("2018/124", "Milan Milanovic",[],[]))

# # print(serial_file_handler_for_students.get_one("2018/124").predmeti)

# # print(nastavnik_serial_file_handler.get_one("14").ime)
# # print(type(Student))
# # print(serial_file_handler_for_students.edit("2018/124", Student("2017/756", "Bojan", "Tomovic", "1.1.2001", [])).ime)

# print(serial_file_handler_for_students.delete_one("2018/124"))
# # for student in serial_file_handler_for_students.get_all():
# #     print(student.ime)

# # borko = Student("2018/999", "Borko", "Radivojevic", "1.1.2001", [])
# # zorica = Student("2018/998", "Zorica", "Brunclik", "1.1.2001", [])
# saban = Student("2018/997", "Saban Saulic", [], [])
# kemis = Student("2018/996", "Kemis Markovic", [], [])
# riki = Student("2018/995", "Riki Martin", [], [])

# umjesto_sabana = Student("2018/991", "Sinan Sakic", [], [npmat, npmreze, npoop,npstp])


# student_values = []
# # student_values.append(saban)
# # student_values.append(zorica)
# student_values.append(kemis)
# student_values.append(riki)


# print((serial_file_handler_for_students.insert_many(student_values)))
# print(serial_file_handler_for_students.edit("2018/789", umjesto_sabana ))

print("/n/n/nNovi STUDENTI----------------------")
for student in serial_file_handler_for_students.get_all():
    print(student.ime_prezime)

