# Fechas

# Las fechas son representaciones de una hora, día, semana, etc.

from datetime import datetime 

now = datetime.now()

def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.second)
    print(date.minute)
    print(date.year)
    print(date.month)
    print(date.timestamp())

print_date(now)

year_2024 = datetime(2023, 1, 1) # Para crear una fecha con horas

print(year_2024)

from datetime import time

current_time = time(21, 6, 0) # Solo hora

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2024, 12, 7) # Solo Fecha

print(current_date.year)
print(current_date.month)
print(current_date.day)

print("")

current_date = date.today() # Imprime el día en el que estamos

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month, current_date.day)  # Cambiamos de año 2024 a 2025 sumandole 1
print(current_date.year)

diff = year_2024 - now
print(diff)
diff = year_2024.date() - current_date
print(diff)

print("")

from datetime import timedelta # Se utiliza para trabajar con franjas de fechas. 

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)

