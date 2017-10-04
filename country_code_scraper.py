import requests
import bs4

def iso_codes():
    #get website
    url = 'https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes'
    source_code = requests.get(url)
    #convert source code to Beautiful Soup
    plain_text = source_code.text
    soup = bs4.BeautifulSoup(plain_text, "html5lib")
    #get desired table
    second_table = soup.find_all('table')[1]

    #declare dict with colloquial names of countries
    countries = {}
    #     'aland': 'AX',
    #     'bolivia': 'BO',
    #     'antigua': 'AG',
    #     'barbuda': 'AG',
    #     'bonaire': 'BQ',
    #     'bosnia': 'BA',
    #     'herzegovina': 'BA',
    #     'bouvet': 'BV',
    #     'brunei': 'BN',
    # }

    with open("output.txt","w", encoding='utf-8') as text_file:
        #get row
        for row in second_table.find_all('tr'):
            #get the row’s first tabledata element
            for col in row.find_all('td', limit=1):
                #find countrycode in next sibling and store in a value
                countrycode = col.next_sibling.next_sibling.find('a').get('href')[-2:]
                #assign country name in td to key and countrycode to value
                for name in col.find('a'):
                    lname = name.lower()
                    countries[lname] = countrycode
        print(countries, file=text_file)


iso_codes()
