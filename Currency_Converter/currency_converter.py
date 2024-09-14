
# Currency Converter

currency_forms = ['USD', 'EURO', 'CAD']
rates = {
    'USD': {'EURO': 0.85, 'CAD': 1.25},
    'EURO': {'USD': 1.18, 'CAD': 1.47},
    'CAD': {'EURO': 0.80, 'USD': 0.68},
}


def get_amount():
    while True:
        amount = input('Enter the amount: ')

        if not (amount.isdigit() and int(amount) > 0):
            print('Invalid Amount!')
            continue

        return amount


def get_currency(caption: str):
    while True:
        currency = input(f'{caption} currency (USD/EURO/CAD): ').upper()
        if currency not in currency_forms:
            print('Invalid Currency')
            continue

        return currency


def convert_amount(amount: int, source_currency, target_currency):
    if source_currency == target_currency:
        return amount

    total = amount * rates[source_currency][target_currency]
    return total


def main():
    amount = int(get_amount())
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    total_amount = convert_amount(amount, source_currency, target_currency)

    print(f'{amount:.2f} {source_currency} is equal to {
        total_amount:.2f} {target_currency}')


# run the main program
main()
