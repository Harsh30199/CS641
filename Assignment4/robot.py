import pexpect

robot = pexpect.spawn('ssh students@172.27.26.188')
robot.expect('students@172.27.26.188\'s password:')
robot.sendline('cs641a')
robot.expect('Enter your group name: ') 
robot.sendline("Lazarus")

robot.expect('Enter password: ')
robot.sendline("lazarus123")

robot.expect('\r\n\r\n\r\nYou have solved 4 levels so far.\r\nLevel you want to start at: ', timeout=50)

robot.sendline("4")
robot.expect('.*')
robot.sendline("read")
robot.expect('.*')

f = open("plaintexts1.txt", 'r')
f1= open("ciphertexts1.txt",'w')


for line in f.readlines():
	robot.sendline(line)
	robot.expect("Slowly, a new text starts.*")
	print(robot.before)
	print('=======================================')
	print(robot.after)
	f1.writelines(str(robot.after)[73:89]+"\n")
	robot.sendline("c")
	robot.expect('The text in the screen vanishes!')
	
f.close()
f1.close()

f = open("plaintexts2.txt", 'r')
f1= open("ciphertexts2.txt",'w')


for line in f.readlines():
	robot.sendline(line)
	robot.expect("Slowly, a new text starts.*")
	print(robot.before)
	print('=======================================')
	print(robot.after)
	f1.writelines(str(robot.after)[73:89]+"\n")
	robot.sendline("c")
	robot.expect('The text in the screen vanishes!')

robot.close()
f.close()
f1.close()

