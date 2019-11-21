import time
import pandas as pd
import numpy as np
from datetime import datetime
import datetime as dt

#New Comment

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def sweek(i):
    switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
    return switcher.get(i,"Invalid day of week")

def smonth(i):
    switcher={
                1:'January',
                2:'February',
                3:'March',
                4:'April',
                5:'May',
                6:'June',
                7:'July',
                8:'August',
                9:'September',
                10:'October',
                11:'November',
                12:'December'
             }
    return switcher.get(i,"Invalid month")


     
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print ("Hello Lets explore some US bikeshare data")
    
    # Get user input for city (chicago, new york city, washington) with exception handling
    while True:
        try:
            city = input ("Enter name of city: ")
            city = city.lower()
            if (city == 'chicago') or (city == 'new york city') or (city == 'washington'):
                break
            else :
                print("Oops!  We don\'t have data for this city yet. Please try again...") 
        except :
            print('An error occurred.')
    
    # Get user input for month (all, january, february, ... , june)) with exception handling
    while True:
        try:
            month = input ("Enter specific month to filter (ie. January or All): ")
            month = month.lower()
            if (month == 'january') : 
                month = 1
                break
            elif (month == 'february') : 
                month = 2
                break
            elif (month == 'march')  : 
                month = 3
                break
            elif  (month == 'april')  : 
                month = 4
                break
            elif  (month == 'may')  : 
                month = 5
                break
            elif  (month == 'june')  : 
                month = 6
                break
            elif  (month == 'july')  : 
                month = 7
                break
            elif  (month == 'august')  :
                month = 8
                break
            elif  (month == 'september')  : 
                month = 9
                break
            elif  (month == 'october')  : 
                month = 10
                break
            elif  (month == 'november')  : 
                month = 11
                break
            elif  (month == 'december')  : 
                month = 12
                break
            elif  (month == 'all') : 
                month = 0
                break
            else :
                print("Oops!  Invalid Input. Please try again...")
                 
        except :
            print('An error occurred.')
    
    # Get user input for day of week (all, monday, tuesday, ... sunday) with exception handling        
    while True:
        try:
            day = input ("Enter specific day to filter (ie. Monday or All): ")
            day = day.lower()  
            if (day == 'monday') :
                day = 1
                break
            elif (day == 'tuesday') :
                day = 2
                break
            elif (day == 'wednesday') :
                day = 3
                break
            elif (day == 'thursday') :
                day = 4
                break
            elif (day == 'friday') :
                day = 5
                break
            elif (day == 'saturday') :
                day = 6
                break
            elif (day == 'sunday'):
                day = 7
                break
            elif (day == 'all'):
                day = 0
                break
            else :
                print("Oops! Invalid Input. Please try again...") 
        except :
            print('An error occurred.')

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
    if df.isnull().values.any():
        print ('There is NAN record!')
        df.dropna()
        print ('Data is clean NOW!')
    else:
        print ('Data is clean!')

    if df.empty == True:
        print('No Records Returned!! Please try again...')
        
    if (month == 0) and (day == 0) : 
        print ('Applying no filter on month and day...')
        return df
    elif (month > 0) and (day == 0) :   
        print ('Applying filter on month only...')
        df['month'] = pd.to_datetime(df['Start Time'])    
        df=df.loc[df['month'].dt.month==month]
        return df
    elif (month == 0) and (day > 0) :
        print ('Applying filter on day only...')
        df['day'] = pd.to_datetime(df['Start Time'])   
        df=df.loc[df['day'].dt.weekday==day]
        return df
    elif (month > 0) and (day > 0):
        print ('Applying filter on month and day...')
        df['both'] = pd.to_datetime(df['Start Time']) 
        df=df.loc[df['both'].dt.month==month]
        df=df.loc[df['both'].dt.weekday==day]
        return df
    else :
        print("Oops! Invalid Input. Please try again...")


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['dtime'] = pd.to_datetime(df['Start Time'])
    
    # Find the most occurance for month
    cm_month = int(df['dtime'].dt.month.mode())
    # Count the occurance for month
    month_count = df['dtime'].dt.month.value_counts()

    # Find the most occurance for day of week
    cm_wday = int(df['dtime'].dt.weekday.mode())
    # Count the occurance for day of week
    wday_count = df['dtime'].dt.weekday.value_counts()
    
    # Find the most occurance for hour of day
    cm_hour = int(df['dtime'].dt.hour.mode())
    # Count the occurance for hour of day
    hour_count = df['dtime'].dt.hour.value_counts()
    
    # TO DO: display the most common month
    print ("Most common month: ", smonth(cm_month), "   Count: ", month_count[cm_month] )
    
    # TO DO: display the most common day of week
    print ("Most common day: ", sweek(cm_wday), "   Count: ", wday_count[cm_wday]  )

    # TO DO: display the most common start hour
    print ("Most common start hour: ", cm_hour , "   Count: ", hour_count[cm_hour] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    # Find the occurance of each start station
    cm_start_st = df["Start Station"].value_counts()
    # Count the most occurance for start station
    start_count = cm_start_st.max()
    # Lookup the start station name based on the count
    start_stn = cm_start_st.loc[cm_start_st.values==start_count].index[0]
    print ("Most commonly used start station: ",start_stn , "   Count: ", start_count )
    
    # TO DO: display most commonly used end station
    # Find the occurance of each end station
    cm_end_st = df["End Station"].value_counts()
    # Count the most occurance for end station
    end_count = cm_end_st.max()
    # Lookup the end station name based on the count
    end_stn = cm_end_st.loc[cm_end_st.values==end_count].index[0]
    print ("Most commonly used end station: ", end_stn , "   Count: ", end_count )
    
    # TO DO: display most frequent combination of start station and end station trip
    
    df["Trip"]=df["Start Station"]+" TO "+df["End Station"]
    
    # Find the occurance of each trip
    cm_trip = df["Trip"].value_counts()
    # Count the most occurance for each trip
    trip_count = cm_trip.max()
    # Lookup the trip name based on the count
    trip_stn = cm_trip.loc[cm_trip.values==trip_count].index[0]
    print ("Most commonly trip is: ", trip_stn , "   Count: ", trip_count )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    sum_time=dt.timedelta()
    mean_time=dt.timedelta()
    ttime=dt.timedelta()
    
    # Display total travel time
    df['duration'] = pd.to_datetime(df['End Time'])-pd.to_datetime(df['Start Time'])
    
    for i in df['duration']:
        i=str(i)
        temp = i.replace(i[:7], '')
        (h,m,s) = temp.split(':')
        d = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum_time = sum_time+d
    print ("Total Travel Time: ", str(sum_time))

    # Display mean travel time
    mean_time=sum_time/df['duration'].count()
    print("Avg Travel Time: ", mean_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    if 'User Type' in df.columns: 
        cm_type = df["User Type"].value_counts()
        # Count the most occurance for gender
        type_count = cm_type.max()
        # Lookup the gender based on the count
        usertype = cm_type.loc[cm_type.values==type_count].index[0]
        print ("Most common user type: ", usertype , "   Count: ", type_count )
    else :
        print('** Warning! Missing User Type Data!')
        
    # Display counts of gender
    if 'Gender' in df.columns:  
        # Find the occurance of gender
        cm_sex = df["Gender"].value_counts()
        # Count the most occurance for gender
        sex_count = cm_sex.max()
        # Lookup the gender based on the count
        gender = cm_sex.loc[cm_sex.values==sex_count].index[0]
        print ("Most commonly gender: ", gender , "   Count: ", sex_count )
    else :
        print('** Warning! Missing Gender Data!')
    
   
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:  
        byear_early = df["Birth Year"].min()
        byear_recent = df["Birth Year"].max()
        # Count the most occurance for birth year
        cm_byear = df["Birth Year"].mode()
 
        print ("Earliest birth year: ", int(byear_early) )
        print ("Most recent birth year: ", int(byear_recent)  )
        print ("Most common year of birth: ", int(cm_byear) )
    else : 
        print('** Warning! Missing Birth Year Data!')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        c = 0
        datacount=df.shape[0]
        if int(datacount) > 0:
            while True:
                raw_view = input('\nWould you like to preview raw data? (Enter yes or no): ')
                
                if raw_view.lower() == 'yes':
                    num_row = input('How many row(s) you like to see? (Enter a number): ')
                    
                    if int(num_row) > int(datacount):
                        print('Error! Input exceed number of row in data file!')
                    else:
                        while c < int(num_row):
                            print(df.iloc[c],'\n')
                            c+=1
                elif raw_view.lower() == 'no':
                    break
        
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        else:
            print('\nError! No Data Records Returned. Try again...')
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
