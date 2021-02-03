# Python program to implement client side of chat room.
import socket
import select
import sys
import wave
import pyaudio
import _thread


def Emmeting():
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
    record_seconds = 100
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
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
        # print(data)
        server.send(data)

    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    sys.stdout.flush()



def ReceiveVoice():
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
    while socks == server:
        message = socks.recv(2048)
        stream.write(message)



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = str("172.21.72.157") #str(sys.argv[1])
Port =  6666 #int(sys.argv[2])
server.connect((IP_address, Port))

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    """ There are two possible input situations. Either the
    user wants to give manual input to send to other people,
    or the server is sending a message to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        filename = "recorded.wav"
        # set the chunk size of 1024 samples
        chunk = 1024
        # sample format
        FORMAT = pyaudio.paInt16
        # mono, change to 2 if you want stereo
        channels = 1
        # 44100 samples per second
        sample_rate = 44100
        record_seconds = 100
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
        _thread.start_new_thread(Emmeting, ())
        _thread.start_new_thread(ReceiveVoice, ())
        while socks == server:
            message = socks.recv(2048)
            stream.write(message)
        print("quit")




server.close()
