import pandas as pd
from src.scraping import scrape_autoscout24
from src.transformation import transform_dataframe
from src.exploration import describe_dataset
from src.visualization import cars_per_brand, top_brands, avg_price_top5_brands, boxplot_price, manual_vs_automatic_distribution, fuel_type_distribution

def main():
    # Scrape data from autoscout24
    print("Scraping data from autoscout24...")
    cars_data = scrape_autoscout24(pages=20)
    if not cars_data:
        print("No cars data scraped. Exiting...")
        return
    
    print(f"Scraped {len(cars_data)} cars data entries.")
    
    # Create a DataFrame from the scraped data
    print("Creating DataFrame from scraped data...")
    df = pd.DataFrame(cars_data)
    print(f"DataFrame created with {df.shape[0]} rows and {df.shape[1]} columns.")

    # Describe the dataset
    print("Describing the raw dataset...")
    describe_dataset(df)
    
    # Transform the DataFrame
    print("Transforming the DataFrame...")
    df = transform_dataframe(df)
    print("DataFrame transformed.")
    print(f"Transformed DataFrame has {df.shape[0]} rows and {df.shape[1]} columns.")

    # Describe the transformed dataset
    print("Describing the transformed dataset...")
    describe_dataset(df)
    
    # Generate visualizations
    print("Generating visualizations...")
    cars_per_brand(df)
    print("Generated visualization: cars per brand.")
    top_brands(df)
    print("Generated visualization: top brands.")
    avg_price_top5_brands(df)
    print("Generated visualization: average price of top 5 brands.")
    boxplot_price(df)
    print("Generated visualization: boxplot of prices.")
    manual_vs_automatic_distribution(df)
    print("Generated visualization: manual vs automatic distribution.")
    fuel_type_distribution(df)
    print("Generated visualization: fuel type distribution.")

if __name__ == "__main__":
    main()
