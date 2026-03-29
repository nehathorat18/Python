#cpu threshold
import psutil

def get_cpu_threshold():
    cpu_threshold=int (input("Enter the CPU threshold value"))
    current_cpu=psutil.cpu_percent(interval=1)
    print("current cpu %",current_cpu)
    if  current_cpu>cpu_threshold:
        print("Sent an email alert")
    else:
        print("CPU is in safe state")

get_cpu_threshold()

    



