class Electronic:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def turn_on(self):
        print(f"{self.name}의 전원을 켭니다.")
    def status(self):
        print("기기 상태 확인")
    
class Computer(Electronic):
    def turn_on(self):
        print(f"컴퓨터 {self.name} 부팅중 ...")
    def run_program(self):
        print("프로그램을 실행합니다.")

class Smartphone(Electronic):
    def turn_on(self):
        print(f"스마트폰 {self.name}을 켭니다.")
    def launch_app(self):
        print("앱을 실행합니다.")

devices = [
    Computer("MacBook", 100),
    Smartphone("Galaxy", 80)
]

for d in devices:
    d.turn_on()
    d.status()

devices[0].run_program()
devices[1].launch_app()