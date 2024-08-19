import argparse
import pandas as pd
from data_processing import load_data, preprocess_data
from segmentation import segment_customers
from visualize import plot_clusters, plot_heatmap, plot_demographics
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # Load environment variables from .env file
    
    parser = argparse.ArgumentParser(description='Customer Segmentation Analysis')
    parser.add_argument('--file', type=str, required=True, help='Path to the input CSV file')
    parser.add_argument('--clusters', type=int, default=5, help='Number of clusters for KMeans')
    args = parser.parse_args()
    
    df = load_data(args.file)
    df = preprocess_data(df)
    
    # Segment customers
    df = segment_customers(df, args.clusters)
    
    # Plot visualizations
    plot_clusters(df)
    plot_heatmap(df)
    plot_demographics(df)

if __name__ == '__main__':
    main()
