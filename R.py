class ROI():

    

    def CalcIncome(self):
        print("Please input the amount spent on the following:")

        for costs in ['Rental_income', 'laundry', 'storage', 'Misc']:
            while True:
                value = input(f'{costs.capitalize()}: $')
                try:
                    value = int(value)
                    setattr(self, costs, value)
                    break
                except ValueError:
                    print("Sorry, that is not a valid input. Please enter a number.")


        self.Income = self.Rental_income + self.laundry + self.storage + self.Misc

        print(f'Your total income per month is ${self.Income}.')


    def CalcExpenses(self):
        
        print("Please input the amount spent on the following:")

        for costs in ['tax', 'insurance', 'utilities', 'HOAfees', 'lawnsnow', 'vacancy', 'repairs', 'Capital_Expenditure', 'Property_Management', 'mortgage']:
            while True:
                value = input(f'{costs.title()}: $')
                try:
                    value = int(value)
                    setattr(self, costs, value)
                    break
                except ValueError:
                    print('Sorry, that is not a valid input. Please enter a number.')

        self.Expenses = self.tax + self.insurance + self.utilities + self.HOAfees + self.lawnsnow + self.vacancy + self.repairs + self.Capital_Expenditure + self.Property_Management + self.mortgage
        
        print(f'Your total expenses per month are ${self.Expenses}.')

    

    def CalcInvestment(self):
        print("Please input the amount spent on the following:")

        for costs in ['Down_Payment', 'closing_costs', 'rehab_budget', 'miscellaneous']:
            while True:
                value = input(f'{costs.title()}: $')
                try:
                    value = int(value)
                    setattr(self, costs, value)
                    break
                except ValueError:
                    print("Sorry, that is not a valid input. Please enter a number.")

        self.Investment = self.Down_Payment + self.closing_costs + self.rehab_budget + self.miscellaneous
        
        print(f'Your total investment is ${self.Investment}.')


    
    def run(self):
        
        while True:
            self.CalcIncome()
            self.CalcExpenses()
            self.CalcInvestment()

            self.Cashflow = self.Income - self.Expenses
            self.AnnualCF = self.Cashflow * 12
            self.ROI = (self.AnnualCF / self.Investment)*100

            print(f'Your cash flow per month is ${self.Cashflow}, and cash flow per year is ${self.AnnualCF}.')

            print(f'This makes your total Return on Investment {self.ROI}%.')
            break

            
calculation = ROI()
calculation.run()


    