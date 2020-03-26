import reader
import time
import threading
import os

def sendEmail(list):
    print("SendEmail task assigned to thread: " + format(threading.current_thread().name))
    print("ID of process running task sendEmail: " + format(os.getpid()))
    t = time.process_time()
    for contact in list:
        time.sleep(0.5)

    endTime = time.process_time() - t

print("Execution started...")
startTime = time.process_time()
email_data = reader.readFile("info_file.csv")

num = int(input("Enter number of threads, you want to use: "))
flag = True
while (flag):
    if (len(email_data) % num == 0):
        flag = False
    else:
        num = int(input("Not applicable entry. Enter again: "))

pivot = int(len(email_data)/num) #pivot point that breaks the data into pieces for each thread
list_of_threads = []
for i in range(num+1):
    thread_worker = threading.Thread(target=sendEmail, args=(email_data[pivot*i:pivot*(i+1)],))
    list_of_threads.append(thread_worker)

for thread in list_of_threads:
    thread.start()
    print("Started: "+ thread.name + "\n")

for thread in list_of_threads:
    thread.join()
    print("Ended: " + thread.name + "\n")


finishTime = time.process_time() - startTime
print("Time elapsed to finish: " + str(finishTime))
print("Execution finished!")