#setting up my compiler
CC = gcc
question1: q1.sh
	chmod +x q1.sh
	./q1.sh
question2: q2.sh q2p2.sh
	chmod +x q2.sh
	./q2.sh
	chmod +x q2p2.sh
	./q2p2.sh
question3: q3
	./q3
q3: q3.c
	$(CC) q3.c -o q3
q3.c:
	echo "#include<stdio.h>\nprintf(\"hello word \\\n\");\nreturn 0;" > q3.c

question5: q4Server q4Client
	gnome-terminal -- bash -c "./q4Server; exec bash" &
	sleep 1
	gnome-terminal -- bash -c "./q4Client; exec bash"

q4Server: q4Server.c
	$(CC) q4Server.c -o q4Server
q4Client: q4Client.c
	$(CC) q4Client.c -o q4Client