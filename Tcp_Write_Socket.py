#Function Usage:-
#
#   from Tcp_Write_Socket import wr2socket
#
#   wr2socket("output")------->only specify name of file(EXTENSION NOT NEEDED)
#   
#   Default port used :- 6996
#


def wr2socket(file):
    import socket
    import time
    filename = "%s.txt" %file
    s = socket.socket()                                                 #creates socket with socket object s;

    port = 6996                                                         #port used by socket;

    s.bind(('',port))                                                   #binds socket
    s.listen()                                                          #listens for incoming connections
    connector,addr =s.accept()                                          #connector is a new socket object and
                                                                        #addr is the address bound to the socket on the other end of the connection.

    lineList = [line.rstrip('\n') for line in open(filename,"r")]       #Converts text file to a list

    for i in lineList:                                                  #iterates over the list
        resp = connector.sendall(i.encode('utf-8'))                     #encodes each list element as UTF-8 as string datatype not supported
        if(resp==None):                                                 #sendall returns None if successfull data tx
            print("Successfull Tx")
        time.sleep(1)

    connector.close()                                                   #close the socket
