import requests
from bs4 import BeautifulSoup
import csv
import os
import time

def scrape_autoscout24(pages=20):
    """
    Scrapes car listings from the AutoScout24 website and saves the data to a CSV file.
    Args:
        pages (int): The number of pages to scrape. Default is 20.
    Returns:
        list: A list of dictionaries, each containing details of a car listing.
    The function performs the following steps:
    1. Iterates through the specified number of pages on the AutoScout24 website.
    2. Extracts car details such as brand, model, model type, price, mileage, transmission type, year, fuel type, and power.
    3. Saves the extracted data to a CSV file in the 'data' directory.
    4. Prints the status code of each HTTP request and the path to the saved CSV file.
    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
        AttributeError: If the expected HTML structure is not found.
    """
    list_cars = []  # Initialize an empty list to store car details
    for i in range(1, pages + 1):  # Iterate through the specified number of pages
        url_param = f"https://www.autoscout24.es/lst?atype=C&cy=E&desc=0&page={i}&search_id=2aqr9pevh6&sort=standard&source=listpage_pagination&ustate=N%2CU"
        html = requests.get(url_param)  # Send an HTTP GET request to the URL
        print(f"Status: {html.status_code}.")  # Print the status code of the HTTP request

        soup = BeautifulSoup(html.content, "html.parser")  # Parse the HTML content using BeautifulSoup
        items = soup.find_all('div', {'class': 'ListItem_wrapper__TxHWu'})  # Find all car listing items
        for item in items:  # Iterate through each car listing item
            brand = item.find('a', {'class': 'ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I'}).span.text  # Extract the car brand
            model = item.find('a', {'class': 'ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I'}).find('h2').find_all('span')[1].text  # Extract the car model
            model_type = item.find('span', {'class': 'ListItem_version__5EWfi'}).text  # Extract the car model type
            fuel = item.find('span', {'data-testid': 'VehicleDetails-gas_pump'}).text  # Extract the fuel type
            power = item.find('span', {'data-testid': 'VehicleDetails-speedometer'}).text  # Extract the power
            year = item.find('span', {'data-testid': 'VehicleDetails-calendar'}).text  # Extract the year
            manual_automatic = item.find('span', {'data-testid': 'VehicleDetails-transmission'}).text  # Extract the transmission type
            mileage = item.find('span', {'data-testid': 'VehicleDetails-mileage_road'}).text.replace(' km', '').replace('.', '')  # Extract and clean the mileage
            price_euros = item.find('p', {'class': 'Price_price__APlgs PriceAndSeals_current_price__ykUpx'}).text.replace(',-', '').replace('€ ', '').replace('.', '')  # Extract and clean the price
            
            list_cars.append({'brand': brand, 'model': model, 'model_type': model_type, 'price_euros': price_euros, 'mileage': mileage, 'manual_automatic': manual_automatic, 'year': year, 'fuel': fuel, 'power': power})  # Append the car details to the list
        
        time.sleep(2)  # Add a delay of 2 seconds between requests
    
    # Save to CSV
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')  # Define the data folder path
    os.makedirs(data_folder, exist_ok=True)  # Create the data folder if it doesn't exist
    csv_file = os.path.join(data_folder, 'scraped_data.csv')  # Define the CSV file path
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:  # Open the CSV file for writing
        writer = csv.DictWriter(file, fieldnames=list_cars[0].keys())  # Create a CSV DictWriter object
        writer.writeheader()  # Write the header row
        writer.writerows(list_cars)  # Write the car details to the CSV file
    
    print(f"Data saved to {csv_file}")  # Print the path to the saved CSV file

    return list_cars  # Return the list of car details