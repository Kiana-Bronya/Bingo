import random
import tkinter as tk
from tkinter import messagebox

class BingoHostSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ビンゴの司会システム")
        self.root.geometry("400x300")

        # ボタンの作成
        self.draw_button = tk.Button(self.root, text="数字を引く", command=self.draw_number)
        self.draw_button.pack(pady=10)

        # 現在の数字を表示するラベル
        self.current_number_label = tk.Label(self.root, text="現在の数字: ")
        self.current_number_label.pack(pady=10)

        # 履歴を表示するテキストボックス
        self.history_text = tk.Text(self.root, height=10, width=40, state='disabled')
        self.history_text.pack(pady=10)

        # 抽選された数字を保持するリスト
        self.drawn_numbers = []

    def draw_number(self):
        if len(self.drawn_numbers) >= 75:
            messagebox.showinfo("終了", "全ての数字が既に抽選されました！")
            return

        new_number = random.randint(1, 75)
        while new_number in self.drawn_numbers:
            new_number = random.randint(1, 75)

        # 新しい数字をリストに追加
        self.drawn_numbers.append(new_number)

        # ラベルと履歴を更新
        self.current_number_label.config(text=f"現在の数字: {new_number}")

        # 履歴を更新するためにTextウィジェットの状態を変更
        self.history_text.config(state='normal')
        self.history_text.insert(tk.END, f"{new_number}, ")
        self.history_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoHostSystem(root)
    root.mainloop()
