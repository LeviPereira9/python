import datetime

#data = date(2024,7,16)
#print(data)

#print(date.today())
#print(data)

#hora = time(1,2,3)

#print(datetime.now())

data = datetime.datetime(2024, 7, 16, 12,30,0)

agenda = data + datetime.timedelta(weeks=2)

print(agenda)

#Formatar a hora, ai sai como string
print(type(data.strftime("%d/%m/%Y - %H:%M")))

#Formatar uma string pra hora

#A string tem que ser igual ao format que passamos alí no strptime
#Sai como datatime
date_string = "20/07/2023 - 15:30"

d = datetime.datetime.strptime(date_string, "%d/%m/%Y - %H:%M")
print(type (d))