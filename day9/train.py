from random import randint

class train:
    def __init__(self, n):
        self.trainNum = n
    def book(self, trainNo, fr, to):
        print(f"your train {self.trainNum} is booked from {fr} to {to} with train number {trainNo}")
    def getstatus(self, trainNo, fr, to):
        print(f"your train {self.trainNum} is running from {fr} to {to} with train number {trainNo}")
    def calcFair(self, trainNo, fr, to):
        print(f"your train {self.trainNum} is running from {fr} to {to} with train number {trainNo}")
        print("the fair is : ",randint(100, 1000))


shatabdi = train(1201)
shatabdi.book(1201, "delhi", "lucknow")
