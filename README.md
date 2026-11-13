# PDF to PowerPoint Converter

A simple desktop application that converts PDF floor plans into editable PowerPoint presentations with proper slide dimensions based on the original PDF page aspect ratio.

---

## ✨ Features

- **PDF to PPTX Conversion** - Converts pages from any PDF document into individual PowerPoint slides
- **Smart Dimensions** - Automatically adjusts PowerPoint slide dimensions to match the PDF page aspect ratio
- **High-Quality Output** - Uses 200 DPI resolution for crisp images on each slide
- **User-Friendly GUI** - Clean, intuitive interface built with Tkinter
- **One-Pass Conversion** - Handles multiple pages in a single operation

---

## 📦 Requirements

This application requires the following Python libraries:
- `pymupdf` (fitz) – For PDF reading and page image extraction
- `python-pptx` – For PowerPoint presentation creation
- `tkinter` – Included with Python for GUI support

---

## 🖥️ Installation

1. **Clone or download** the repository to your local machine.

2. **Install required packages:**
   ```bash
   pip install pymupdf python-pptx
   ```

3. *(Optional)* If you're on Ubuntu/Debian:
   ```bash
   sudo apt-get update
   sudo apt-get install -y libpango1.0-0 libreoffice libreoffice-text-to-speech
   ```

4. **Run the app** using Python 3.x (preferably 3.8+):
   ```bash
   python pdf_to_pptx.py
   ```

---

## 🧪 Usage Instructions

1. Click **"Select PDF File"** to choose a `.pdf` file from your computer.
2. The app will display the selected filename and enable the conversion button.
3. Click **"Convert to PPTX"** when ready to generate the presentation.
4. The application automatically converts each page into a slide with adjusted dimensions.
5. Once complete, click **"OK"** on the success message window. Your PowerPoint file is saved next to the original PDF file (e.g., `document.pdf` → `document.pptx`).

---

## 💡 How It Works

| Step | Action | Description |
|------|--------|-------------|
| 1 | Open PDF | Loads PDF file using pymupdf library |
| 2 | Get Dimensions | Measures the first page to set appropriate slide aspect ratio |
| 3 | Extract Pages | Converts each PDF page into a PNG image at 200 DPI |
| 4 | Create Slides | Adds an image slide per page with adjusted width/height |
| 5 | Save Output | Saves `.pptx` file to same directory as original PDF |

---

## 📊 Project Structure

```
.
├── pdf_to_pptx.py    # Main application code
├── README.md          # Project documentation
└── requirements.txt   # Dependencies (optional)
```

---

## 🐛 Troubleshooting

If you encounter any issues while using the app:

- **ImportError:** Make sure `pip install pymupdf python-pptx` was executed successfully.
- **PDF Not Found:** Ensure that `.pdf` files are being selected from your system path.
- **Slide Not Converting:** If pages aren't converting, check that the PDF has valid page structures.
- **No GUI Response:** Ensure you're using Python 3.x and not an incompatible environment like PyCharm or Anaconda (unless virtualized correctly).

---

## 📄 License

This project is released under the [MIT License](LICENSE) – feel free to use it for personal, educational, or commercial purposes.

---

## 👨‍💻 Author

Name: Ahmad Abbas Issa
LinkedIN: www.linkedin.com/in/ahmadissa22

---

> 🌟 If this tool helps you with your workflow, consider giving this project a ⭐ on GitHub!
