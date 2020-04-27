import datetime, pandas, requests, json

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
date = Previous_Date.strftime ('%m-%d-%Y')
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' +  date + '.csv'
r = requests.get(url)

f = open('test.csv', 'wb')
f.write(r.content)
f.close

colnames = ['FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key']
data = pandas.read_csv('test.csv', names=colnames, engine='python', encoding='utf-8', error_bad_lines=False)
cases = data.Confirmed.tolist()
latitude = data.Lat.tolist()
longitude = data.Long_.tolist()


c = []

for i in range(len(cases)):
    c.append(latitude[i])
    c.append(longitude[i])
    c.append(cases[i])

d = json.dumps(c)

h = open('data.json', 'wb')
h.write(d)
h.close
