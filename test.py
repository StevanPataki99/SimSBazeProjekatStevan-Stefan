from data_classes.databse_file_handlers.smartphone import SmartPhone
from data_classes.databse_file_handlers.data_classes.student import Student
from data_classes.databse_file_handlers.data_classes.institution import Institution
from random import randint
import pickle




# with open("bin/"+file_name, 'wb') as data_file:
#     # koristimo pickle da bismo serijalizovali u binarnu datoteku
#     pickle.dump(data, data_file)

institution_data = [
    {"institution_signature":"FTN",
     "name":"Fakultet Tehnickih Nauka",
     "adresa":"Neka adresa 123"
    },
    {"institution_signature":"PMF",
     "name":"Prirodno-matematicki Fakultet",
     "adresa":"Neka adresa 333"
    },
    {"institution_signature":"US",
     "name":"Univerzitet Singidunum",
     "adresa":"Neka Adresa 444"
    },
    {"institution_signature":"MFN",
     "name":"Medicinski Fakultet Novi Sad",
     "adresa":"Neka adresa 555"
    },
    {"institution_signature":"FPN",
     "name":"Fakultet Politickih Nauka",
     "adresa":"Neka adresa 555"
    }
]
student_data = [

    {"institution_signature":"US",
     "profession":"SII",
     "student_id":"2018000000",
     "surname":"Mitar",
     "parent_name":"Mitar",
     "name":"Mitar",
     "gender":"male",
     "address":"Marka Bulata 24",
     "phone_number":"0653456789",
     "id_number":"05061998123456",
     "birth_date":"1998-01-01"
    },
    {"institution_signature":"US",
     "profession":"SII",
     "student_id":"2018000001",
     "surname":"Marko",
     "parent_name":"Drazen",
     "name":"Markovic",
     "gender":"male",
     "address":"Marka Bulata 25",
     "phone_number":"0653456781",
     "id_number":"02061998123333",
     "birth_date":"1998-01-02"
    },
    {"institution_signature":"FTN",
     "profession":"Mehatronika",
     "student_id":"MH-78/2017",
     "surname":"Pavle",
     "parent_name":"Nikola",
     "name":"Mirkovic",
     "gender":"male",
     "address":"Železnicka 44",
     "phone_number":"0666789765",
     "id_number":"09051993123456",
     "birth_date":"1998-05-09"
    },
    {"institution_signature":"PMF",
     "profession":"Fizika",
     "student_id":"F67-50",
     "surname":"Stanovic",
     "parent_name":"Ivan",
     "name":"Ivana",
     "gender":"female",
     "address":"Krajisnicka 50",
     "phone_number":"0634567891",
     "id_number":"27011992456789",
     "birth_date":"1998-01-27"
    },
    {"institution_signature":"FPN",
     "profession":"Medjunarodna Politika",
     "student_id":"MP-1000",
     "surname":"Savo",
     "parent_name":"Milan",
     "name":"Mirković",
     "gender":"male",
     "address":"Mise Dimitrijevica 10",
     "phone_number":"0657890002",
     "id_number":"27071990444555",
     "birth_date":"1998-07-27"
    }
]
level_of_studies = [
    {
        "level_signature":"Bc",
        "name":"Bachelor Degree"
    },
    {
        "level_signature":"Msc",
        "name":"Master Degree"
    },
    {
        "level_signature":"Phd",
        "name":"Doctors Degree"
    }
]
subjects = [

    {"institution_signature":"FTN",
     "class_signature":"MATH",
     "name":"Mathematics 1",
     "espb":8
    },
    {"institution_signature":"US",
     "class_signature":"OOP2",
     "name":"Object Orientded Programming 2",
     "espb":8
    },
    {"institution_signature":"US",
     "class_signature":"DM",
     "name":"Discrete Mathematics",
     "espb":8
    },
    {"institution_signature":"PMF",
     "class_signature":"FM1",
     "name":"Flouid Mechanics 1",
     "espb":8
    },
    {"institution_signature":"FPN",
     "class_signature":"RL",
     "name":"Roman Law",
     "espb":8
    },

]

majors = [
    {"institution_signature":"US",
     "level_signature":"Bc",
     "major_signature":"SDE",
     "major_name":"Software and Data Engineering"
    },
    {"institution_signature":"US",
     "level_signature":"Bc",
     "major_signature":"HT",
     "major_name":"Hotelierism and Tourism"
    },
    {"institution_signature":"US",
     "level_signature":"Bc",
     "major_signature":"IT",
     "major_name":"Informational Technologies"
    },
    {"institution_signature":"US",
     "level_signature":"Bc",
     "major_signature":"EB",
     "major_name":"Business and Economy"
    },
    {"institution_signature":"FTN",
     "level_signature":"Bc",
     "major_signature":"SEIT",
     "major_name":"Software Engineering and Informational Tecnologies"
    },
    {"institution_signature":"FTN",
     "level_signature":"Bc",
     "major_signature":"MEH",
     "major_name":"Mechatronics"
    },
    {"institution_signature":"FPN",
     "level_signature":"Bc",
     "major_signature":"CL",
     "major_name":"Crime Law"
    }
]

session_flow_of_studies = [
    {
     "institution_signature":"US",
     "major_signature":"SDE",
     "student_id":"2018000000",
     "profession":"SII",
     "current_calendar_year":"2020",
     "year_of_studies":"2",
     "block":"F3",
     "entrance_position":"5",
     "date_of_enrolment":"2018-06-06",
     "date_of_verification":"2018-08-01",
     "espb_start":0,
     "espb_end":240
    },
    {
     "institution_signature":"US",
     "major_signature":"SDE",
     "student_id":"MH-78/2017",
     "profession":"Mehatronika",
     "current_calendar_year":"2020",
     "year_of_studies":"2",
     "block":"A1",
     "entrance_position":"10",
     "date_of_enrolment":"2018-06-06",
     "date_of_verification":"2018-08-01",
     "espb_start":0,
     "espb_end":240
    },{
     "institution_signature":"PMF",
     "major_signature":"FM1",
     "student_id":"F67-50",
     "profession":"Fizika",
     "current_calendar_year":"2020",
     "year_of_studies":"2",
     "block":"F3",
     "entrance_position":"5",
     "date_of_enrolment":"2018-06-06",
     "date_of_verification":"2018-08-01",
     "espb_start":0,
     "espb_end":240
    },{
     "institution_signature":"FPN",
     "major_signature":"MP",
     "student_id":"MP-1000",
     "profession":"Medjunarodna Politika",
     "current_calendar_year":"2020",
     "year_of_studies":"3",
     "block":"G3",
     "entrance_position":"80",
     "date_of_enrolment":"2018-06-06",
     "date_of_verification":"2018-08-01",
     "espb_start":0,
     "espb_end":240
    }
]

majors_group_plan = [{
    "institution_signature":"US",
    "major_signature":"SDE",
    "block":"F3",
    "position":"something",
    "institution_class":"b3",
    "class_signature":"DM"
}]

linked_data_paths = {"data_path": "bin/level_of_studies_data",
                     "metadata_path": "bin/level_of_studies_metadata.json", "database_type": "serial"}

file_name = "level_of_studies"
with open("data/"+file_name, 'wb') as data_file:
    # koristimo pickle da bismo serijalizovali u binarnu datoteku
    pickle.dump(linked_data_paths, data_file)





