import sys

if len(sys.argv) >= 2: # check the number of argument passed

    data = open(sys.argv[1], "a")  # create file to add data

    while True:  # create a loop 
      line = input() # get line to save from the user
      if line != "SAVE": # check if line is the exit command before saving line to the file 
          data.write(line + "\n") # save line to the file
      else:
          break  #break out of the loop if the line is exit command

    data.close() #close file

    print("The above content has been saved to "+ str(sys.argv[1]))

else:
     print("Oops: file name argument is required")



