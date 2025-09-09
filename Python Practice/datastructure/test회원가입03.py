import json
class MemberManagement:
    def __init__(self):
        with open("C:/Users/parkw/OneDrive/바탕 화면/Python Practice/member.json", "r", encoding="utf-8") as file1:
            self.k = json.load(file1)
        #self.k = self.member
        with open("C:/Users/parkw/OneDrive/바탕 화면/Python Practice/deleted.json", "r", encoding="utf-8") as file2:
            self.i = json.load(file2)
        #self.i = self.deleted
    def menu(self):
        print("======= Menu =======")
        print(" 1. Register Member")
        print(" 2. View Members")
        print(" 3. Delete Member")
        print(" 4. Restore Member")
        print(" 5. Exit program")    
        print("====================")
        return input("select: ")
    
    def register(self) :
        Id = input("Please enter an ID:") # a
        while True: 
            if Id in self.k : 
                print("Id already exists.")
                Id = input("Please enter an ID:")
            else: 
                break
        password = input("Please enter a password :") # a
        name = input("Please Enter a name:") # a
        phoneNumber = input("Enter a phoneNumber :") #01012341234
        mail = input("please enter a E-mail :") #abc@ac.com

        self.k[Id] = {"name" : name, "password" : password,
                        "phoneNumber" : phoneNumber, "mail" : mail}
        print("Registration completed.")           
        #self.k[a] = {"name" : a, "password" : a,
                        #"phoneNumber" : 01012341234, "mail" : abc@ac.com}
        #self.k[b] = {"name" : b, "password" : c,
        #"phoneNumber" : 01011111111, "mail" : abc@ac.com}

        """
        self.k = {
            a : {
                "name" : a, 
                "password" : a,
                "phoneNumber" : 01012341234, 
                "mail" : abc@ac.com
            }
            ,
                b : {
                "name" : b, 
                "password" : c,
                "phoneNumber" : 01011111111, 
                "mail" : abc@ac.com
            }
        }
        """
    def view(self) :
        id_list = list(self.k.keys())
        if len(id_list) == 0:
            print("Empty")
            return 
        for i, n in enumerate(self.k.keys(), start = 1):
                print(f"{i}. {n} - {self.k[n]['name']}")
        a = input("select(View details): ")
        a = int(a)
        b = id_list[a-1]
        print (f"- Name: {self.k[b]['name']}")
        print (f"- E-mail adress: {self.k[b]['mail']}")
        print (f"- Phone number: {self.k[b]['phoneNumber']}")
        print (f"- Id(고유값): {b}")
        print (f"- Password: {self.k[b]['password']}")

    def delete(self):
        id_list = list(self.k.keys()) 
        for i, n in enumerate(self.k.keys(), start = 1):
                print(f"{i}. {n} - {self.k[n]['name']}")
        a = input("select: ")
        a = int(a)
        b = id_list[a-1]
        self.i[b] = self.k.pop(b)
        print(f"Member [{b}] deleted.")
    
    def recovery(self):
        id_list = list(self.i.keys())
        for i, n in enumerate(self.i.keys(), start = 1):
                print(f"{i}. {n} - {self.i[n]['name']}")
    
        a = input("select: ")
        a = int(a)
        b = id_list[a-1]
        self.k[b] = self.i.pop(b)
        print(f"Member [{b}] recovered.")

        
    def save(self):
        with open("C:/Users/parkw/OneDrive/바탕 화면/Python Practice/member.json", "w",encoding="utf-8") as file1:
            json.dump(self.k, file1, indent=4)
        with open("C:/Users/parkw/OneDrive/바탕 화면/Python Practice/deleted.json","w",encoding="utf-8") as file2:
            json.dump(self.i, file2, indent=4)

mm = MemberManagement()
while True: 
    k=  mm.menu()
    if k == "1":
        mm.register()
    if k == "2":
        mm.view()
    if k == "3":
        mm.delete()
    if k == "4":
        mm.recovery()
    if k == "5":
        mm.save()
        break 
