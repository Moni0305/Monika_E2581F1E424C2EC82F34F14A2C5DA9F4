def isleapyear(year):
  if(year%4==0 and year%100!=0)oryear%400==0:
  return True
 else:
  return False
year=2013
if isleapyear(year):
   print("{} is leap year".format(year))
else:
   print("{}is not a leap year".format(year))