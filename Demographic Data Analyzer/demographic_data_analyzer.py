import pandas as pd


def calculate_demographic_data(print_data=True):
    df=pd.read_csv("adult.data.txt",header=None)
    df.columns=['Age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().tolist()

    # What is the average age of men?
    df['sex']=df['sex'].astype('|S')
    a=df.loc[df['sex']== b' Male']
    b=a['Age'].tolist()
    average_age_men = round(sum(b)/len(b),1)

    # What is the percentage of people who have a Bachelor's degree?
    df['education']=df['education'].astype('|S')
    c=df.loc[df['education']==b' Bachelors']
    percentage_bachelors=round(c['Age'].count()/df['Age'].count()*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    z=df.loc[(df['education']==b' Bachelors')|(df['education']==b' Doctorate') | (df['education']==b' Masters') ]
    zz=z.loc[z['salary']==b' >50K']
    higher_education = round(zz['education'].count()/z['education'].count()*100,1)
    lower_education = (len(df[(df['education']!='Bachelors') &
                                  (df['education']!='Masters') &
                                  (df['education']!='Doctorate')])) / len(df) * 100


    # percentage with salary >50K
    higher_education_rich = (len(df[(df['salary']=='>50K')]) / len(df)) * 100
    lower_education_rich = (len(df[(df['salary']!='>50K')]) / len(df)) * 100   

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (len(df[df['hours-per-week'] == df['hours-per-week'].min()]))

    rich_percentage = (len(df[(df['hours-per-week'] == df['hours-per-week'].min()) &
                             (df['salary']=='>50K')]) / len(df)) * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning = []
    for i in df['native-country'].unique():
        population = len(df[(df['native-country']==i) & (df['salary']=='>50K')])
        highest_earning.append(population)
    
    highest_earning_country = max(highest_earning)
    highest_earning_country_percentage = (highest_earning_country / len(df)) *100
    # Identify the most popular occupation for those who earn >50K in India.
    df['salary']=df['salary'].astype('|S')
    df['native-country']=df['native-country'].astype('|S')
    d=df.loc[(df['salary']==b' >50K') & (df['native-country']==b' India')]

    top_IN_occupation = d['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }