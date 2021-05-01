import math
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--type', '-t')
parser.add_argument('--payment', '-pa')
parser.add_argument('--principal', '-pr')
parser.add_argument('--periods', '-pe')
parser.add_argument('--interest', '-i')

args = parser.parse_args()


def differentiated_payment(principal, periods, interest):
    total = 0
    for i in range(1, periods + 1):
        payment = math.ceil((principal / periods) + (interest / 1200) * (principal - (principal * (i - 1) / periods)))
        print(f'Month {i}: payment is {payment}')
        total += payment
    print(f'\nOverpayment: {round(total - principal)}')


def annuity_payment(interest, principal, periods, payment):
    nominal = interest / 1200
    if payment is None:
        payment = math.ceil(principal * ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1)))
        print(f'Your annuity payment: {payment}!\nOverpayment: {int(round(payment * periods - principal))}')
    if principal is None:
        principal = math.floor(payment / ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1)))
        print(f'Your loan principal: {principal}!\nOverpayment: {int(round(payment * periods - principal))}')
    if periods is None:
        months = math.ceil(math.log(payment / (payment - nominal * principal), 1 + nominal))
        if months > 12:
            print(f'It will take {months // 12} years {f"and {months % 12} months " if months % 12 != 0 else ""}to repay this loan!')
        else:
            print(f'It will take {months} months to repay this loan!')
        print('Overpayment:', int(round(months * payment - principal)))


if args.interest is None or len(sys.argv) != 5:
    print('Incorrect parameters!')
else:
    if args.type == 'diff':
        differentiated_payment(principal=float(args.principal), periods=int(args.periods), interest=float(args.interest))
    if args.type == 'annuity':
        annuity_payment(interest=float(args.interest),
                        principal=float(args.principal) if args.principal is not None else None,
                        periods=int(args.periods) if args.periods is not None else None,
                        payment=float(args.payment) if args.payment is not None else None)
