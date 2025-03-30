import pandas as pd

def part1():
    
    def filter_survivors(df):
        return df[df['Survived'] == 1]

    def fill_missing_age(df):
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        return df

    def add_fare_per_age(df):
        df['Fare_Per_Age'] = df['Fare'] / df['Age']
        return df

    titanic_df = pd.read_excel('lesson-17/data/titanic.xlsx')
    processed_titanic = (titanic_df
                        .pipe(filter_survivors)
                        .pipe(fill_missing_age)
                        .pipe(add_fare_per_age))

    print(processed_titanic[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())

def part2():
    def filter_long_delays(df):
        return df[df['DepDelay'] > 30]

    def add_delay_per_hour(df):
        df['Delay_Per_Hour'] = df['DepDelay'] / df['FlightDuration']
        return df


    flights_df = pd.read_parquet('flights.parquet')
    processed_flights = (flights_df
                        .pipe(filter_long_delays)
                        .pipe(add_delay_per_hour))

    print(processed_flights[['DepDelay', 'FlightDuration', 'Delay_Per_Hour']].head())