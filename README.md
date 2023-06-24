# Hotel Booking Data Analysis

This project is aimed at performing data analysis on a hotel booking dataset. The dataset contains information about hotel bookings, including various attributes such as guest information, booking details, hotel type, and more. The analysis is performed using Python and several libraries for data manipulation, visualization, and analysis.

## Prerequisites

To run this project, you need to have the following libraries installed:

- pandas: Used for data manipulation and extraction.
- numpy: Used for numerical computations.
- matplotlib: Used for creating visualizations such as plots and charts.
- seaborn: Used for statistical data visualization.
- plotly: Used for interactive and dynamic visualizations.
- sort_dataframeby_monthorweek: A custom library for sorting data by month or week.
- warnings: Used to ignore warning messages.

## Getting Started

1. Clone the repository to your local machine or download the code files.
2. Install the required libraries mentioned in the "Prerequisites" section.
3. Open the project in a Python IDE or Jupyter Notebook.

## Project Structure

The project contains the following files:

- `hotel_booking_analysis.py`: The main Python script that performs data cleaning, preprocessing, and analysis.
- `hotel_bookings.csv`: The dataset file in CSV format.

## Project Tasks

### Task 1: Data Cleaning and Data Pre-processing

- Read the hotel booking data from the CSV file.
- Perform data cleaning by filling null values with zero.
- Filter out incorrect entries with zero values for children, adults, and babies.

### Task 2: Guest Origins and Spatial Analysis

- Analyze where the guests come from (country) for both resort and city hotels.
- Visualize the guest origins using a pie chart and a choropleth map.

### Task 3: Variation of Hotel Prices Across Years

- Analyze the variation of hotel prices across different room types.
- Group the data by months and calculate the average daily rate (ADR) for both resort and city hotels.
- Plot a line chart to visualize the price trends.

### Task 4: Nights Spent, Market Segments, and Guest Preferences

- Analyze the distribution of nights spent at hotels by market segment and hotel type.
- Analyze guest preferences for meal types using a donut chart.
- Analyze special requests made by customers and their relationship with booking cancellation.

### Task 5: Busiest Month Analysis

- Analyze the busiest month for both resort and city hotels based on the number of guests.
- Sort the months in chronological order and plot a line chart to visualize the guest trends.

### Task 6: Length of Stay and Bookings by Market Segment

- Analyze the length of stay at hotels and group the data by total nights and hotel type.
- Plot a bar chart to visualize the stays in different hotel types.
- Analyze bookings by market segment using a pie chart.

### Task 7: Price per Night, Cancellations, and High Cancellation Month

- Analyze the price per night (ADR) and person based on booking and room type.
- Analyze the number of bookings that were cancelled for both resort and city hotels.
- Identify the month with the highest number of cancellations.

## Running the Analysis

To run the analysis, execute the `hotel_booking_analysis.py` script. The script will perform the data cleaning, preprocessing, and analysis tasks described above. Each task's results will be displayed through various visualizations, such as pie charts, bar charts, line plots, and more.

Feel free to modify the script or add additional analysis based on your requirements.

## Conclusion

This project provides a comprehensive analysis of hotel booking data, covering various aspects such as guest origins, price variations, guest preferences, booking trends, and more. The visualizations generated

 from the analysis help in understanding the patterns, trends, and insights present in the dataset. By exploring the code and results, you can gain valuable insights into the hotel booking industry and make informed decisions based on the data.

For more detailed information, please refer to the code comments and documentation provided within the `hotel_booking_analysis.py` script.
