import pandas as pd

def calculate_demographic_data():
    columns = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship',
               'race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']
    
    data = pd.read_csv("adult.data.csv", names=columns)

    racecount = data['race'].value_counts()

    totalpeople = len(data)
    filteredu = data[data['education'] == 'Bachelors']
    percentagebachelors = round((len(filteredu) / totalpeople) * 100, 1)

    advedu = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advrich = advedu[advedu['salary'] == '>50K']
    highereducationrich = round((len(advrich) / len(advedu)) * 100, 1)

    nonadvedu = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    nonadvedurich = nonadvedu[nonadvedu['salary'] == '>50K']
    lowereducationrich = round(len(nonadvedurich) / len(nonadvedu) * 100, 1)

    minwork = data['hours-per-week'].min()
    minhrswork = data[data['hours-per-week'] == minwork]
    minhrssalary = minhrswork[minhrswork['salary'] == '>50K']
    richpercentageminhours = round(len(minhrssalary) / len(minhrswork) * 100, 1)

    totalpercountry = data['native-country'].value_counts()
    richcountry = data[data['salary'] == '>50K']['native-country'].value_counts()
    percentagepercountry = (richcountry / totalpercountry) * 100
    highestearningcountry = percentagepercountry.idxmax()
    highestearningcountrypercentage = round(percentagepercountry.max(), 1)

    richinindia = data[(data['salary'] == '>50K') & (data['native-country'] == 'India')]
    topINoccupation = richinindia['occupation'].value_counts().idxmax()

    return {
         'racecount': racecount,
          'percentagebachelors': percentagebachelors,
          'highereducationrich': highereducationrich,
         'lowereducationrich': lowereducationrich,
         'minworkhours': minwork,
         'richpercentageminhours': richpercentageminhours,
         'highestearningcountry': highestearningcountry,
         'highestearningcountrypercentage': highestearningcountrypercentage,
         'topINoccupation': topINoccupation
    }


                       


  




