def generateLdifEntry(file, seed):
    firstName="user"
    lastName="test"
    baseDn="ou=root,ou=fr"
    seed=str(seed)
    file.write("dn: uid=" + firstName + seed + "." + lastName + "," + baseDn + "\n")
    file.write("uid: " + firstName + seed + "." + lastName + "\n")
    file.write("cn: " + firstName + " " + lastName + "\n")
    file.write("\n")


file = open("file.ldif","w+")
for i in range(20):
    generateLdifEntry(file,i)
file.close()
