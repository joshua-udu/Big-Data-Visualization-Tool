import plotly.express as px
import plotly.graph_objects as go
import os

def plot_clusters(df):
    x_column = os.getenv('X_COLUMN')
    y_column = os.getenv('Y_COLUMN')
    color_column = os.getenv('COLOR_COLUMN')
    plot_title = os.getenv('PLOT_TITLE')
    
    fig = px.scatter(df, 
                     x=x_column, 
                     y=y_column, 
                     color=color_column, 
                     title=plot_title)
    fig.show()

def plot_heatmap(df):
    segment_counts = df['Segment'].value_counts().sort_index()
    fig = go.Figure(data=go.Heatmap(
        z=[segment_counts.values],
        x=[f'Segment {i}' for i in segment_counts.index],
        y=['Count'],
        colorscale='Viridis'))
    fig.show()

def plot_demographics(df):
    fig = px.pie(df, names='Segment', title='Customer Segment Distribution')
    fig.show()
