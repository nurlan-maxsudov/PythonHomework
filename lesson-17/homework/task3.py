import pandas as pd

def part1():
    titanic_df = pd.read_excel('lesson-17/data/titanic.xlsx')


    def classify_age(age):
        if pd.isna(age): 
            return 'Unknown'
        return 'Child' if age < 18 else 'Adult'

    titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age)

    print(titanic_df[['Age', 'Age_Group']].head(10))
def part2():
    df = pd.read_csv("lesson-17/data/employee.csv")

    def normalize_salaries(group):
        return (group - group.mean()) / group.std()

    df["Normalized Salary"] = (df.groupby("DEPARTMENT")["BASE_SALARY"].transform(normalize_salaries))

    print(df[["UNIQUE_ID", "POSITION_TITLE", "DEPARTMENT", "BASE_SALARY", "Normalized Salary"]])

def part3():
    df = pd.read_csv("lesson-17/data/movie.csv")

    def classify_movie(duration):
        if duration < 60:
            return "Short"
        elif duration < 120:
            return "Medium"
        elif duration > 120:
            return "Long"

    df["Movie type"] = df["duration"].apply(classify_movie)
    print(df)



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
