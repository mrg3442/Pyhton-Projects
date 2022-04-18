


class Tax:
    
    def __init__(self, income):
        self.income = income
        self.__stateIncTax = .06
        self._fedIncTax  = .22

    #gets private state tax var
    def getStateIncTax(self):
        print(self.__stateIncTax)

    #modifies private state tax var
    def setStateIncTax(self, private):
        self.__stateIncTax = private


    def incomeAfter(self):
        fedTaxAmount = self.income *self._fedIncTax
        stateTaxAmount = self.income * self.__stateIncTax
        totalTax = fedTaxAmount + stateTaxAmount
        afterTax = self.income - totalTax
        print("Your after tax salary is: #{}".format(afterTax))


sal = Tax(100000)
sal.incomeAfter()
        


    
        
