# Escribir un programa que implemente un calendario perpetuo, es decir, que dado una fecha
# en formato mes, día y año le retorne al usuario el día de la semana que corresponde para esta
# fecha.

dia = int(input('Dia: '))
mes = int(input('Mes: '))
year = int(input('Anio: '))
 
if year < 1583:
  print('Solo acepta fechas mayores a 1582')
else:
  a = (14 - mes) // 12
  y = year - a
  m = mes + 12 * a - 2
 
  d = (dia + year + (year//4) - (year//100) + (year//400) + ((31 * m)//12)) % 7
 
  if d == 0:
    diaSemana = 'Domingo'
  elif d == 1:
    diaSemana = 'Lunes'
  elif d == 2:
    diaSemana = 'Martes'
  elif d == 3:
    diaSemana = 'Miercoles'
  elif d == 4:
    diaSemana = 'Jueves'
  elif d == 5:
    diaSemana = 'Viernes'
  else:
    diaSemana = 'Sabado'
 
  print('El dia %d del mes %d de %d es %s' %(dia,mes,year,diaSemana))