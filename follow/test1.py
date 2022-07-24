handles_file = open('data/list.txt', 'r')
handles = handles_file.readlines()
COUNTER=0
FOLLOW_REQ=5

for handle in handles:
    print(handles[0].strip('\n'))
    handles.pop(0)
    COUNTER = COUNTER + 1
    if (COUNTER >= FOLLOW_REQ + 1):
        break

print(handles)