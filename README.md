## Real-Time Chat Application

Overview
This is a Python-based real-time chat application using socket programming and threading, developed as a solution for the Kuvaka Tech Backend Developer internship task.

Features
- Multithreaded server handling multiple client connections
- Real-time message broadcasting
- Simple text-based client interface

Technical Specifications
- Language: Python 3.8+
- Communication: Socket Programming
- Concurrency: Threading

Prerequisites
- Python 3.8 or higher
- Standard Python libraries (socket, threading)

Setup and Running
Server
python server.py

Client
Open multiple terminal windows and run:
python client.py


Architecture
- Server uses threading to handle multiple client connections concurrently
- Each client connection is managed in a separate thread
- Broadcasts messages to all connected clients except the sender

Design Choices
- Used threading for concurrent client handling
- Implemented error handling for network disconnections
- Simple, clean interface focusing on core functionality

Limitations and Potential Improvements
- No persistent message storage
- Basic error handling
- No authentication mechanism

Submission Details
- Developed for Kuvaka Tech Backend Developer Internship
- Demonstrates socket programming and concurrent network communication

License
MIT License
