import tkinter as tk
from tkinter import filedialog

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("تطبيق التعديل على الصور")

        # إعداد الصفحة الأولى
        self.page1_label = tk.Label(root, text="مرحبًا بك في تطبيق التعديل على الصور!")
        self.page1_label.pack(pady=20)

        self.page1_button = tk.Button(root, text="الانتقال إلى الصفحة الثانية", command=self.show_page2)
        self.page1_button.pack()

        # زر العودة للصفحة الأولى
        self.back_button = tk.Button(root, text="العودة للصفحة الأولى", command=self.show_page1)

        # عناصر إضافية يمكن تخصيصها حسب الاحتياجات

    def show_page2(self):
        # إخفاء عناصر الصفحة الأولى
        self.page1_label.pack_forget()
        self.page1_button.pack_forget()

        # إظهار عناصر الصفحة الثانية
        self.page2_label.pack(pady=20)
        self.upload_button.pack()
        for button in self.page2_buttons:
            button.pack(pady=5)
        self.back_button.pack(side=tk.BOTTOM)

    def show_page1(self):
        # إخفاء عناصر الصفحة الثانية
        self.page2_label.pack_forget()
        self.upload_button.pack_forget()
        for button in self.page2_buttons:
            button.pack_forget()
        self.back_button.pack_forget()

        # إظهار عناصر الصفحة الأولى
        self.page1_label.pack(pady=20)
        self.page1_button.pack()

    def upload_image(self):
        # افتح نافذة لاختيار ملف الصورة
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # يمكنك هنا إجراء الإجراءات التي تحتاجها لمعالجة الصورة
            print(f"تم رفع الصورة: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
