import datetime

inputData = input("in: ")
inputComponents = inputData.split(",")

date = datetime.date(int(inputComponents[0]), 1, 1)
week = int(inputComponents[1])

while(date.isocalendar()[1] < week):
    date += datetime.timedelta(days=1)

while(date.weekday() > 0):
    date += datetime.timedelta(days=1)


print("out: " + str(date.ctime()))