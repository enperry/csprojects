class PhoneNumber:
    def __init__(self, number):
        self.num = "".join([num for num in number if num.isnumeric()])
        self.number = self.parse()
        self.area_code = self.number[:3]

    def parse(self):
        if(len(self.num) not in [10, 11] or self.num[-7] in ["0", "1"] or self.num[-10] in ["0", "1"]):
            raise ValueError("Number Error")
        if(len(self.num) == 11 and self.num[0] == "1"):
            return self.num[1:]
        elif(len(self.num) == 10):
            return self.num
        else:
            raise ValueError("ERROR")
    
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"