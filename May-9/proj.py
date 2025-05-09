import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from scipy import stats
import os


# Base class for loading and cleaning data
class DataHandler:
    def __init__(self):
        self.df = None
        self.numerical_cols = []

    def load_data_from_user(self):
        # Ask user to input the path to a CSV file
        path = input(" Please enter the full path to your CSV file: ").strip()

        if not os.path.exists(path):
            print(" The file does not exist. Please check the path and try again.")
            return False

        try:
            self.df = pd.read_csv(path)
            print(" Data loaded successfully! Here's a preview:")
            print(self.df.head())
            return True
        except Exception as e:
            print(f" Failed to load file: {e}")
            return False

    def handle_missing(self):
        # Remove rows with missing data
        if self.df is None:
            print("No data loaded.")
            return

        before = self.df.shape[0]
        self.df.dropna(inplace=True)
        after = self.df.shape[0]
        print(f" Removed {before - after} rows with missing values.")


# Class for processing data: normalization and outlier detection

class DataProcessor(DataHandler):
    def normalize_data(self):
        # Identify numeric columns
        self.numerical_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()

        if not self.numerical_cols:
            print(" No numeric columns found to normalize.")
            return

        # Apply Z-score normalization
        scaler = StandardScaler()
        self.df[self.numerical_cols] = scaler.fit_transform(self.df[self.numerical_cols])
        print(" Numeric data normalized using Z-score standardization.")

    def detect_outliers(self):
        if not self.numerical_cols:
            print(" No numeric columns to check for outliers.")
            return

        #  Z-Score Method 
        z_scores = np.abs(stats.zscore(self.df[self.numerical_cols]))
        z_outliers = np.sum(z_scores > 3)
        print(f"Z-score method detected {z_outliers} outlier values.")

        # IQR Method 
        Q1 = self.df[self.numerical_cols].quantile(0.25)
        Q3 = self.df[self.numerical_cols].quantile(0.75)
        IQR = Q3 - Q1
        iqr_outliers = ((self.df[self.numerical_cols] < (Q1 - 1.5 * IQR)) |
                        (self.df[self.numerical_cols] > (Q3 + 1.5 * IQR)))
        print(f"IQR method detected {iqr_outliers.sum().sum()} outlier values.")

        # DBSCAN Method
        dbscan = DBSCAN(eps=0.5, min_samples=5)
        labels = dbscan.fit_predict(self.df[self.numerical_cols])
        noise_points = list(labels).count(-1)
        print(f"DBSCAN identified {noise_points} noise points (outliers).")


# Class for visualizing data

class DataPlotter:
    def __init__(self, df, numerical_cols):
        self.df = df
        self.numerical_cols = numerical_cols

    def plot_distributions(self):
        for col in self.numerical_cols:
            plt.figure(figsize=(6, 4))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.show()

    def plot_boxplots(self):
        for col in self.numerical_cols:
            plt.figure(figsize=(6, 4))
            sns.boxplot(x=self.df[col])
            plt.title(f'Boxplot of {col}')
            plt.tight_layout()
            plt.show()

    def plot_dbscan(self):
        if len(self.numerical_cols) < 2:
            print(" Need at least two numeric columns for DBSCAN clustering plot.")
            return

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
        plt.tight_layout()
        plt.show()


# Main execution logic

def main():
    print(" Welcome to the Beginner-Friendly Data Analysis Tool!")

    processor = DataProcessor()

    if not processor.load_data_from_user():
        return

    processor.handle_missing()
    processor.normalize_data()
    processor.detect_outliers()

    plotter = DataPlotter(processor.df, processor.numerical_cols)
    plotter.plot_distributions()
    plotter.plot_boxplots()
    plotter.plot_dbscan()

if __name__ == "__main__":
    main()

