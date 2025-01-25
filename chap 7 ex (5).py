def describe_city(city, country='japan'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('tokyo')
describe_city('reykjavik', 'iceland')
describe_city('kyoto')