"""
Name: Sachin Ravindra Wani
Stud ID: 1001563321
"""

import http.client
from time import time


class ClientCore:
    """
    core functionality of client is implemented in this class
    """
    try:
        # connect with server
        conn = http.client.HTTPConnection("localhost", 8000)
        print("\nconnection to " + conn.host + " at port " + str(conn.port) + " Successful")
        print("\nEnter file name: ")
        # take filename as user input
        file_name = input()
        t1 = time()
        # request the file from server
        conn.request("GET", file_name)
        t2 = time()
    except http.client.HTTPException as err:
        print(err)

    try:
        # receive server response
        resp = conn.getresponse()
    except http.client.RemoteDisconnected as err:
        print(err)

    try:
        # extract headers from response
        headers = resp.getheaders()
        print("Status: " + str(resp.status), resp.reason)
        RTT = round((t2 - t1), 2)
        print("RTT: " + str(RTT) + " Seconds")
        print("Server Name: " + headers[0][1])
        print("Date-Time: " + headers[1][1])
        print("Content Type: " + headers[2][1])
        print("HTTP version: " + str(resp.version))
        if resp.status == 200:
            print("\n<=====Message body=====>\n" + resp.read(200).decode())
        print("<=====END=====>\n")
    except:
        RTT = round((t2 - t1), 2)
        pass

    conn.close()
    print("Connection closed!")
