def add_purchase(consumptions, limit, name, price, category):
    current_total = sum_prices(consumptions)

    if limit > 0 and (current_total + price > limit):
        print(f'Operation denied! Limit: ${limit}, Current: ${current_total + price}\n')
        return

    consumptions.append({
        'Name': name.capitalize(),
        'Price': price,
        'Category': category.capitalize()
    })
    print("Purchase added successfully!\n")

def print_consumptions(consumptions):
    if consumptions:
        for dictionary in consumptions:
            for key, value in dictionary.items():
                print(f'{key}: {value}')
            print()
    else:
        print('There are no purchases made yet!\n')

def filter_by_category(consumptions):
    filter_category = input('Please enter a category to filter consumptions: ')
    print()
    categories = [dictionary['Category'] for dictionary in consumptions]

    if filter_category.capitalize() in categories:
        return list(filter(lambda d: d['Category'].lower() == filter_category.lower(), consumptions))
    else:
        return []

def sum_prices(consumptions):
    return sum([dictionary['Price'] for dictionary in consumptions])

def main():
    consumptions = []
    limit = 0

    while True:
        choice = int(input('Please enter a number:\n'
                           '1. Add new purchase\n'
                           '2. Print all consumptions\n'
                           '3. Filter by a category\n'
                           '4. Calculate money balance\n'
                           '5. Set a limit\n'
                           '6. Exit the program\n\n'))
        print()

        match choice:
            case 1:
                name = input('Please enter the name of the purchase: ')
                price = float(input('Please enter the price ($) of the purchase: '))
                category = input('Please enter the category of the purchase: ')
                print()
                add_purchase(consumptions, limit, name, price, category)
            case 2:
                print_consumptions(consumptions)
            case 3:
                filtered_consumptions = filter_by_category(consumptions)
                print_consumptions(filtered_consumptions)
            case 4:
                total_sum = sum_prices(consumptions)
                print(f"The price of all the purchases (${', $'.join(str(dictionary['Price']) for dictionary in consumptions)}) is: ${total_sum}\n")
            case 5:
                limit = float(input('Please enter a limit you want to set: '))
                print()
            case 6:
                print('Exiting the program...')
                break
            case _:
                print(f'\'{choice}\' is an unrecognisable value!\n')

if __name__ == '__main__':
    main()