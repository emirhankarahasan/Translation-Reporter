import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# CSV dosyasını oku
def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Çeviri durumunu say
def count_translation_status(translations):
    total_count = len(translations)
    missing_count = sum(1 for row in translations if not row['translation'])  # 'translation' alanı çevirisi olmayan satırlar
    completed_count = total_count - missing_count
    return total_count, completed_count, missing_count

# İlerleme durumu görselleştirmesini göster
def show_progress(total, completed, missing):
    root = tk.Tk()
    root.title("Translation Progress")

    # İlerleme bilgisi
    progress = tk.Label(root, text=f"Completed: {completed}/{total} translations")
    progress.pack()

    # Pie chart
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie([completed, missing], labels=['Completed', 'Missing'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Daire şeklinde çizen eşit oranlar

    # Matplotlib Canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()

# Dosya seçim ekranı
def browse_file():
    file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        translations = read_csv(file_path)
        total, completed, missing = count_translation_status(translations)
        
        # Durum grafiklerini ve ilerlemeyi göster
        show_progress(total, completed, missing)

# Tkinter GUI
root = tk.Tk()
root.title("Translation Reporter")

browse_button = tk.Button(root, text="Browse CSV File", command=browse_file)
browse_button.pack(pady=20)

root.mainloop()
