from datetime import datetime

current_time = datetime.now().hour
print("\n*******************************************")
print("Note: we are useing 24 Hours of time format")
print("*******************************************")


if(5 <= current_time <=12):
    message = "A Very Good Morning! Have a nice day"
elif(12 <= current_time <=17):
    message = "A Very Good Afternoon! Hope your doing well today"
elif(17 <= current_time <=21):
    message = "A Very Good Evening! Relax and enjoy your evening"
else:
    message = "A Very Good Night! Take a rest and get recharged for next day"

print(message,"\n")