
while True:
    user_input = input('Izaberi tabelu za unos (radnik/kupac/proizvodi/masine): ').lower()
    if user_input == 'radnik':
        import radnik

    elif user_input == 'kupac':
        import kupac

    elif user_input == 'proizvodi':
        import proizvodi

    elif user_input == 'masine':
        import masine

    else:
        break