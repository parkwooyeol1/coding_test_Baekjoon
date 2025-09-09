class calculator: 
    def __init__(self,a,k=None):
        self.k = list()
        self.a = a
    def add(self,a):
        self.a += a 
        return self.a 
    def sub(self,a):
        self.a  -= a
        return self.a 
    def mul(self,a):
        self.a  *= a
        return self.a 
    def div(self,a):
        self.a  /= float(a)
        return self.a 
    def CalMenu (self):
        print("======우열이의 계산기========")
        print("1. + 2. - 3. * 4. /")
        print()
        print()
        print("========================")
        
        a = input("계산 선택: ")
        if a == "exit" :
            print("종료됐습니다.")
            return False

        b = input("숫자입력(결과 빈 값 입력): ")
        b = int(b)
        self.k.append(b)
        self.a= b     

        while True:
            self.k.append(" + ")
            b = input("숫자입력(결과 빈 값 입력): ")
            self.k.append(b)
            if b == "":
                break

            b = int(b)

            if a == "1":
                cal1.add(b)
            elif a == "2":
                cal1.sub(b)
            elif a == "3":
                cal1.mul(b)
            else :
                cal1.div(b)
            
            
        return True
    def Result(self) :
        for i in self.k :
            print(i, end="")

cal1 = calculator(0)
while cal1.CalMenu() == True :
    print()
    print ("결과: ", end="")
    cal1.Result()
    print(f" = {cal1.a}")