def main():
    user_input = input("enter a element, its symbol or group").lower()
    ELEMENTS = {
        'alkali metals': {
            'Lithium,Li': 'Atomic weight: 6.94',
            'Sodium,Na': 'Atomic weight: 22.99',
            'Potassium,K': 'Atomic weight: 39.09',
            },
        'halogen ': {
            'Florine,F': 'Atomic weight: 18.99',
            'Chlorine,Cl': 'Atomic weight: 35.45',
            'Bromine,Br': 'Atomic weight: 79.9',
        }
    }
    groups = ELEMENTS.keys()
    all_elements = []
    all_symbols = []
    for groups in ELEMENTS:
        for element in ELEMENTS[groups]:
            _lst = element.split(",")
            all_elements.append(_lst[0].lower())
            all_symbols.append(_lst[1].lower())
    if user_input in groups:
        GROUP = ELEMENTS.get(user_input, None)
        if GROUP == None:
            print("invalid group")
        else:
            mystr = f"Group: {user_input}\n\n"
            for x in GROUP:
                _lst = x.split(",")
                element = _lst[0]
                symbol = _lst[1]
                info = GROUP[x]
                mystr += f"Element: {element}\nSymbol: {symbol}\n{info}\n\n"
            print(mystr)

    elif user_input in all_elements:
        for x in ELEMENTS:
            for i in ELEMENTS[x]:
                _lst = i.split(",")
                if user_input == _lst[0].lower():
                    element = _lst[0]
                    symbol = _lst[1]
                    info = ELEMENTS[x][i]
                    print(f"Group: {x}\nElement: {element}\nSymbol: {symbol}\n{info}\n\n")

    elif user_input in all_symbols:
        for x in ELEMENTS:
            for i in ELEMENTS[x]:
                _lst = i.split(",")
                if user_input == _lst[1].lower():
                    element = _lst[0]
                    symbol = _lst[1]
                    info = ELEMENTS[x][i]
                    print(f"Group: {x}\nElement: {element}\nSymbol: {symbol}\n{info}\n\n")
    else:
        print("not a valid element, symbol or group!")

if __name__ == "__main__":
    main()
