def getdate():
    import datetime
    return datetime.datetime.now()
print("Welcome to Health Managment System \n Please choose your plan ")
user = int(input("1 : Log Data \n2 : Retrive Data \n>>"))
if user == 1:
    Plan = int(input(" 1 : Log Diet \n 2 : Log Exercise \n>>"))
    if Plan == 1:
        client = int(input("Choose your client \n 1 : Harry \n 2 : Rohan \n 3 : Vipul \n>>1"))
        if client == 1:
            f = open ("HarryDiet.txt","a")
            inp = input("Enter the Diet taken by Harry : ")
            time = str(getdate())
            f.write(inp + "[" + time +inp+ "]")
            f.close
        if client == 2:
            f1 = open ("RohanDiet.txt","a")
            inp = input("Enter the Diet taken by Rohan : ")
            time = str(getdate())
            f1.write(inp + "[" + time +inp+ "]")
            f1.close
        if client == 3:
            f2 = open ("VipulDiet.txt","a")
            inp = input("Enter the Diet taken by Vipul : ")
            time = str(getdate())
            f2.write(inp + "[" + time + inp+"]")
            f2.close
    if Plan == 2:
        client = input("Choose your client \n 1 : Harry \n 2 : Rohan \n 3 : Vipul \n>>")
        if client == 1:
            f3 = open ("HarryExercise.txt","a")
            inp = input("Enter the Exercise done by Harry : ")
            time = str(getdate())
            f3.write(inp + "[" + time +inp+ "]")
            f3.close
        if client == 2:
            f4 = open ("RohanExercise.txt","a")
            inp = input("Enter the Exercise done by Rohan : ")
            time = str(getdate())
            f4.write(inp + "[" + time +inp+ "]")
            f4.close
        if client == 3:
            f5 = open ("VipulExercise.txt","a")
            inp = input("Enter the Exercise done by Vipul : ")
            time = str(getdate())
            f5.write(inp + "[" + time +inp+ "]")
            f5.close
if user == 2:
    Plan = int(input(" 1 : Retrive Diet \n 2 : Retrive Exercise \n>>"))
    if Plan == 1:
        client = int(input("Choose your client \n 1 : Harry \n 2 : Rohan \n 3 : Vipul \n>>"))
        if client == 1:
            f = open ("HarryDiet.txt")
            print(f.read())
            f.close
        if client == 2:
            f1 = open ("RohanDiet.txt")
            print(f1.read())
            f1.close
        if client == 3:
            f2 = open ("VipulDiet.txt")
            print(f2.read())
            f2.close
    if Plan == 2:
        client = input("Choose your client \n 1 : Harry \n 2 : Rohan \n 3 : Vipul \n>>")
        if client == 1:
            f3 = open ("HarryExercise.txt")
            print(f3.read())
            f3.close
        if client == 2:
            f4 = open ("RohanExercise.txt")
            print(f4.read())
            f4.close
        if client == 3:
            f5 = open ("VipulExercise.txt")
            print(f5.read)
            f5.close
