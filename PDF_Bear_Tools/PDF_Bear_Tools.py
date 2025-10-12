from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path, pages_per_part=30):
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    parts = (total_pages + pages_per_part - 1) // pages_per_part

    for i in range(parts):
        writer = PdfWriter()
        start = i * pages_per_part
        end = min(start + pages_per_part, total_pages)
        for page in range(start, end):
            writer.add_page(reader.pages[page])

        output_filename = f"{file_path.replace('.pdf', '')}_part_{i+1}.pdf"
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)
        print(f"Processed: {output_filename} ({end-start} pages)")





