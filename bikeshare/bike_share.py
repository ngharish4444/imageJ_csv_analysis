import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'bikeshare\chicago.csv',
              'new york city': 'bikeshare\new_york_city.csv',
              'washington': 'bikeshare\washington.csv' }

def get_filters():
    global city, month, day
    while True:
        city_names = ['chicago','new york city','washington']
        city_names = [x.lower() for x in city_names ]
        month_names = ["all","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec","January","February","March","April","May","June","July","August","September","October","November","December"]
        month_names = [x.lower() for x in month_names]
        day_names = ['all','Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        day_names =[x.lower() for x in day_names]

        c=input('Enter city name: ') or 'chicago'
        m=input('Enter month name: ') or 'all'
        d=input('Enter day name: ') or 'all'
        
        if c in city_names and m in month_names and d in day_names:
            print('data format is correct')
            break
        else:
            print('data in wrong format')
    city =c
    month =m
    day =d
    print('Hello! Let\'s explore some US bikeshare data!')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    global df_1
    p_c= CITY_DATA[city]
    df_1 = pd.read_csv(p_c)
    
    df_1['Start Time']= pd.to_datetime(df_1['Start Time'])
    df_1['End Time']= pd.to_datetime(df_1['End Time'])
    df_1['month']=df_1['Start Time'].dt.month_name()
    df_1['day']=df_1['Start Time'].dt.day_name()
    df_1['hour']= df_1['Start Time'].dt.hour
    
    return df_1



def time_stats(df_1):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('{} month is most popular month'.format(df_1['month'].mode()[0]))

    print('{} is most popular day'.format(df_1['day'].mode()[0]))

    print('The {}.00 hour is most popular'.format(df_1['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    ss = df_1['Start Station'].value_counts().idxmax()
    es = df_1['End Station'].value_counts().idxmax()
    print('The most popular Start Station {}'.format(ss))
    print('The most popular End Station {}'.format(es))
    
    print('most famous start station is{} & end staion is {}'.format(ss,es))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('Total travel duration {} minutes'.format(sum(df_1['Trip Duration'])/60))
    print('Average travel duration {} minutes'.format(df_1['Trip Duration'].mean()/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    x=df_1['User Type'].value_counts()
    print('Number of user types\n {}'.format(x))
    y=df_1['Gender'].value_counts()
    print('Number of gender types\n {}'.format(y))
    ear= df_1['Birth Year'].min()
    more =df_1['Birth Year'].max()
    mc= df_1['Birth Year'].value_counts().idxmax()
    print('the earliest birth date {} , most recent birth date {} and common birth year {}'.format(ear,more,mc))
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()