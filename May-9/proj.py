import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from scipy import stats
import os

# --------------------------------------------
# Base class responsible for loading and cleaning data
# --------------------------------------------
class DataHandler:
    def __init__(self):
        self.df = None               # DataFrame to store loaded data
        self.numerical_cols = []     # List of numeric column names

    def load_data_from_user(self):
        # Prompt user to enter the CSV path
        path = input("📂 Enter the path to your CSV file: ").strip()

        # Check if file exists
        if not os.path.exists(path):
            print("❌ File not found. Please check the path and try again.")
            exit()

        # Try loading the file using pandas
        try:
            self.df = pd.read_csv(path)
            print("✅ Data loaded successfully!")
            print(self.df.head())  # Display first few rows
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            exit()

        return self.df

    def handle_missing(self):
        # Drop rows with missing values and report how many were dropped
        before = self.df.shape[0]
        self.df.dropna(inplace=True)
        after = self.df.shape[0]
        print(f"🧹 Removed {before - after} rows with missing values.")

# --------------------------------------------
# Derived class responsible for processing the data
# --------------------------------------------
class DataProcessor(DataHandler):
    def normalize_data(self):
        # Identify numerical columns for scaling
        self.numerical_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()

        if not self.numerical_cols:
            print("⚠️ No numerical columns found to normalize.")
            return

        # Apply Z-score normalization
        scaler = StandardScaler()
        self.df[self.numerical_cols] = scaler.fit_transform(self.df[self.numerical_cols])
        print("📊 Data normalized using Z-score.")

    def detect_outliers(self):
        if not self.numerical_cols:
            print("⚠️ No numerical columns for outlier detection.")
            return

        # --- Z-Score Method ---
        z_scores = np.abs(stats.zscore(self.df[self.numerical_cols]))
        outlier_mask = (z_scores > 3)
        print(f"🔍 Z-score outliers: {np.sum(outlier_mask)}")

        # --- IQR Method ---
        Q1 = self.df[self.numerical_cols].quantile(0.25)
        Q3 = self.df[self.numerical_cols].quantile(0.75)
        IQR = Q3 - Q1
        outlier_iqr = ((self.df[self.numerical_cols] < (Q1 - 1.5 * IQR)) |
                       (self.df[self.numerical_cols] > (Q3 + 1.5 * IQR)))
        print(f"📏 IQR outliers: {outlier_iqr.sum().sum()}")

        # --- DBSCAN Method ---
        dbscan = DBSCAN(eps=0.5, min_samples=5)
        labels = dbscan.fit_predict(self.df[self.numerical_cols])
        print(f"📌 DBSCAN noise points: {list(labels).count(-1)}")

# --------------------------------------------
# Class for plotting distributions and clusters
# --------------------------------------------
class DataPlotter:
    def __init__(self, df, numerical_cols):
        self.df = df
        self.numerical_cols = numerical_cols

    def plot_distributions(self):
        # Plot histogram and KDE for each numerical column
        for col in self.numerical_cols:
            plt.figure(figsize=(6, 4))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.show()

    def plot_boxplots(self):
        # Plot boxplots for each numerical column
        for col in self.numerical_cols:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=self.df[col])
            plt.title(f'Boxplot of {col}')
            plt.show()

    def plot_dbscan(self):
        # Plot DBSCAN clustering on first two numerical columns
        if len(self.numerical_cols) >= 2:
            dbscan = DBSCAN(eps=0.5, min_samples=5)
            labels = dbscan.fit_predict(self.df[self.numerical_cols])
            plt.figure(figsize=(6, 5))
            sns.scatterplot(
                x=self.df[self.numerical_cols[0]],
                y=self.df[self.numerical_cols[1]],
                hue=labels,
                palette="Set1"
            )
            plt.title("DBSCAN Clustering")
            plt.show()

# --------------------------------------------
# Main function to run the whole project
# --------------------------------------------
if __name__ == "__main__":
    print("🧠 OOP-Based Data Analysis Script")
    
    # Step 1: Create an object and load data from user input
    processor = DataProcessor()
    processor.load_data_from_user()
    
    # Step 2: Handle missing data
    processor.handle_missing()
    
    # Step 3: Normalize data
    processor.normalize_data()
    
    # Step 4: Detect outliers
    processor.detect_outliers()
    
    # Step 5: Visualize results
    plotter = DataPlotter(processor.df, processor.numerical_cols)
    plotter.plot_distributions()
    plotter.plot_boxplots()
    plotter.plot_dbscan()
