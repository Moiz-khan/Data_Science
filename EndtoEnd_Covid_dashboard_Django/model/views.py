from django.shortcuts import HttpResponse, render
import matplotlib.pyplot as plt
from pandas.io.parsers import count_empty_vals, read_csv
import seaborn as sns
import pandas as pd
import numpy as np

# For models
#Getting Random Forest class from sklearn.ensemble
from sklearn.ensemble import RandomForestRegressor

#Getting Random Forest class from sklearn.tree
from sklearn.tree import DecisionTreeRegressor

#For Splitting of data in train and test
from sklearn.model_selection import train_test_split

#for Mean Absolute Error of every model
from sklearn.metrics import mean_absolute_error



df = pd.read_csv('E:\Django\mldeploy\deploy\model\PKCOVID-19.csv')

# Create your views here.
def index(request):
    plot_pie_chart()
    cities = df.Province.unique()
    print(cities)
    params = visualize()
    # print(params)
    sindh_cases()
    
    
    report_cases()
    params_prov = province_cases()
    models()

    data = {'params': params, 'prov_info': params_prov}
    print(data)
    return render(request, 'model/index.html', data)


def visualize():
    cases = int(df.Cases.sum())
    deaths = int(df.Deaths.sum())
    recovd = int(df.Recovered.sum())
    
    # fg = df.hist()
    info = [cases, deaths, recovd]
    finalData = {}
    params = {"finalData" : info}
    # print(df.head())

    return info

sizes = np.array([5860, 677, 3200])
def absolute_value(val):
    a  = np.round(val/100.*sizes.sum(), 0)
    return int(a)

def plot_pie_chart():
    # Creating dataset
    cities = df.Province.unique()
    counts = []
  
    for i in cities:
        counts.append( df[df.Province == i]['Cases'].sum())

    cities = cities[:9]
    counts = counts[:9]
    cities = np.delete(cities, 5)
    kpk = counts[5] + counts[6]
    counts[5] = kpk
    counts.remove(2.0)
   
    # Creating plot
    # fig = plt.figure(figsize =(10, 7))
    plt.pie(counts, labels = cities, autopct=absolute_value, shadow=True)
    
    # show plot
    # plt.savefig('pie_chart.png',dpi=100)


def sindh_cases():
    cities = df.Province.unique()
    print(cities)

    '''['Islamabad Capital Territory' 'Sindh' 'Gilgit-Baltistan' 'Baluchistan'
 'Punjab' 'Khyber Pakhtunkhwa' 'khyber Pakhtunkhwa' 'Azad Jummu Kashmir'
 'Federal Administration Tribal Area']'''
   
    covid_case = df[df['Province'] == 'Azad Jummu Kashmir']["Cases"][:10]
    plt.title("No of cases in Azad Jummu Kashmir")
    plt.xlabel("Cases")
    plt.ylabel("Dates")
    # plt.bar( covid_case[:10], df.Date.head(10))
    plt.barh(df.Date.head(10), covid_case)

    # plt.savefig('case_ajk.png',dpi=100)



def province_cases():
    case = []
    recov = []
    death = []
    case_info = []

    cities = df.Province.unique()

    for i in cities:
        case.append(int(df[df['Province'] == i]['Cases'].sum()))
        recov.append(int(df[df['Province'] == i]['Recovered'].sum()))
        death.append(int(df[df['Province'] == i]['Deaths'].sum()))


    kpk = case[5] + case[6]
    case[5] = kpk
    case.remove(2.0)
    
    kpk_rec= recov[5] + recov[6]
    recov[5] = kpk_rec
    recov.remove(0.0)

    kpk_death = death[5] + death[6]
    death[5] = kpk_death
    death.remove(0.0)

    case_info = [case, recov, death]
    return case_info


def report_cases():
    Dates = df['Date']
    Cases = df['Cases']
    
    plt.title("No of Cases on per Day")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.barh(Dates[:10], Cases[:10])

    # plt.savefig('cases.png',dpi=100)
    # Show Plot
    

def models():
#characteristics/features of a house used to train model
    df.dropna(inplace=True)
    features = ['Cases', 'Recovered']
    X = df[features]
    y = df.Deaths

    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    # print(val_X)
    covid_rf = RandomForestRegressor(random_state=0)
    covid_rf.fit(train_X, train_y)
    rf_preds_val = covid_rf.predict(val_X)
    rf_model_mae = mean_absolute_error(rf_preds_val, val_y)
    # print(rf_model_mae)

    pred_data = {'Deaths': rf_preds_val}
    pred_data = pd.DataFrame(pred_data)
    # print(pred_data.head())
    #dates X axis y-axis deaths
    # plt.figure(figsize=[10,8])

    plt.hist(x=pred_data)
    # plt.savefig('hist.png',dpi=100)

    # covid_model = DecisionTreeRegressor(random_state=1)
    # covid_model.fit(train_X, train_y)
    # covid_model_preds = covid_model.predict(val_X)
    # val_mae = mean_absolute_error(covid_model_preds, val_y)
    # print(val_mae)