fill=open("position.txt", "w+")
nb="0"
for i in range(17):
    fill.write(nb+"\n")
    nb=int(nb)+25
    nb=str(nb)




fill.close()