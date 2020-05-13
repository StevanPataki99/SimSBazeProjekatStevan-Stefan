from student import Student
from sequential_file_handler import SequentialFileHandler

studentSeq = SequentialFileHandler("student_data", "simsProjekatStevfan/student_metadata.json")

studentSeq.sort_data()


# s2 = Student("2018/888", "Kemis", [], [])
s1 = Student("2018/222", "Jessica", [], [])

# studentSeq.insert_many([s1,s2])
# studentSeq.insert(s2)

# studentSeq.delete_one("2018/888")
studentSeq.edit("2018/222",s1)
studentSeq.print_data()
# x = "2018/271328"

# print(x.split("/")[1])



