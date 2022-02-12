class Card:
    def __init__(self, number, holder, valid_date, ccv):
        self.number = number
        self.holder = holder
        self.valid_date = valid_date
        self.ccv = ccv

    def get_hidden_number(self):
        return '{}** **** **** {}'.format(self.number[0:2],
                                          self.number[-4:])

    def __str__(self):
        return "Карта {}".format(self.get_hidden_number())


class Visa(Card):
    def __str__(self):
        return '[visa {}]'.format(self.get_hidden_number())


class MasterCard(Card):
    def __str__(self):
        return '[mastercard {}]'.format(self.get_hidden_number())


testcard = Visa('4200000000001234', 'holder name',
                '12/24', '111')
testcard2 = MasterCard('4500000000001564', 'holder name',
                       '11/24', '333')
# Visa(str(input('card number: ')),str(input('holder name:')),str(input('valid date: ')),str(input('ccv: ')))
print(testcard)
print(testcard2)