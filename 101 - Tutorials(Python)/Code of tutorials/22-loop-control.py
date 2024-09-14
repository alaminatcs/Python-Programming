# Loop control: used to change a loop execution from it's normal seq.
# break, continue, pass

# break used to bring-out from the loop forcefully
# --------------------------------------------------
for i in range(10):
    if i == 5:
        break
    # print('iteration no: ', i)



# continue used to skip the certain step/s in the loop
# --------------------------------------------------
for i in range(10):
    if i <= 4:
        continue
    # print('iteration no: ', i)


# pass similar to the continue but does nothing act as a placeholder
# ------------------------------------------------------------------
for i in range(15):
    if i < 10:
        pass
    else:
        print('iteration no: ', i)

# The pass statement is a placeholder that does nothing. It's often used in situations
# where a statement is required syntactically but you don't want to execute any code.