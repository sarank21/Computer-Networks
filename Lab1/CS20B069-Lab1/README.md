## Lab1
Run python3 <file_name> for all the files.

### Q1
Created an echo server which echoes the message sent by client. Response from server is printed on Client's side. If "end client" is given as input, client is ended. Although server continues to run.

### Q2
If permitted operand and values are given, the result is computed by the server program and answer is returned, which is printed by the client. If "exit" is given as input by client, the client program is ended.

### Q3
The client side requests the filename (.txt file) and value of n. Once given, the server reads the last 'n' characters from the file and sends it to client. Client creates another file (.txt file) with the name filename1 and writes the message sent by server on to the file. 
In case the filename sent by client does not exist in the current directory, server returns the message "SORRY!" and client prints the message "Server says file does not exist".