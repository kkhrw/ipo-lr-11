import requests
from bs4 import BeautifulSoup
import json

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
number = 0

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    countries = soup.find_all('div', class_='country')
    countries_data = []
    
    for country in countries:
        number += 1
        name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text.strip()
        print(f"{number}. Country: {name}; Capital: {capital}")
        
        country_info = {
            "id": number,
            "name": name,
            "capital": capital
        }
        countries_data.append(country_info)

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(countries_data, json_file, ensure_ascii=False, indent=2)
    
    table_rows = ''
    for country in countries_data:
        table_rows += f'''
        <tr>
            <td>{country['id']}</td>
            <td>{country['name']}</td>
            <td>{country['capital']}</td>
        </tr>
        '''
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countries Information</title>
</head>
<body style="background-color: #FAAFBA;">

    <h1>Countries and Their Capitals</h1>
    <table border="1" cellpadding="10" cellspacing="0" bgcolor ="#FFFFFF">
        <tr bgcolor="#FFE4C4">
            <th >№</th>
            <th >Country</th>
            <th ">Capital</th>
        </tr>
        {table_rows}
    </table>
    <br>
    <p>Source: <a href="https://www.scrapethissite.com/pages/simple/">https://www.scrapethissite.com/pages/simple/</a></p>
</body>
</html>'''
    
    with open('index.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
else:
    print(f"Ошибка при запросе: {response.status_code}")