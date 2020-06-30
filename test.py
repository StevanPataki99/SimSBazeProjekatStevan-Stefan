from data_classes.databse_file_handlers.smartphone import SmartPhone
from data_classes.databse_file_handlers.data_classes.student import Student
from data_classes.databse_file_handlers.data_classes.institution import Institution
from random import randint
import pickle

# smart_phone1 = SmartPhone("Samsung", "A50", 500,
#                           "Taiwan", "Samsung INC", randint(1, 100000000), [])
# smart_phone2 = SmartPhone("Nokia", "3310", 130, "Finland",
#                           "Nokia INC", randint(1, 100000000), [])
# smart_phone3 = SmartPhone("Apple", "Iphone 7s", 500,
#                           "China", "Apple INC", randint(1, 100000000), [])
# smart_phone4 = SmartPhone("Apple", "Iphone X", 800,
#                           "China", "Apple INC", randint(1, 100000000), [])
# smart_phone5 = SmartPhone("Huawei", "P40 Pro", 700,
#                           "China", "Huawei INC", randint(1, 100000000), [])

linked_data_paths = {"data_path": "bin/smartphone_data",
                     "metadata_path": "bin/smartphone_metadata.json", "database_type": "serial"}

# institution_1 = Institution("ETS", "Mihajlo Pupin", "Futoski Put 18") 

# student_1 = Student("ETS", "Elektronicar", "20181001", "Markovic", "Mirko", "Marko", "M", "Mise Ruzica 5", "021747575", "111199900018", "11.11.1999")
# student_2 = Student("ETS", "Programer", "20181002", "Petrovic", "Petar", "Njegos", "M", "Jase Tomica 3", "021666999", "091099900011", "09.10.1999")
# student_3 = Student("ETS", "Elektronicar", "20181003", "Ivan", "Ilija", "Ivanovic", "M", "Narodni Front 15", "021888454", "101099900018", "10.10.1999")

# data = []
# # data.append(smart_phone1)
# # data.append(smart_phone2)
# # data.append(smart_phone3)
# # data.append(smart_phone4)
# # data.append(smart_phone5)
# # data.append(student_1)
# # data.append(student_2)
# # data.append(student_3)
# data.append(institution_1)


# # file_name = type(smart_phone1).__name__.lower()
file_name = "smartphone"

# for d in data:
#    print(str(d))

# with open("bin/"+file_name, 'wb') as data_file:
#     # koristimo pickle da bismo serijalizovali u binarnu datoteku
#     pickle.dump(data, data_file)

# print(file_name)
with open("data/"+file_name, 'wb') as data_file:
    # koristimo pickle da bismo serijalizovali u binarnu datoteku
    pickle.dump(linked_data_paths, data_file)


# res = None
# with open("bin/smartphone_data", "rb") as f:
#     res = pickle.load(f)

# print(res)
