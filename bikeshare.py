import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    isValidCity = False
    month = None
    day = None
    while not isValidCity:
        city = input('Would you like to see data for chicago, new york city, washington?\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            isValidCity = True
        else:
            isValidCity = False
            print('Please pick a listed city')
    # TO DO: get user input for month (all, january, february, ... , june)
        if isValidCity:
            isValidTimeInput = False
            while not isValidTimeInput:
                time = input('Would you like to filter the data by month, day, or not at all? Type none for no filter\n').lower()
                if time == 'month':
                    month = input('Which month - january, february, march, april, may, june?\n').lower()
                    if month in ('january', 'february', 'march', 'april', 'may', 'june'):
                        isValidTimeInput = True
                    else:
                        isValidTimeInput = False
                        print('Please enter a valid month')
                elif time == 'day':
                    day = input('Which day - monday, tuesday, wednesday, thursday, friday, saturday, sunday?\n').lower()
                    if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                        isValidTimeInput = True                    
                elif time == 'none':
                    isValidTimeInput = True
                else:
                    isValidTimeInput = False
                    print ('Please enter a valid response')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


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
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df_start_time = pd.to_datetime(df['Start Time'])
    df['month'] = df_start_time.dt.month
    max_month_int = df['month'].mode()
    print('Month: ',months[max_month_int[0] - 1].title())
   
    # TO DO: display the most common day of week
    df['day_of_week'] = df_start_time.dt.day_name()
    max_day = df['day_of_week'].mode()
    print('Day of week: ',max_day[0])

    # TO DO: display the most common start hour
    df['hour'] = df_start_time.dt.hour
    max_hour = df['hour'].mode()
    print('Hour of day: ',max_hour[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station']
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The Most commonly used start station: ', common_start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station']
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The Most commonly used end station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print(f'The Most common combination start and end station trip: {combo_station[0]} and {combo_station[1]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = sum(df['Trip Duration'])
    print('Total travel time: ',travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round(1)
    print('Mean travel time: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].fillna('Unknown').value_counts()
    print('Types of users:\n',user_type)

    # TO DO: Display counts of gender
    #df['Gender'].isnull().sum()
    try:
        gender = df['Gender'].fillna('Unknown').value_counts()
        print('Gender of users: ',gender)
    except KeyError:
        print('No Gender reported')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        print('Earliest year of birth: ',earliest_birth)
    except KeyError:
        print('No Birth Year reported')
    
    try:
        most_recent_birth = int(df['Birth Year'].max())
        print('Most recent year of birth: ',most_recent_birth)
    except KeyError:
        print('No Birth Year reported')
    
    try:
        most_common_birth_year = int(df['Birth Year'].mode())
        print('Most common year of birth: ',most_common_birth_year)
    except KeyError:
        print('No Birth Year reported')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    x = 0
    while True:
        rawdata = input('Would you like to see the rawdata? Enter Y or N.\n')
        if rawdata.lower() == 'y':
            print(df.iloc[x:x+5])
            x += 5
        elif rawdata.lower() == 'n':
            break
        else:
            print('Enter a valid response as Y or N')
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
     
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
