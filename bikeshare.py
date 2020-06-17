import time
import pandas as pd
import numpy as np
from datetime import datetime


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cit = ''
    cities = ['chicago', 'new york', 'washington']
    while cit not in cities:
        cit = input('Which city would you like to explore (chicago, new york, washington)?').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month  not in months:
        month = input('Which month would you like to explore (all, january, february, march, april, may, june)?').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    days = ['all','mo','tu', 'we', 'th', 'fr', 'sa', 'su']
    while day not in days:
        day = input('Which day would you like to explore (all, mo, tu, we, th, fr, sa, su)?').lower()
    
    print('-'*40)
    return cit, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        days = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
        day = days.index(day)
        df = df[df['weekday'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    most_pop_hour = df['hour'].mode()[0]
    
    print('Hour with the most times of Travel: '+ str(most_pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used Start Station: ' + start_station)
    
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used End Station: ' + end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total Travel Time: '+str(total_duration))
    count = df['Trip Duration'].count()
    print('Amount of Travels: '+str(count))
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Average Travel Time: '+ str(mean_travel))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    print(user_types)
    print('\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        youngest_age  = 2020.0 - df['Birth Year'].max()
        oldest_age =  2020.0 - df['Birth Year'].min()
        avg_age = 2020.0 - df['Birth Year'].mean()
        print('Youngest Age: ' + str(youngest_age) + '\n')
        print('Oldest Age: ' + str(oldest_age) + '\n')
        print('Average Age: ' + str(avg_age) + '\n')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except KeyError: 
        print('No data for this city')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        trips = df.to_json()
        
        index = 0
        while True:
            individual_data = input('\nWould you like to see individual Data? Enter yes or no.\n')
            if individual_data == 'no':
                break
            if individual_data == 'yes':
                print(df.iloc[index:index + 5].to_json())
                index += 5
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
