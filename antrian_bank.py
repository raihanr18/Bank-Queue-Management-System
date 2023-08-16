import tempfile
import os
import tkinter as tk
from playsound import playsound
import threading
import time
from gtts import gTTS

PRIMARY_COLOR = "#3498db"
SECONDARY_COLOR = "#e74c3c"
BACKGROUND_COLOR = "#ecf0f1"
TEXT_COLOR = "#2c3e50"
BUTTON_COLOR = "#2ecc71"

class HeapNode:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        node = HeapNode(item, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.heap:
            self._swap(0, len(self.heap) - 1)
            node = self.heap.pop()
            self._heapify_down(0)
            return node.item
        return None

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index].priority > self.heap[index].priority:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index].priority < self.heap[smallest].priority:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index].priority < self.heap[smallest].priority:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

class BankQueueApp:
    def __init__(self):
        self.queue = MinHeap()
        self.next_number = 1
        self.personal_queue = []

        self.root = tk.Tk()
        self.root.title("Aplikasi Antrian Bank")
        self.root.configure(bg=BACKGROUND_COLOR)

        self.label_meja1 = self.create_label("Meja 1:", 20, TEXT_COLOR)
        self.label_meja1.pack(pady=10)
        
        self.label_meja2 = self.create_label("Meja 2:", 20, TEXT_COLOR)
        self.label_meja2.pack(pady=10)
        
        self.label_next_number = self.create_label("Nomor Selanjutnya: {}".format(self.get_next_number()), 16, TEXT_COLOR)
        self.label_next_number.pack(pady=10)
        
        self.button_antrian_bisnis = self.create_button("Tambah Antrian Bisnis", 14, BUTTON_COLOR, self.tambah_antrian_bisnis)
        self.button_antrian_bisnis.pack(pady=5)
        
        self.button_antrian_personal = self.create_button("Tambah Antrian Personal", 14, BUTTON_COLOR, self.tambah_antrian_personal)
        self.button_antrian_personal.pack(pady=5)
        
        self.button_meja1 = self.create_button("Meja 1 Memanggil", 14, PRIMARY_COLOR, self.meja1_memanggil)
        self.button_meja1.pack(pady=5)
        
        self.button_meja2 = self.create_button("Meja 2 Memanggil", 14, PRIMARY_COLOR, self.meja2_memanggil)
        self.button_meja2.pack(pady=5)
        
        self.button_keluar = self.create_button("Keluar", 14, SECONDARY_COLOR, self.root.quit)
        self.button_keluar.pack(pady=10)

        self.current_meja1 = None
        self.current_meja2 = None

        self.run()

    def create_label(self, text, font_size, color):
        label = tk.Label(self.root, text=text, font=("Helvetica", font_size), fg=color, bg=BACKGROUND_COLOR)
        return label

    def create_button(self, text, font_size, color, command):
        button = tk.Button(self.root, text=text, font=("Helvetica", font_size), fg="white", bg=color, command=command)
        return button

    def set_label_text(self, label, text):
        label.config(text=text)

    def tampilan_utama(self):
        self.label_meja1 = self.create_label("Meja 1:", 20, TEXT_COLOR)
        self.label_meja1.pack(pady=10)
        
        self.label_meja2 = self.create_label("Meja 2:", 20, TEXT_COLOR)
        self.label_meja2.pack(pady=10)
        
        self.label_next_number = self.create_label("Nomor Selanjutnya: {}".format(self.get_next_number()), 16, TEXT_COLOR)
        self.label_next_number.pack(pady=10)
        
        self.button_antrian_bisnis = self.create_button("Tambah Antrian Bisnis", 14, BUTTON_COLOR, self.tambah_antrian_bisnis)
        self.button_antrian_bisnis.pack(pady=5)
        
        self.button_antrian_personal = self.create_button("Tambah Antrian Personal", 14, BUTTON_COLOR, self.tambah_antrian_personal)
        self.button_antrian_personal.pack(pady=5)
        
        self.button_meja1 = self.create_button("Meja 1 Memanggil", 14, PRIMARY_COLOR, self.meja1_memanggil)
        self.button_meja1.pack(pady=5)
        
        self.button_meja2 = self.create_button("Meja 2 Memanggil", 14, PRIMARY_COLOR, self.meja2_memanggil)
        self.button_meja2.pack(pady=5)
        
        self.button_keluar = self.create_button("Keluar", 14, SECONDARY_COLOR, self.root.quit)
        self.button_keluar.pack(pady=10)

    def get_next_number(self):
        if self.queue.heap:
            return self.queue.heap[0].item
        return self.next_number

    def tambah_antrian_bisnis(self):
        antrian = "B{:03d}".format(self.next_number)
        self.queue.push(antrian, -1)
        self.set_label_text(self.label_next_number, "Nomor Selanjutnya: {}".format(self.get_next_number()))
        self.next_number += 1

    def tambah_antrian_personal(self):
        antrian = "P{:03d}".format(self.next_number)
        self.queue.push(antrian, self.get_priority(antrian))  
        self.set_label_text(self.label_next_number, "Nomor Selanjutnya: {}".format(self.get_next_number()))
        self.next_number += 1

    def meja1_memanggil(self):
        if self.current_meja1 is None:
            if self.queue.heap:
                self.current_meja1 = self.queue.pop()
            elif self.personal_queue:
                self.current_meja1 = self.personal_queue.pop(0)
        else:
            if self.personal_queue:
                self.queue.push(self.current_meja1, self.get_priority(self.current_meja1))
                self.current_meja1 = self.personal_queue.pop(0)
            else:
                self.queue.push(self.current_meja1, self.get_priority(self.current_meja1))
                self.current_meja1 = None

        self.set_label_text(self.label_meja1, "Meja 1: {}".format(self.current_meja1))
        if self.current_meja1:
            self.play_dynamic_sound(self.current_meja1, meja=1)

    def meja2_memanggil(self):
        if self.current_meja2 is None:
            if self.queue.heap:
                self.current_meja2 = self.queue.pop()
            elif self.personal_queue:
                self.current_meja2 = self.personal_queue.pop(0)
        else:
            if self.personal_queue:
                self.queue.push(self.current_meja2, self.get_priority(self.current_meja2))
                self.current_meja2 = self.personal_queue.pop(0)
            else:
                self.queue.push(self.current_meja2, self.get_priority(self.current_meja2))
                self.current_meja2 = None

        self.set_label_text(self.label_meja2, "Meja 2: {}".format(self.current_meja2))
        if self.current_meja2:
            self.play_dynamic_sound(self.current_meja2, meja=2)

    def get_priority(self, antrian):
        return -1 if antrian.startswith("B") else int(antrian[1:]) + 1

    def play_dynamic_sound(self, antrian, meja):
        tts_text = "{} di meja {}".format(antrian, meja)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        temp_file.close()
        self.text_to_speech(tts_text, temp_file.name)
        self.play_sound(temp_file.name)
        time.sleep(2)
        os.remove(temp_file.name)

    def text_to_speech(self, text, output_file):
        tts = gTTS(text, lang='id')
        tts.save(output_file)

    def play_sound(self, sound_file):
        threading.Thread(target=playsound, args=(sound_file,)).start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BankQueueApp()