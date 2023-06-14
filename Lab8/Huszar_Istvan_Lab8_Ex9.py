from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


class PDFManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Manager")

        self.merge_button = Button(self.root, text="Merge", command=self.merge_files)
        self.merge_button.pack(pady=10)

        self.split_button = Button(self.root, text="Split", command=self.split_file)
        self.split_button.pack(pady=10)

    def merge_files(self):
        file_paths = filedialog.askopenfilenames(title="Selectați fișierele PDF pentru unire",
                                                 filetypes=[("Fișiere PDF", "*.pdf")])

        if file_paths:
            merger = PdfFileMerger()

            for file_path in file_paths:
                merger.append(file_path)

            save_path = filedialog.asksaveasfilename(title="Salvați fișierul de ieșire", defaultextension=".pdf",
                                                     filetypes=[("Fișiere PDF", "*.pdf")])

            if save_path:
                merger.write(save_path)
                merger.close()
                messagebox.showinfo("Complet", "Fișierele PDF au fost unite cu succes!")

    def split_file(self):
        file_path = filedialog.askopenfilename(title="Selectați fișierul PDF pentru împărțire",
                                               filetypes=[("Fișiere PDF", "*.pdf")])

        if file_path:
            pdf = PdfFileReader(file_path)
            num_pages = pdf.getNumPages()

            page_start = simpledialog.askinteger("Split", "Introduceți pagina de început (1 - {}):".format(num_pages),
                                                 minvalue=1, maxvalue=num_pages)

            if page_start:
                page_end = simpledialog.askinteger("Split",
                                                   "Introduceți pagina de sfârșit ({} - {}):".format(page_start,
                                                                                                     num_pages),
                                                   minvalue=page_start, maxvalue=num_pages)

                if page_end:
                    output_files = []

                    for page in range(page_start - 1, page_end):
                        output_pdf = PdfFileWriter()
                        output_pdf.addPage(pdf.getPage(page))

                        save_path = filedialog.asksaveasfilename(title="Salvați fișierul de ieșire",
                                                                 defaultextension=".pdf",
                                                                 filetypes=[("Fișiere PDF", "*.pdf")])

                        if save_path:
                            output_file_path = "{}_{}.pdf".format(save_path, page + 1)
                            output_files.append(output_file_path)

                            with open(output_file_path, "wb") as output_file:
                                output_pdf.write(output_file)

                    messagebox.showinfo("Complet",
                                        "Fișierul PDF a fost împărțit cu succes în: {}".format(", ".join(output_files)))


root = Tk()
app = PDFManagerApp(root)
root.mainloop()