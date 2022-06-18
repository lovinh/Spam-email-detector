from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import *
from model import *


class MainActivity:
    def __init__(self) -> None:
        self.root = Tk()

        # Setting root window
        self.root.title("Spam Email Classifier")
        self.root.iconphoto(False, PhotoImage(
            "icon", file=r"E:\Learn Machine Learning\Project\Spam Email Classifier\Images\spam.png"))
        self.root.config(
            background="#17202A"
        )
        self.root.columnconfigure(0, weight=1, minsize=768)
        # Setting label
        self.lbl_title = ttk.Label(
            text="Nhập nội dung thư cần dự đoán".capitalize(),
            background="#17202A",
            foreground="#ECF0F1",
            font=("Arial", 18)
        )
        self.lbl_title.grid(
            row=1,
            column=0,
            sticky="n",
            pady=10
        )
        print(self.lbl_title.winfo_width())

        self.ent_email_subject = ttk.Entry(
            background="#ECF0F1",
            font=("UTM Aurora", 18),
            justify=LEFT,
            width=50
        )
        self.ent_email_subject.grid(
            row=2,
            column=0,
            pady=10,
        )
        self.ent_email_subject.bind("<Return>", self.key_pressed)

        self.btn_submit = ttk.Button(
            text="Dự Đoán",
            command=self.btn_click
        )
        self.btn_submit.grid(
            row=3,
            column=0,
            pady=10
        )

        self.lbl_result_title = ttk.Label(
            text="Kết quả dự đoán:".capitalize(),
            background="#17202A",
            foreground="#ECF0F1",
            font=("Arial", 25)
        )
        self.lbl_result_title.grid(
            row=4,
            column=0,
            pady=10
        )

        self.lbl_result = ttk.Label(
            text="",
            background="#17202A",
            foreground="#ECF0F1",
            font=("iCiel Gotham Ultra", 25)
        )
        self.lbl_result.grid(
            row=5,
            column=0,
            pady=20
        )

        self.model = Model_Predict()
        self.txt_pp = text_preprocessing()

    def run(self):
        self.root.mainloop()

    def get_subject(self):
        res = self.ent_email_subject.get()
        if res == "":
            messagebox.showerror(
                "Nhắc nhở", message="Bạn không được bỏ trống ô nhập liệu")
        else:
            return res

    def set_result(self, status):
        if status:
            self.lbl_result.config(
                foreground="#D35400",
                text="Spam"
            )
        else:
            self.lbl_result.config(
                foreground="#27AE60",
                text="Ham"
            )

    def btn_click(self):
        self.set_result(self.model.get_predict(
            self.txt_pp.fit_transform(self.get_subject())))

    def key_pressed(self, event):
        self.btn_click()
