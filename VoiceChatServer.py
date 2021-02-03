import socket
import select
import sys
import ssl
import pyaudio

import _thread



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = str("172.21.72.157") #str("127.21.72.117")

Port = 6666

server.bind((IP_address, Port))

server.listen(100)

Clients = []

def ClientThread(conn, addr):
    conn.send("Bienvenue sur le Vocal".encode())
    import pyaudio
    import wave

    # the file name output you want to record into
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 5
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")


    while True:
        try:
            message = conn.recv(2048)
            if message:
                #print(message)
                #stream.write(message)
                message_send = (message)
                #print(bytes(message_send))
                broadcast(message_send, conn)

            else:
                remove(conn)

        except:
            continue




    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()






def broadcast(message, connection):
    for clients in Clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)



def remove(connection):
    if connection in Clients:
        Clients.remove(connection)

while True:
    conn, addr = server.accept()
    Clients.append(conn)
    print(addr[0] + "connecté !")
    _thread.start_new_thread(ClientThread, (conn, addr))

conn.close()
server.close()
