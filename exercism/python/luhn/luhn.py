class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        digits = self.card_num.replace(" ", "")
        if(len(digits) < 2 or not digits.isdigit()):
            return False

        _sum = 0
        for i, digit in enumerate(reversed(digits)):
            d = int(digit)
            if(((i + 1) % 2) == 0):
                d = d * 2
                if(d > 9):
                    d = d - 9
            _sum = _sum + d
         
        return not _sum % 10