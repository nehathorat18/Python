#SCRIPTING
#function KAAM
#indentation
def sum_of_num():
    num1=int (input("Enter the first num"))
    num2=int (input("Enter the second num"))
    sum=num1+num2
    print (sum)


env = input("Enter the env name")
print("The env is ",env)
if env=="prod":
    sum_of_num()#funcation calling
