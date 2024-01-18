def new_tax_calculation(amount):
    if amount <= 250000:  # 1 rupee to 2 Lakh 50 thousand rupees
        tax = 0
    elif amount <= 500000:  # 2 Lakh 50 thousand rupees to 5 Lakh rupees
        tax = (amount - 250000) * 0.05
    elif amount <= 750000:  # 5 Lakh rupees to 7 lakh 50 thousand rupees
        tax = (amount - 500000) * 0.10 + 12500
    elif amount <= 1000000:  # 7 lakh 50 thousand rupees to 10 Lakh rupees
        tax = (amount - 750000) * 0.15 + 37500
    elif amount <= 1250000:  # 10 Lakh rupees to 12 lakh 50 thousand rupees
        tax = (amount - 1000000) * 0.20 + 75000
    elif amount <= 1500000:  # 12 lakh 50 thousand rupees to 15 lakh rupees
        tax = (amount - 1250000) * 0.25 + 125000
    else:  # Above 15 lakh rupees
        tax = (amount - 1500000) * 0.30 + 187500
    return tax


def old_tax_calculation(amount, age):
    if age > 80:  # super senior citizens
        if amount <= 500000:  # 1 rupee to 5 Lakh rupees
            tax = 0
        elif amount <= 750000:  # 5 Lakh rupees to 7 lakh 50 thousand rupees
            tax = (amount - 500000) * 0.20 + 12500
        elif amount <= 1000000:  # 7 lakh 50 thousand rupees to 10 Lakh rupees
            tax = (amount - 750000) * 0.20 + 62500
        elif amount <= 1250000:  # 10 Lakh rupees to 12 lakh 50 thousand rupees
            tax = (amount - 1000000) * 0.30 + 112500
        elif amount <= 1500000:  # 12 lakh 50 thousand rupees to 15 lakh rupees
            tax = (amount - 1250000) * 0.30 + 187500
        else:  # Above 15 lakh rupees
            tax = (amount - 1500000) * 0.30 + 262500
    elif age > 60:  # senior citizens
        if amount <= 300000:  # 1 rupee to 3 Lakh rupees
            tax = 0
        elif amount <= 500000:  # 3 Lakh rupees to 5 Lakh rupees
            tax = (amount - 300000) * 0.05
        elif amount <= 750000:  # 5 Lakh rupees to 7 lakh 50 thousand rupees
            tax = (amount - 500000) * 0.20 + 12500
        elif amount <= 1000000:  # 7 lakh 50 thousand rupees to 10 Lakh rupees
            tax = (amount - 750000) * 0.20 + 62500
        elif amount <= 1250000:  # 10 Lakh rupees to 12 lakh 50 thousand rupees
            tax = (amount - 1000000) * 0.30 + 112500
        elif amount <= 1500000:  # 12 lakh 50 thousand rupees to 15 lakh rupees
            tax = (amount - 1250000) * 0.30 + 187500
        else:  # Above 15 lakh rupees
            tax = (amount - 1500000) * 0.30 + 262500
    else:  # Aged between 1 to 60
        if amount <= 250000:  # 1 rupee to 2 Lakh 50 thousand rupees
            tax = 0
        elif amount <= 500000:  # 2 Lakh 50 thousand rupees to 5 Lakh rupees
            tax = (amount - 250000) * 0.05
        elif amount <= 750000:  # 5 Lakh rupees to 7 lakh 50 thousand rupees
            tax = (amount - 500000) * 0.20 + 12500
        elif amount <= 1000000:  # 7 lakh 50 thousand rupees to 10 Lakh rupees
            tax = (amount - 750000) * 0.20 + 62500
        elif amount <= 1250000:  # 10 Lakh rupees to 12 lakh 50 thousand rupees
            tax = (amount - 1000000) * 0.30 + 112500
        elif amount <= 1500000:  # 12 lakh 50 thousand rupees to 15 lakh rupees
            tax = (amount - 1250000) * 0.30 + 187500
        else:  # Above 15 lakh rupees
            tax = (amount - 1500000) * 0.30 + 262500
    return tax
