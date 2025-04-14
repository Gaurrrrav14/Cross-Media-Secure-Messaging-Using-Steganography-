with open("islab.txt", 'r') as file :
    s = file.read()
    s = s.encode('ascii', 'ignore').decode('utf-8')
    print(s[:100])