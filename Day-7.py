'''
#for-else with Notifications scenario

#notifications = [0,0,0,0]
#try to take notifications from user -->list of integers
notifications = list(map(int,input("Enter the values -->0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print('Unread Notification')
        break
else:
    print('All caught up')
'''
#While -->it relies on condition, it will be completely executed until the condition is satisfied
'''
Syntax while:

while<condition>:
     statement(s).....
     ............
     ......

while True:
    print("Yes")

#It runs an infinite loop, we need to press ctrl+c(keyboard interrupt)
    
i=0 #initialised statement
while i<=9:
      i=i+1
      print(i)

#Get code from 10 to 1
i=0
while i<=10:
    print(10-i)
    i=i+1
'''
#banking scenario -->PIN authentication if more than 3 attempts account locked..

pin = "1112"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("Login Successful")
        break
    else:
        print("Entered PIN is wrong..try again carefully")
        current_attempt +=1
else:
    print("Account Locked,try after 24 hours...")
    





