import tkinter as tk
from tkinter import filedialog
from tkhtmlview import HTMLLabel
import markdown
import ttkbootstrap as tb

class MarkdownEditor(tb.Window):
    def __init__(self):
        super().__init__(themename="cosmo")
        self.title("Markdown Journal")
        self.geometry("800x600")

        self.text_area = tk.Text(self, wrap="word", font=("Segoe UI", 12))
        self.text_area.pack(fill="both", expand=True)

        btn_frame = tb.Frame(self)
        btn_frame.pack(fill="x")

        tb.Button(btn_frame, text="Open", command=self.open_file).pack(side="left")
        tb.Button(btn_frame, text="Save", command=self.save_file).pack(side="left")
        tb.Button(btn_frame, text="Preview", command=self.show_preview).pack(side="left")
        tb.Button(btn_frame, text="Edit Mode", command=self.show_editor).pack(side="left")

        self.preview_label = None
        self.file_path = None

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, f.read())

    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                                          filetypes=[("Markdown Files", "*.md")])
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", tk.END))

    def show_preview(self):
        md_text = self.text_area.get("1.0", tk.END)
        html_content = markdown.markdown(md_text)

        if self.preview_label:
            self.preview_label.destroy()

        self.text_area.pack_forget()
        self.preview_label = HTMLLabel(self, html=html_content)
        self.preview_label.pack(fill="both", expand=True)

    def show_editor(self):
        if self.preview_label:
            self.preview_label.destroy()
        self.text_area.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MarkdownEditor()
    app.mainloop()
