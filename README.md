# Bank Queue Management System

This program is a simple Bank Queue Management System implemented using Python and Tkinter. The system allows users to simulate a bank queue where customers can be added to either a business queue or a personal queue. Customers are then served based on priority and assigned to available service desks.

## Features

- **Queue Management:** The system manages two types of queues - business and personal. Customers can be added to these queues based on their type.

- **Priority Management:** Customers in the personal queue are assigned priorities based on their queue number. The lower the queue number, the higher the priority.

- **Service Desk Management:** There are two service desks available. Each service desk can call the next customer based on their priority.

- **Text-to-Speech Announcements:** When a customer is called to a service desk, the system generates a dynamic text-to-speech announcement with the customer's queue number and the service desk number.

## Dependencies

- `tkinter`: The standard Python interface to the Tk GUI toolkit.
- `playsound`: A Python library to play sound files.
- `threading`: A built-in Python module for concurrent execution.
- `time`: A built-in Python module for time-related functions.
- `gtts`: Google Text-to-Speech, a Python library and CLI tool to interface with Google Text-to-Speech API.

## Note

- The program uses Google Text-to-Speech to generate announcements. Please make sure you have an active internet connection to utilize this feature.

- This program is a simplified simulation and can be used as a starting point for more advanced queue management systems.

- For any issues, improvements, or suggestions, feel free to contribute to the code or contact the developer.

---
