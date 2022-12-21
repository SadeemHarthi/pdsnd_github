import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    city=input(" \nEnter the city name that you want to see data for . Chicago or New York City or Washington: ").lower()
    while city not in CITY_DATA:
        city=input("Invalid city name, Please Try Again. P.S. Pay extra attention to the list of cities available above.").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month=input("\nEnter the month from January to June or enter All: ").lower()
    while month not in months:
        month=input("Invalid month, Please Try Again. P.S. Pay extra attention to the list of months avalibale above.").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sunday']
    day=input("\nEnter a specific day or enter All: ").lower()
    while day not in days:
        day=input("Invalid day, Please Try Again.").lower()

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
    df=pd.read_csv(CITY_DATA[city])
    #convert the start time to date time using datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])

    #now to create new columns for month and day we will extract them from Start Time
    df['month']= df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    #create new column for hour by extract it from Start Time
    df['hour']= df['Start Time'].dt.hour
    #filter data by month
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month= months.index(month)+1
        df= df[df['month'] == month]
    #filter data by day
    if day != 'all':
        df= df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month= df['month'].mode()[0]
    print(f"Most Common Month is: {most_common_month}") 

    # TO DO: display the most common day of week
    most_common_day= df['day_of_week'].mode()[0]
    print(f"Most Common Day of Week is: {most_common_day}")
          

    # TO DO: display the most common start hour
    most_common_hour= df['hour'].mode()[0]
    print(f"Most Common Start Hour is: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Commonly Used start Stationis:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most Commonly Used End Station is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("\nMost Frequent Combination of Start and End Station Trip are: \n\n", df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time is: ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean Travel Time is: ", df['Trip Duration'].mean()) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    print(f"Counts of User types: \n {user_types}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender= df['Gender'].value_counts()
        print(f"Counts of The Users Gender: \n {gender}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest= df['Birth Year'].min()
        print(f"Earliest Year of birth: \n {earliest}")
        recent= df['Birth Year'].max()
        print(f"Most Recent Year of Birth: \n {recent}")
        common= df['Birth Year'].mode()[0]
        print(f"Most Common Year of Birth: \n {common}")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        #raw data display upon request by the user
        n= 0
        raw_data= ['yes', 'no']
        user_input= input(" Do you want to see more data? \n -enter 'yes' for more data \n -enter no if you don\'t more data \n").lower()
        while user_input.lower() not in raw_data:
            user_input= input("Please enter 'yes' or 'no'").lower()
            
        while True:
            if user_input.lower() == 'yes':
                print(df.iloc[n : n+5])
                n+= 5
                user_input= input(" Do you want to see more data? \n -enter 'yes' for more data \n -enter no if you don\'t more data \n").lower()
                while user_input.lower() not in raw_data:
                    user_input= input("Please enter 'yes' or 'no'").lower()
                else:
                    break
                    

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
