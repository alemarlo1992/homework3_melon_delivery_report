

def produce_summary(day_num, date_file):
    #we created a function to avoid repeatition 
    """ We will create a produce summary that includes 
    the melon name, count sold, and amount sold
    """
    print("Day", day_num)
    #We want to include the day of each delivery 
    file_name = "um-deliveries-" + date_file + ".txt"
    """ this will allow us to change teh date_file to the corresponding 
    dates that we want to obtain
    """
    the_file = open(file_name)
    #this line will open up the file 


    for line in the_file:
    #we will create a loop through each line of the file
    
        line = line.rstrip()
    #remove empty spaces from the file
    
        words = line.split('|')
    #make the line into a list so wr can access info for each
    

        melon = words[0]
        count = words[1]
        amount = words[2]
    #accessding the list through the index
   

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
    #print the desired count, nmelon type, and total in money
    the_file.close()
    #closes the file from the loop

produce_summary(1, "20140519")
produce_summary(2, "20140520")
produce_summary(3, "20140521")

#calls the fuction with each corresponding date that we want


