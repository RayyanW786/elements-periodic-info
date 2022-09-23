def nine():
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
    print(groups)
    all_elements = []
    all_symbols = []
    for groups in ELEMENTS:
        print(1)
        for element in ELEMENTS[groups]:
            all_elements.append(element.split(",")[0].lower())
            all_symbols.append(element.split(",")[1].lower())
    if user_input in groups:
        print(2)
        GROUP = ELEMENTS.get(user_input, None)
        if GROUP == None:
            print("invalid group")
        else:
            mystr = f"Group: {user_input}\n\n"
            for x in GROUP:
                element = x.split(",")[0]
                symbol = x.split(",")[1]
                info = GROUP[x]
                mystr += f"Element: {element}\nSymbol: {symbol}\n{info}\n\n"
            print(mystr)

    elif user_input in all_elements:
        print(3)
        for x in ELEMENTS:
            for i in x:
                if user_input == i.split(",")[0].lower():
                    element = i.split(",")[0]
                    symbol = i.split(",")[1]
                    info = x[i]
                    print(f"Group: {i}\nElement: {element}\nSymbol: {symbol}\n{info}\n\n")

    elif user_input in all_symbols:
        print(4)
        for x in ELEMENTS:
            for i in ELEMENTS[x]:
                if user_input == i.split(",")[1].lower():
                    element = i.split(",")[0]
                    symbol = i.split(",")[1]
                    info = ELEMENTS[x][i]
                    print(f"Group: {i}\nElement: {element}\nSymbol: {symbol}\n{info}\n\n")
    else:
        print("not a valid element, symbol or group!")

nine()
