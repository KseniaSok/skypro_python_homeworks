class User:

    def __unit__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
       
    def sayFirstName(self):
        print("Имя: ", self.first_name)
    def sayLastName(self):
        print("Фамилия: ", self.last_name)
    def sayFullName(self):
         print("Имя Фамилия: ", self.first_name, self.last_name)