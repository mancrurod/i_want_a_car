def describe_dataset(df):
    """
    Prints a summary of the given dataframe, including its shape, general information, 
    statistical description, and the number of null values per column.

    Parameters:
    df (pandas.DataFrame): The dataframe to describe.

    Returns:
    None
    """
    
    # Print the number of rows and columns in the dataframe
    print(f"This dataframe has {df.shape[0]} rows and {df.shape[1]} columns.")
    
    # Print general information about the dataframe
    print("General information about the dataset:")
    print(df.info())
    
    # Print statistical description of the dataframe
    print("\nDataset description:")
    print(df.describe())
    
    # Print the number of null values in each column
    print("\nNumber of null values per column:")
    print(df.isnull().sum())