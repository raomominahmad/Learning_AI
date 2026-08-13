class Student:
    def __init__( self , name , house ):
        # if not name:
        #     raise ValueError("Missing name")
        # if house not in ["Gryffindor" , "Hufflepuff" , "Ravenclaw" , "Slytherin"]:
        #   raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):  # same as .toString() Java Method
        return f"{self.name}  from  {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("HOuse: ")
        return cls(name, house)

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self,name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name
    #
    # # Getter
    # @property
    # def house (self):
    #     return self._house
    #
    # # Setter
    # @house.setter
    # def house (self,house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house


    # def charm ( self ):
    #     match  self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"

    # def get_student():
    #     name = input("Name: ")
    #     house = input("House: ")
    #     return Student(name, house)

def main():
    student = Student.get()
    #student.house = "Number Four, Privet Drive"
    print(student)
    # if student["name"] == "Padma":
    #     student['house'] = "RavenClaw"
    #print("Execpto Patronum! ")
    #print(student.charm())



        # try:
        #    return Student(name,house)
        # except Value:
        #     ...
        # student = Student()
        # student.name = input("Name: ")
        # student.house = input("House: ")

        # name = input("Name: ")
        # house = input("House: ")
        # return { "name":name , "house":house}
        # name = input("Name: ")
        # house = input("House: ")
        # return [name , house] # an immutabe list --> tuple


if __name__ == "__main__":
    main()