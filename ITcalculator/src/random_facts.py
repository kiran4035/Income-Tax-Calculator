from random import choice


def random_fact():
    facts = [
        "India’s GST (Goods and Services Tax) was first implemented on 1st July 2017. The GST model is made concerning the Canadian Model, even though GST was first implemented in France.",
        "GST was implemented through the 101st Constitution Amendment Act, 2016.",
        "Amitabh Bachchan was made the brand ambassador of GST in India.",
        "For those who do not pay GST, there is a provision of imprisonment for five years.",
        "GST is an indirect tax, which replaced other indirect taxes in India, such as VAT and CST.",
        "Although India’s population stands at about 130 crore people, the number of people that pay taxes are deficient. Only 1.46 crore people in India pay income tax.",
        "In India, around one crore people disclose their taxable income between 5 to 10 lakh per annum, while the remaining disclose their income above the 10 lakh bracket.",
        "For the Financial year 2020, the Budget had exempted individual taxpayers with income up to 5 lakh.",
        "Only 8, 600 taxpayers (individuals) have disclosed that they can pay income tax for an annual income of 5 crores. These individuals come from the professions of doctors, lawyers, chartered accountants, etc.",
        "Although the income tax brackets may look like it favours the rich, it does not ring true. The 'rich', or those who have incomes between 69 lakhs to 1.8 crores in India, contribute to three-fifths of the Indian Tax collections, and that’s just for individual income tax. In other words, these taxpayers pay roughly a third of tax collections in the country.",
        "The 'rich' taxpayers are known to constitute only an equivalent to 0.01% of the country’s population.",
        "Despite people fussing over income tax return and India’s tax rates, the country seems to have lower tax collections than those of similar size.",
        "Compared to tax collections in other Asian countries as per the country’s GDP, India’s performance is not that bad. India’s tax collections as per the country’s GDP are comparable to Asian countries, Egypt, and the Philippines.",
        "Although only a percentage of adults pay income tax in India, India’s tax collections are still at par with other Asian countries. In other words, if more Indians would pay income tax, India’s tax collections would rise and outdo other countries in the continent.",
        "There was a startling discovery in a report by the Comptroller and Auditor General of India audit in 2017. The percentage of those who do not file for income tax has doubled between 2013 and 2017. The reasons were cited as poor administration.",
        "The credit rating of countries appears to be biased. China’s credit rating has increased from A+ to AA- (December 2010) and has decreased to another variant of A, despite its decelerated growth. However, India’s credit rating has been the same for years, despite the GDP going up and down. Even today, India’s credit rating stays at BBB.",
        "Although most Indian citizens who pay taxes, around 95%, show that their income is up to 2.5 lakh per annum. The remaining 5% collectively pays about 89,000 crore income tax.",
        "As of 2001, the corporate taxes and income taxes collected from individuals were at a level, and there was hardly a difference. In FY2001, the corporate sector paid 35,696 INR crore taxes while individuals paid around 31,674 INR crore in taxes. However, over the next few years, India’s corporate tax would continue to grow faster, while individual taxes kept getting lower. The ratios kept falling, 58-42 in FY2019.",
        "As per the data, about 25% don’t file returns. Data shows that such assessments show that the income is deducted at the source. In other words, it means that about 8.45 crore assess their income. However, out of that number 6.33 do not pay taxes in the end.",
        "Out of all the taxes that are to be paid and assessed, half of the people have zero tax liability.",
        "In AY 2018-19, an anomaly in tax collections was detected. As per the data, 10.02 lakh crore taxes were collected. However, as per the IT department, only 8.07 Lakh crore taxes had been collected. Meanwhile, there is no real explanation for the extra two lakh crore.",
        "An interesting nugget, about 15% of PAN card holders file for tax returns.",
        "In India, three states constitute about 60% of the tax collections when it comes to income taxes. Delhi, Karnataka, and Maharashtra’s tax collections weigh 60% of the total tax collected in India.",
        "In 2011, a survey had collected data and found that around 27 million households in the country were rented out. However, as per the individuals' tax returns, only 4 million people claim that they receive incomes from house properties, bringing about one-six of the rental market.",
        "As per data, only three Indians pay more than 100 crore taxes per year. Furthermore, 85% of Indian taxpayers pay less than 1.5 lakh as their income tax per annum.",
        "Between the period 2008-09 and 2014-15, five states have shown significant growth: Kerala, Sikkim, Mizoram, Nagaland, and Madhya Pradesh. These states have shown the best instances of growth in terms of growth in income tax collections."
    ]  # List of facts

    display_fact = choice(facts)  # selecting a random fact to display
    return display_fact
