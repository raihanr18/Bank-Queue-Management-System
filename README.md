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

## Usage

1. Run the program by executing the script. Make sure you have all the required dependencies installed.

```bash
python your_program_name.py
```

2. The graphical user interface (GUI) will appear, showing the available service desks and buttons for adding customers to the queues.

3. Click the "Tambah Antrian Bisnis" button to add a business customer to the queue. Their queue number will be displayed in the "Nomor Selanjutnya" label.

4. Click the "Tambah Antrian Personal" button to add a personal customer to the queue. The customer's queue number will be generated based on priority.

5. Click the "Meja 1 Memanggil" button to call the next customer from the queue to Service Desk 1. The customer's queue number will be displayed in the "Meja 1" label, and a dynamic text-to-speech announcement will be played.

6. Click the "Meja 2 Memanggil" button to call the next customer from the queue to Service Desk 2. The customer's queue number will be displayed in the "Meja 2" label, and a dynamic text-to-speech announcement will be played.

7. The "Keluar" button can be clicked to exit the program.

## Note

- The program uses Google Text-to-Speech to generate announcements. Please make sure you have an active internet connection to utilize this feature.

- This program is a simplified simulation and can be used as a starting point for more advanced queue management systems.

- For any issues, improvements, or suggestions, feel free to contribute to the code or contact the developer.

---
