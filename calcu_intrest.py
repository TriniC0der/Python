balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 1

def calculate(months, monthlyPaymentRate, balance):
    total_paid = 0.0
    while months != 13:
        previous_balance = balance
        monthly_interest_rate = annualInterestRate / 12.0
        minimum_monthly_payment = (monthlyPaymentRate * previous_balance)
        monthly_unpaid_balance = previous_balance - minimum_monthly_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        total_paid += minimum_monthly_payment


        output(months,minimum_monthly_payment,balance)
        if months == 12:
            print('Total paid: {:.2f}'.format(total_paid))
            print('Remaining balance: {:.2f}'.format(balance))
        months += 1


def output(months, monthlyPaymentRate, balance):
    print('Month: %d' % months)
    print('Minimum monthly payment: {:.2f}'.format(monthlyPaymentRate))
    print('Remaining balance: {:.2f}'.format(balance))

calculate(months,monthlyPaymentRate,balance)
