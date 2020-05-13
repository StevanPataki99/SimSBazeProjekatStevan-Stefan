from student import Student
from data_handler import DataHandler
import json
import pickle


class SequentialFileHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        self.filepath = filepath
        self.meta_filepath = meta_filepath
        self.data = []
        self.metadata = {}
        self.load_data()
        self.sort_data()
    
    #radi
    def load_data(self):
        #učitavanje podataka
        try:
            with open((self.filepath), 'rb') as dfile:
                self.data = pickle.load(dfile) #koristimo pickle za deserijalizaciju podataka
        except FileNotFoundError:
            print("Ne postoji File")
        #učitavanje metapodataka   
        with open(self.meta_filepath) as meta_file:
            self.metadata = json.load(meta_file) 
    #radi
    def sort_data(self):
        # for student in self.data:
        #     indeks = getattr(student, self.metadata['key'])
        #     cutted_index = indeks.split("/")[0]
        #     student.broj_indeksa = cutted_index
        sorted_list = sorted(self.data, reverse=False)
        self.data = sorted_list
    
    #radi
    def save_to_file(self):
        self.sort_data()
        with open(self.filepath, "wb") as sfile:
            pickle.dump(self.data, sfile)  

    #radi
    def insert(self, obj):
        self.data.append(obj)
        self.save_to_file()
    #radi
    def insert_many(self, new_values):
        for value in new_values:
            self.data.append(value)
        self.save_to_file()
    #radi
    def __len__(self):
        print(len(self.data))
        return len(self.data)
 
    #radi
    def get_one(self, id):
        for d in self.data: #za serijsku datoteku moramo proći linearno kroz sve slogove kada tražimo
            if getattr(d, (self.metadata["key"])) == id: #ako se poklopi ključna kolona, koju dobavljamo iz metapodataka sa zadatim podatkom
                return d
        return None


    #radi
    def get_all(self):
        return self.data    
            
    #radi      
    def edit(self, id, new_value):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                index_elementa = self.data.index(d)
                self.data[index_elementa] = new_value
        self.save_to_file()

    #radi
    def delete_one(self, id):
            for d in self.data:
                print(str(self.data))
                if getattr(d, (self.metadata["key"])) == id:
                    index_elementa = self.data.index(d)
                    del self.data[index_elementa]
                    print(str(self.data))
                    self.save_to_file()
                    return "Objekat je obrisan!"
            return("Objekat nije obrisan!")

    #radi
    def print_data(self):
        for s in self.data:
            print(s)







































