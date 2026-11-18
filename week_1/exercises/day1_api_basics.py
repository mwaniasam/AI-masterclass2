import requests

url = 'https://api.restcountries.com/countries/v5?q=germany'

response = requests.get(
    url,
    headers={'Authorization': 'Bearer rc_live_1770886474de47878d28539216c4f8c2'}
)

if response.status_code == 200:
    data = response.json()
    country = data['data']['objects'][0]

    # 'names' contains common/official or a name dictionary/string
    names_data = country.get('names', {})
    if isinstance(names_data, dict):
        name = names_data.get('common') or names_data.get('name') or list(names_data.values())[0]
    elif isinstance(names_data, list):
        name = names_data[0]
    else:
        name = str(names_data)

    # 'capitals' is a list or dictionary
    capitals_data = country.get('capitals', [])
    if isinstance(capitals_data, list) and capitals_data:
        capital = capitals_data[0]
    elif isinstance(capitals_data, dict):
        capital = list(capitals_data.values())[0]
    else:
        capital = str(capitals_data)

    # 'population' is typically a numeric value or dictionary under economy
    population = country.get('population', 0)
    if isinstance(population, dict):
        population = population.get('total', 0)

    # 'currencies'
    currencies_data = country.get('currencies', {})
    if isinstance(currencies_data, dict):
        currency = list(currencies_data.keys())[0] if currencies_data else 'N/A'
    elif isinstance(currencies_data, list) and currencies_data:
        currency = currencies_data[0].get('code', currencies_data[0]) if isinstance(currencies_data[0], dict) else currencies_data[0]
    else:
        currency = str(currencies_data)

    print(f"Country: {name}")
    print(f"Capital city: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print(f"Request failed. Status code: {response.status_code}")