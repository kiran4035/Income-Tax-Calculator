def surcharge(amount, tax):
    if amount <= 10000000:  # 50 Lakh to 1 crore rupees
        sur_charge = tax * 0.10
    elif amount <= 20000000:  # 1 crore rupees to 2 crore rupees
        sur_charge = tax * 0.15
    elif amount <= 50000000:  # 2 crore rupees to 5 crore rupees
        sur_charge = tax * 0.25
    else:  # Above 5 crore rupees
        sur_charge = tax * 0.37
    return sur_charge
