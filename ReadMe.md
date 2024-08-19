## Customer Segmentation Visualiation Tool

### Overview

This tool performs customer segmentation analysis based on customer demographics and purchase history. It processes input data, segments customers using KMeans clustering, and generates visualizations to help understand customer segments.

### Setup

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a Virtual Environment**:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Download Sample Data**:
   Download a sample dataset that contains customer demographics and purchase history. Ensure the data is in CSV format.

5. **Create a .env File**:
   Create a `.env` file in the root directory with the following content:
   ```env
   # Plot settings
   X_COLUMN=TotalSpent
   Y_COLUMN=TotalQuantity
   COLOR_COLUMN=Segment
   PLOT_TITLE=Customer Segments by Total Spent and Quantity Purchased

   # Preprocessing settings
   DATE_COLUMN=InvoiceDate
   QUANTITY_COLUMN=Quantity
   UNITPRICE_COLUMN=UnitPrice
   GROUPBY_COLUMN=CustomerID
   AGGREGATIONS=Quantity:sum,TotalSpent:sum,InvoiceNo:nunique
   RENAME_COLUMNS=Quantity:TotalQuantity,InvoiceNo:UniqueInvoices
   TOTAL_SALES_COLUMN=TotalSpent

   # Segmentation settings
   SEGMENTATION_COLUMNS=TotalQuantity,TotalSpent,UniqueInvoices
   ```

### Configuration

- **.env File**:
  - **Plot settings**:
    - `X_COLUMN`: Column for x-axis in scatter plot.
    - `Y_COLUMN`: Column for y-axis in scatter plot.
    - `COLOR_COLUMN`: Column for color coding in scatter plot.
    - `PLOT_TITLE`: Title for the scatter plot.

  - **Preprocessing settings**:
    - `DATE_COLUMN`: Column name for the date of purchase.
    - `QUANTITY_COLUMN`: Column name for the quantity of items purchased.
    - `UNITPRICE_COLUMN`: Column name for the unit price of items.
    - `GROUPBY_COLUMN`: Column name to group data by (e.g., CustomerID).
    - `AGGREGATIONS`: Aggregation operations for grouping (e.g., Quantity:sum).
    - `RENAME_COLUMNS`: New names for the aggregated columns.
    - `TOTAL_SALES_COLUMN`: Column name for the total amount spent.

  - **Segmentation settings**:
    - `SEGMENTATION_COLUMNS`: Columns to be used for clustering.

### Usage

1. **Prepare the Data**:
   Ensure the CSV file with customer data is placed in the `data` directory or any desired directory.

2. **Run the Tool**:
   ```sh
   python src/main.py --file data/sample_data.csv --clusters 5
   ```

   - `--file`: Path to the input CSV file.
   - `--clusters`: Number of clusters for KMeans (default is 5).

3. **View the Output**:
   The tool will generate visualizations that will open in your default web browser:
   - **Scatter Plot**: Displays customer segments based on total spent and quantity purchased.
   - **Heatmap**: Shows the distribution of customers across segments.
   - **Pie Chart**: Illustrates the distribution of customer segments.

### Explanation of Functions

- **load_data(file_path)**:
  Loads the data from the specified CSV file. Detects the file encoding to ensure proper loading.

- **preprocess_data(df)**:
  Processes the data by converting date columns to datetime format, calculating total spent, and aggregating data by customer ID. Uses environment variables to customize column names and aggregation methods.

- **segment_customers(df, n_clusters)**:
  Segments customers using KMeans clustering. Uses columns specified in the environment variables for clustering.

- **plot_clusters(df)**:
  Generates a scatter plot using Plotly based on the specified columns in the environment variables.

- **plot_heatmap(df)**:
  Creates a heatmap to visualize the distribution of customers across segments.

- **plot_demographics(df)**:
  Creates a pie chart to show the distribution of customer segments.

### Example .env File

```env
# Plot settings
X_COLUMN=TotalSpent
Y_COLUMN=TotalQuantity
COLOR_COLUMN=Segment
PLOT_TITLE=Customer Segments by Total Spent and Quantity Purchased

# Preprocessing settings
DATE_COLUMN=InvoiceDate
QUANTITY_COLUMN=Quantity
UNITPRICE_COLUMN=UnitPrice
GROUPBY_COLUMN=CustomerID
AGGREGATIONS=Quantity:sum,TotalSpent:sum,InvoiceNo:nunique
RENAME_COLUMNS=Quantity:TotalQuantity,InvoiceNo:UniqueInvoices
TOTAL_SALES_COLUMN=TotalSpent

# Segmentation settings
SEGMENTATION_COLUMNS=TotalQuantity,TotalSpent,UniqueInvoices
```

### Troubleshooting

- **Data Loading Issues**: Ensure the CSV file is correctly formatted and the path is accurate.
- **Environment Variable Errors**: Verify that the `.env` file contains all required variables and that they are correctly spelled.
- **Visualization Issues**: Ensure that Plotly is installed and that the columns specified in the environment variables exist in the data.

### Conclusion

This tool provides a flexible framework for customer segmentation analysis, allowing users to customize data processing and visualization through environment variables. By following the instructions and configuring the `.env` file, users can adapt the tool to various datasets and requirements.
