log_file = open("um-server-01.txt")

#Function name
def sales_reports(log_file):
    #Function to get the report from the um-server-01.txt file
    for line in log_file: #for everyline that is in um-server-01.txt file do:
        line = line.rstrip() #remove the blank space of the right
        day = line[0:3] #day = the fist three characters of the string line
        if day == "Mon": #if the day is Monday
            print(line) # print line


sales_reports(log_file)
