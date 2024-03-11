def describe_city(city, country='United Arab Emirates'):
    msg = f"{city.title()} is located in {country.title()}."
    print(msg)

describe_city('Dubai')
describe_city('reykjavik', 'iceland')
describe_city('Sharjah')