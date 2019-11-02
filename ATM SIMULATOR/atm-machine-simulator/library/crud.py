from data import Data

counts = []

def insert(data):
    global counts
    counts.append(data)

    return 1

def save():
    global counts
    with open("database.txt", 'w') as file:
        #print(counts)
        for count in counts:
            file.write(count.fname+' '+count.mname+' '+count.lname+' '+count.sex+' '+count.pin+' '+str(count.balance)+' '+count.cardNo+ '\n')
    print("Register SUCCESSFUL!")

def retrieve():
    global counts
    with open("database.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split(' ')
            insert(Data(line[0], line[1], line[2], line[3], line[4], float(line[5]), line[6].strip()))

def save_to_card(path, acc_no):
    with open(path+":\\"+"CSFB"+".txt",'w') as file:
        file.write(acc_no)