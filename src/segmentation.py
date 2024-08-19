from sklearn.cluster import KMeans
import os

def segment_customers(df, n_clusters):
    # Get the columns for segmentation from the environment variables
    segmentation_columns = os.getenv('SEGMENTATION_COLUMNS').split(',')
    features = df[segmentation_columns]
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Segment'] = kmeans.fit_predict(features)
    return df
