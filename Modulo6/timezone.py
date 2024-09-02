import datetime
import pytz

#Datetime com timezone ^d
dia = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

#Datetime timeZone SP sem pytz
dia2 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BR-SP"))

print(dia)
print(dia2)