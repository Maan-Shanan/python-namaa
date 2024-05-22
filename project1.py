# استيراد مكتبات البايثون المطلوبة
import tkinter as tk
from tkinter import ttk
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display
import os

# إنشاء النافذة
window = tk.Tk()
window.title("برنامج محل تصليح الأدوات الكهربائية")
window.geometry("800x600")

# إنشاء مربع الإدخال لرقم الهاتف
phone_label = tk.Label(window, text="رقم الهاتف:")
phone_label.pack(fill=tk.X)
phone_entry = tk.Entry(window)
phone_entry.pack(fill=tk.X)

# إنشاء القائمة المنسدلة لاختيار الآلة
machine_label = tk.Label(window, text="اختر الآلة:")
machine_label.pack(fill=tk.X)
machine_var = tk.StringVar()
machine_combobox = ttk.Combobox(window, textvariable=machine_var)
machine_combobox['values'] = ('آلة 1', 'آلة 2', 'آلة 3')
machine_combobox.pack(fill=tk.X)

# إنشاء مربع الإدخال لتاريخ اليوم
date_label = tk.Label(window, text="تاريخ اليوم:")
date_label.pack(fill=tk.X)
date_entry = tk.Entry(window)
date_entry.insert(0, date.today())
date_entry.pack(fill=tk.X)

# إنشاء الزر لطباعة المعلومات
def print_info():
    phone = phone_entry.get()
    machine = machine_var.get()
    date = date_entry.get()

    # إنشاء مستند PDF جديد
    pdf = canvas.Canvas("info.pdf")

    # تحميل الخط العربي
    pdfmetrics.registerFont(TTFont('Arabic', 'arial.ttf'))

    # تحويل النص العربي إلى الشكل الصحيح
    reshaped_text_phone = arabic_reshaper.reshape(f"رقم الهاتف: {phone}")
    bidi_text_phone = get_display(reshaped_text_phone)
    
    reshaped_text_machine = arabic_reshaper.reshape(f"الآلة: {machine}")
    bidi_text_machine = get_display(reshaped_text_machine)
    
    reshaped_text_date = arabic_reshaper.reshape(f"التاريخ: {date}")
    bidi_text_date = get_display(reshaped_text_date)

    # إضافة النص
    pdf.setFont('Arabic', 12)
    pdf.drawString(100, 750, bidi_text_phone)
    pdf.drawString(100, 730, bidi_text_machine)
    pdf.drawString(100, 710, bidi_text_date)

    # حفظ الملف
    pdf.save()

    # فتح الملف
    os.system("info.pdf")

print_button = tk.Button(window, text="طباعة المعلومات", command=print_info)
print_button.pack()

# بدء الحلقة الرئيسية للنافذة
window.mainloop()
