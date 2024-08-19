import pandas as pd
import os

def load_data(file_path):
    import chardet
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    return pd.read_csv(file_path, encoding=encoding)

def preprocess_data(df):
    date_column = os.getenv('DATE_COLUMN')
    quantity_column = os.getenv('QUANTITY_COLUMN')
    unitprice_column = os.getenv('UNITPRICE_COLUMN')
    groupby_column = os.getenv('GROUPBY_COLUMN')
    aggregations = os.getenv('AGGREGATIONS').split(',')
    rename_columns = os.getenv('RENAME_COLUMNS').split(',')
    
    # Convert date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Calculate total amount spent if needed
    if 'TotalSpent' not in df.columns:
        df['TotalSpent'] = df[quantity_column] * df[unitprice_column]
    
    # Prepare the aggregation dictionary
    agg_dict = {agg.split(':')[0]: agg.split(':')[1] for agg in aggregations}
    
    # Aggregate data
    agg_df = df.groupby(groupby_column).agg(agg_dict)
    
    # Rename columns
    rename_dict = {rename.split(':')[0]: rename.split(':')[1] for rename in rename_columns}
    agg_df = agg_df.rename(columns=rename_dict)
    
    return agg_df.reset_index()
