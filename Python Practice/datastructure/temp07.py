import json
class test: 
    def __init__(self):
        with open("C:/Users/parkw/OneDrive/바탕 화면/Python Practice/a.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)
    def t(self):
        print(self.data)
test1 = test()
print(test1.t())
