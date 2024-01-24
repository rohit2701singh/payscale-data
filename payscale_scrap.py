import requests
from bs4 import BeautifulSoup
import pandas

table_heading_name = []
row_data = []
for page_number in range(1, 34):
    URL = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_number}"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
    }

    response = requests.get(url=URL, headers=header)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    # print(soup)

    table_container = soup.find(name="div", class_="csr-gridpage__grid")
    # print(table_container)
    if page_number == 1:
        table_heading = table_container.find_all(name="th", class_="data-table__header")
        for item in table_heading:
            heading = item.getText()
            table_heading_name.append(heading)
        # print(table_heading_name)

    table_body = soup.find(name="tbody")
    table_rows = table_body.find_all(name="tr", class_="data-table__row")

    for row in table_rows:
        table_data = row.find_all(name="td", class_="data-table__cell")
        values = []
        for data in table_data:
            column_values = data.find(name="span", class_="data-table__value").getText()
            # print(column_values)
            values.append(column_values)
        row_data.append(values)
    page_number += 1

print(row_data)

df = pandas.DataFrame(row_data, columns=table_heading_name)
df.to_csv('data_file.csv', index=False)
