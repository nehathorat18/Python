
for i in range(5):

    env = input("Enter the env name")
    print("The env is ",env)

    if env=="prod":
        print("Don't deploy on friday")
    elif env=="stg":
        print("Take backup and test well")
    else:
        print("deploy on any day")
