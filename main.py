import pandas as pd         # Data manipulation, extraction
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px
import sort_dataframeby_monthorweek as sd
import warnings
from warnings import filterwarnings
filterwarnings('ignore')



# Task-1 : Perform Data Cleaning and Data Pre-processing on data

# Read Data
df = pd.read_csv(r'C:\Data Science\Projects\Hotel Booking\hotel_bookings.csv')
# pd.set_option('display.max_columns',None)
print(df.head())

# print(df.isnull.values.any())           # Returns boolean Whether null values are present or not
# print(df.isnull.sum())                  # Returns the number of null values

# Filling the null values with value = 0
df.fillna(0,inplace=True)

df['meal'].value_counts()
df['children'].unique()
df['adults'].unique()
df['babies'].unique()
# The above 4 rows returns unique values, but it also contains entries with 0 values which he have to resolve.

# So, we have to make a filter in order to filter out 0 values and manipulate them
custom_filter = (df['children'] == 0) & (df['adults'] == 0) & (df['babies'] == 0)
# Passing the filter in dataframe
print(df[custom_filter])        # Returns all the wrong values i.e. contains entries with value = 0
print(df[~custom_filter])       # Returns all the correct values i.e. excludes all wrong values



# Task-2 : Where do the guests come from (country) & performing spatial analysis
# Creating dataframe for filtering data
resort = df[(df['hotel'] == 'Resort Hotel') & (df['is_canceled'] == 0)]

city = df[(df['hotel'] == 'City Hotel') & (df['is_canceled'] == 0)]
print(city.head())

labels = resort['country'].value_counts().index
values = resort['country'].value_counts()

trace = go.Pie(labels=labels,values=values,hoverinfo='label+percent',textinfo='value')
iplot([trace])

# Creating a dataframe to extract country names
country_wise_data = df[df['is_canceled'] == 0]['country'].value_counts().reset_index()
country_wise_data.columns = ['country','No of guests']
print(country_wise_data.head())

fig = px.choropleth(country_wise_data,
              locations=country_wise_data['country'],
              color=country_wise_data['No of guests'],
              hover_name=country_wise_data['country'],
              title='Home Country of Guests')
fig.show()



# Task 3: Analysing about the variation of hotel price across year

data_hotel = df[df['is_canceled'] == 0]        # Creating a dataframe for task 3 i.e. to remove cancelled bookings
plt.figure(figsize=(12,8))
sns.boxplot(x='reserved_room_type',y='adr',data=data_hotel,hue='hotel')
plt.title("Price of rooms based on their types i.e per night per person",fontsize=16)
plt.xlabel('Room Type')
plt.ylabel('Price in EURO')
plt.show()

data_resort = resort[resort['is_canceled'] == 0]
data_city = city[city['is_canceled'] == 0]
print(data_resort.head())
print(data_city.head())

# Grouping data based on months & adr i.e. price

resort_hotel = data_resort.groupby('arrival_date_month')['adr'].mean().reset_index()
city_hotel = data_city.groupby('arrival_date_month')['adr'].mean().reset_index()

# Merging the about two dataframes

final = resort_hotel.merge(city_hotel,on='arrival_date_month')
final.columns = ['month','price_for_resort','price_for_city_hotel']

# Sorting this dataframe by downloading a library named sort-dataframeby-monthorweek & sorted-months-weekdays

final2 = sd.Sort_Dataframeby_Month(final,monthcolumnname='month')
print(final2.head())

# Plotting a line plot

fig2 = px.line(final2,x='month',y=['price_for_resort','price_for_city_hotel'],title='Room Prices across the year')
fig2.show()



# Task-4: a). Distribution of nights spent at hotels by market segment and hotel type
# b). Analyzing preference of guests

sns.boxplot(x='market_segment',y='stays_in_weekend_nights',data=df,hue='hotel')
plt.figure(figsize=(15,10))
plt.show()

# Plotting a Donut chart to visualize the data

df['meal'].value_counts()
fig3 = px.pie(data_frame=df,values=df['meal'].value_counts(),names=df['meal'].value_counts().index,hole=0.5)
fig3.show()



# Task-4: a). Analyze special requests by customers
# b). Creating a pivot table of relationship btw special request and cancellation booking status

sns.countplot(df['total_of_special_requests'])
plt.show()

# Grouping data based on types of special requests

pivot = df.groupby(['total_of_special_requests','is_canceled']).agg({'total_of_special_requests':'count'}).rename({'total_of_special_requests':'count'}).unstack()
pivot.plot(kind='bar')
plt.show()



# Task-5 : Analysing the busiest month

rush_resort = data_resort['arrival_date_month'].value_counts().reset_index()
rush_resort.columns = ['month','No. of Guests']

rush_city = data_city['arrival_date_month'].value_counts().reset_index()
rush_city.columns = ['month','No. of Guests']

# Merging the above two dataframes

final_rush = rush_resort.merge(rush_city,on='month')
final_rush.columns = ['month','No. of guests in resort','No. of guests in city hotel']

# Sorting Months (asc)

final_rush2 = sd.Sort_Dataframeby_Month(df=final_rush,monthcolumnname='month')

# Plotting a line plot

fig4 = px.line(data_frame=final_rush2,x='month',y=['No. of guests in resort','No. of guests in city hotel'],title='Total No. of guests per month')
fig4.show()



# Task-6: a). How long do people stay at hotel?
# b). Bookings by market segment

custom_filter_2 = df['is_canceled'] == 0
clean_data = df[custom_filter_2]
print(clean_data.head())

# Creating a dataframe which contains total no. of stays during weekend & weekdays

clean_data['total_nights'] = clean_data['stays_in_weekend_nights'] + clean_data['stays_in_week_nights']
# A new column of 'total_nights' is added to the dataframe clean_data

# Creating a dataframe by grouping total_nights and hotel
stay = clean_data.groupby(['total_nights','hotel']).agg('count').reset_index()      # Adding reset_index() creates a dataframe
stay = stay.iloc[:,0:3]            # Limiting the number of column to 3

stay.rename(columns={'is_canceled':'number of stays'})   # Renaming a column
stay['number of stays'] = stay.index
print(stay.head())

plt.figure(figsize=(20,8))
sns.barplot(x='total_nights',y=stay.index,hue='hotel',hue_order=['City hotel','Resort hotel'],data=stay)
plt.show()

# Bookings as per market segment
clean_data['market_segment'].value_counts()
fig5 = px.pie(clean_data,values=clean_data['market_segment'].value_counts(),names=clean_data['market_segment'].value_counts().index,title='Bookings per market segment')
fig5.show()



# Task-7: a).price per night(adr) and person based on booking and room
# b). how many bookings were cancelled
# c). which month has the highest number of cancellations

plt.figure(figsize=(20,10))
sns.barplot(x='market_segment',y='adr',hue='reserved_room_type',data=clean_data)
plt.show()
# The above task gives us an idea about the customer's preference during bookings(i.e. Room type)


cancel = df[df['is_canceled'] == 1]
# Finding out the total cancellations for city hotels and resort hotels

len(cancel[cancel['hotel'] == 'Resort Hotel'])      # Gives total no. of resort hotel cancellations
len(cancel[cancel['hotel'] == 'City Hotel'])        # Gives total no. of city hotel cancellations

fig6 = px.pie(values=[len(cancel[cancel['hotel'] == 'Resort Hotel']),len(cancel[cancel['hotel'] == 'City Hotel'])],names=['rh_cancellations','ch_cancellations'])
fig6.show()

