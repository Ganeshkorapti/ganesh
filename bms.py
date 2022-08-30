data=[{'name':"ganesh","account_number":1122,"balence":5000000,"password":"jyothika","phone_number":1234567890},]
c_name=input("Enter your user name :")
c_pass=str(input("Enter your password :"))
for record in data:
    if record["name"]==c_name and record["password"]==c_pass:
      print(''''
      1.deposit
      2.withdraw
      3.mini statement
      4.user details
      ''')
      amount=record['balence']
      option=int(input("Select your option: "))
      if option==1:
        deposite=int(input("Enter your amount: "))
        amount+=deposite
        print("Total amount",amount)
      elif option==2:
        withdraw=int(input("Enter your amount: "))
        amount-=withdraw
        print("Total amount",amount)
      elif option==3:
        print('========Mini statement=========')
        print('Username: ',record['name'] )
        print('Total balence: ',amount)
        print('Thanks for visiting')
        print('========Mini statement=========')
      elif option ==4:
        print('Name: ',record['name'])
        print('Account number: ',record['account_number'])
        print('Phone number: ',record['phone_number'])
      else:
        print("Invalid Credentials")
    

