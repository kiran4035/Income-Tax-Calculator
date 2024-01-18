from tkinter import *


def faqs():
    # create root window
    root = Tk()

    # App Title
    root.title("FAQ's regarding Tax's")

    # Defining the size of the window
    root.geometry('1200x800')

    # create a vertical scrollbar-no need to write orient as it is by default vertical
    v = Scrollbar(root)

    # attach Scrollbar to root window on the side
    v.pack(side=RIGHT, fill=Y)

    # create a Text widget with 70 lines height here yscrollcommand is used to attach Text
    # widget to the vertical scrollbar
    t = Text(root, height=70, wrap=WORD, yscrollcommand=v.set)

    # insert some text into the text widget
    t.insert(END,
             '''
Income Tax: 
             
    Filing an income tax return is an annual ritual for millions of Indians. Income tax is a percentage of your income that you give the government to pay for expenditure on infrastructure, salaries of government employees and other expenditure incurred by the government. Any tax that is imposed by the government must be based on law. Tax is charged on income from the following heads: salaries, income from house properties, profits or gains from profession or business, capital gains and income from other sources (like income arising from investments including interest and dividends.)
    The Income Tax department is responsible for all activities related to the tax process. It is under the supervision of the Central Board of Direct Taxes (CBDT) which is in turn under the Ministry of Finance. The provisions governing income tax law are based on the Income Tax Act of 1961.
    
1.Who pays income tax?

    Every person or business entity that generates an income is legally obliged to pay tax. The definition of a person under the Income Tax Act includes both individuals as well as artificial entities. Those who need to pay tax include: individuals, Hindu Undivided Families (HUFs), Association of Persons (AOPs), Body of Individuals (BOIs), Firms, LLPs, Companies, local authorities and any other entity not covered by any of the categories above.

2.How is tax calculated?

    Income tax is based on your annual income earned from various sources including your salary (income in cash, kind or facilities provided by your employer), profits from business, gains from selling capital assets like property, rental income, and interest/dividend/commission income. There are various slabs of income tax rates based on earnings and the rates get progressively higher for taxpayers with higher incomes.

3.What is the period for which tax is calculated?

    Tax is charged on earnings during the period April 1- March 31. Any income earned during this period is assessed for income tax purposes. The year in which the income was earned is known as the ‘previous year’ and the year in which the tax is calculated, is known as the ‘assessment year’. So, income you have earned between 1st April, 2105 and 31st March 2016 is known as the previous year. The tax you have to pay on this income is calculated during the assessment year which is 1st April, 2016 – 31st March, 2017.

4.How does the government collect income tax?

    The government collects income tax in 3 ways:

        1. Voluntary payment by assesses and payment into designated banks. This includes Advance Tax and Self-Assessment Tax.
        2. Taxes Deducted at Source (TDS) which is deducted at the point of origin of your income even before you receive it.
        3. Taxes Collected at Source (TCS).
    
5.How to calculate tax liability?

    The most recent income tax rates are available in the Finance Act passed by Parliament every year. There has been no change in the existing income tax rate for the financial year 2016-2107. The easiest way to calculate your income tax according to your income is to use an online Income Tax Calculator tool. You could also approach professional sources for expert help.

6.Can I use an online Income Tax Calculator tool?

    Yes, it is easy to use an Income Tax Calculator to estimate your tax payment for the year. Doing your taxes can seem like a complex and daunting task that requires making time for physical visits to an accountant/ tax professional and dealing with cumbersome paperwork. Thanks to technology, however, it has never been easier to calculate your tax on your own, and in your own time. CreditMantri’s free Income Tax Calculator is a quick, simple and user-friendly way of estimating how much your income tax liability will be. The Income Tax Calculator will take you step by step through the tax process and enable you to estimate your tax obligation on your own.
    You can also use the online Income Tax Calculator tool offered by the income tax department of the Government of India. There are other income tax calculators that are available online but it is important that you refer to a reputable and reliable website to avoid the risk of inaccurate information.

7.What is TDS?

    Tax Deducted at Source (TDS) is a system whereby the tax due by you is deducted directly at the point of origin of income before it is disbursed to you. For example, if you are a salaried employee, your employer will calculate the amount of tax due on your earnings and deduct the amount (TDS) from your salary and pay it directly to the government on your behalf. Similarly, banks will calculate the tax due on your interest earnings and automatically deduct the amount from your account and remit it to the government. You can claim this tax paid on your behalf as a credit (like Advance Tax) while filing your income tax return.
    The TDS mechanism enables greater efficiency and speed in collection of taxes. The kinds of income covered by TDS include salary, interest earnings, brokerage, professional and commission fees, contracts and royalty payments.
    If you want to know the amount of tax that has been deducted, you can ask each payer to furnish you with a TDS certificate.

8.What are allowances and are they taxable?

    Allowances are fixed amounts that are paid by the employer, in addition to the salary, to meet certain requirements. These could include travel allowance, house rent allowance, uniform allowance among others. There are 3 kinds of allowance as per the Income Tax Act:

        1. Taxable allowances (where you have to pay taxes on the full allowance amount - e.g. Dearness Allowance (DA), Overtime Allowance, Entertainment Allowance etc.).
        2. Fully exempt allowances (the entire amount of the allowance is tax-free - e.g. allowances paid to government servants abroad or paid to judges).
        3. Partially exempt allowances (you need to pay taxes on a portion of the allowance – e.g. House Rent Allowance).
        
9.What is an income tax return?

    Your income tax return (known as return of income) is a prescribed form that is completed by you and communicates to the government the details of your income for the financial year and the taxes paid on the income. There are different forms for stating the return of income depending on the status and nature of the income.
    It is very important to stress that there should be no falsification or deliberate withholding of information on your income tax return.
    
10.What are the various kinds of income tax forms?

    ITR – 1 Also known as SAHAJ, it is applicable to an individual having salary or pension income or income from one house property or income from other sources ( not including lottery winnings or income from racehorses).

    ITR 2A It is applicable to Individuals and Hindu Undivided Family not having income from business or profession and capital gains and residents who do not hold foreign assets do not have foreign income.

    ITR - 2 It is applicable to an individual or a Hindu Undivided Family having income from any source other than "Profits and gains of business or profession".

    TR - 3 It is applicable to an individual or a Hindu Undivided Family who is a partner in a firm and where income chargeable to tax under the head "Profits or gains of business or profession" does not include any income except the income by way of any interest, salary, bonus, commission or remuneration, by whatever name called, due to, or received by him from such firm.

    ITR - 4S Also known as SUGAM, it is applicable to individuals and Hindu Undivided Family who have opted for the presumptive taxation scheme.

    ITR - 4 Is applicable to an individual or a Hindu Undivided Family in a proprietary business or profession.

    ITR - 5 This form can be used by a person being a firm, LLP, AOP, BOI, artificial juridical person , co-operative society and local authority.

    ITR - 6 It is applicable to a company, other than a company claiming exemption under section 11

    ITR - 7 It is applicable to persons including companies who are required to furnish return under section 139(4A, B, C) such as trusts, political parties, institutions, colleges, etc.

    ITR - V It is the acknowledgement of filing the return of income.

    You can download these income tax forms at incometaxindia.gov.in   
    
11.How to check income tax status?

    Your residential status is determined by how many days you have been resident in India during the financial year and for a pre-determined number of preceding years. There is no correlation between citizenship and residential status. For example, an Indian citizen may not be resident in India, while a citizen of a foreign country might be a resident of India. Ordinary Residents have the maximum tax liability, followed by Not-Ordinary Residents, and the least tax liability is enjoyed by Non-Residents. You can check income tax status at the income tax department’s website or consult a tax professional.  
 
12.What is e-filing?

    Filing your income tax return electronically online is known as e-filing. All individuals with an income above Rs 5 lakhs are required to file their return of income electronically with or without digital signature or with an electronic verification code. You need to have a net banking facility to use this method of filing. There is a separate portal for e-filing of return of income at www.incometaxindiaefiling.gov.in.

    Senior citizens above the age of 80, even with an income above Rs 5 lakhs, are exempt from mandatory e-filing. They have the option to submit their income tax returns either physically or online.

    Individuals with an income of less than Rs 5 lakh can submit their application by hard copy to the local office of the IT department.

    In addition to e filing, you can also pay your tax electronically through net banking facilities or using SBI credit or debit card. If you use an online Income Tax calculator, the entire process of computing the amount of tax you need to pay, filing the return, and making the payment can all be completed electronically at your convenience.

    It is mandatory for all companies to file their returns electronically with digital signature.

13.What is exempt income and taxable income?

    Certain kinds of income are not subject to taxation. This is known as exempt income. For example, shareholders of a company do not need to pay tax on their dividend income. However, dividend income from a foreign company is taxable. Income Tax Calculators will help you identify your taxable and exempt income.
    
''')

    # attach Text widget to root window at top
    t.pack(side=TOP, fill=X)

    # the root window handles the mouse click event
    root.mainloop()
