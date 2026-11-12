import io
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pymupdf
from pptx import Presentation
from pptx.util import Inches


class PDFToPPTXApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to PPTX Converter")
        self.root.geometry("520x220")
        self.root.resizable(False, False)

        self.pdf_path = ""
        self.status_var = tk.StringVar(value="No file selected")

        tk.Label(
            root,
            text="PDF Floor Plan to PowerPoint Converter",
            font=("Segoe UI", 13, "bold"),
        ).pack(pady=(18, 10))

        tk.Button(
            root,
            text="1. Select PDF File",
            font=("Segoe UI", 10),
            width=22,
            command=self.select_pdf,
        ).pack(pady=5)

        tk.Label(
            root,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            fg="#333333",
            wraplength=480,
        ).pack(pady=6)

        self.convert_btn = tk.Button(
            root,
            text="2. Convert to PPTX",
            font=("Segoe UI", 10, "bold"),
            width=22,
            state=tk.DISABLED,
            command=self.convert_to_pptx,
        )
        self.convert_btn.pack(pady=10)

    def select_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select a PDF File",
            filetypes=[("PDF Files", "*.pdf")],
        )
        if file_path:
            self.pdf_path = file_path
            self.status_var.set(f"Selected: {os.path.basename(file_path)}")
            self.convert_btn.config(state=tk.NORMAL)

    def convert_to_pptx(self):
        if not self.pdf_path:
            return

        try:
            self.convert_btn.config(state=tk.DISABLED)
            self.status_var.set("Converting pages at 200 DPI... Please wait.")
            self.root.update_idletasks()

            doc = pymupdf.open(self.pdf_path)
            prs = Presentation()
            blank_layout = prs.slide_layouts[6]

            # Match PowerPoint slide aspect ratio to the first PDF page
            first_rect = doc[0].rect
            slide_width = Inches(13.333)
            slide_height = Inches(13.333 * (first_rect.height / first_rect.width))
            prs.slide_width = slide_width
            prs.slide_height = slide_height

            for page_index in range(len(doc)):
                page = doc.load_page(page_index)
                pix = page.get_pixmap(dpi=200)
                img_stream = io.BytesIO(pix.tobytes("png"))

                slide = prs.slides.add_slide(blank_layout)
                slide.shapes.add_picture(
                    img_stream, 0, 0, width=slide_width, height=slide_height
                )

            output_path = os.path.splitext(self.pdf_path)[0] + ".pptx"
            prs.save(output_path)
            doc.close()

            self.status_var.set(f"Saved: {os.path.basename(output_path)}")
            messagebox.showinfo(
                "Conversion Complete",
                f"Converted {len(prs.slides)} pages!\n\nSaved to:\n{output_path}",
            )
        except Exception as e:
            self.status_var.set("Conversion failed.")
            messagebox.showerror("Error", f"Failed to convert PDF:\n{e}")
        finally:
            self.convert_btn.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToPPTXApp(root)
    root.mainloop()
