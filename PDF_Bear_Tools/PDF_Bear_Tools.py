from PyPDF2 import PdfReader, PdfWriter
import argparse

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
        
        write_pdf(file_path, f"_part_{i+1}", writer, f"({end-start} pages)")

def excerpt_pages_from_pdf(file_path, start_page, end_page):
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    
    if start_page < 0 or end_page > total_pages or start_page >= end_page:
        print(f"Error: Page range ({start_page+1}-{end_page}) is invalid. The file contains {total_pages} pages.")
        return
    
    writer = PdfWriter()
    for page in range(start_page, end_page):
        writer.add_page(reader.pages[page])
    
    write_pdf(file_path, f"_excerpt_{start_page+1}_to_{end_page}", writer, f"({end_page-start_page} pages)")

def write_pdf(file_path, filename_suffix, pdf_writer : PdfWriter, additional_info):
    output_filename = f"{file_path.replace('.pdf', '')}{filename_suffix}.pdf"
    with open(output_filename, "wb") as output_file:
        pdf_writer.write(output_file)
    print(f"Processed: {output_filename} {additional_info}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Bear Tools - operations on PDF files")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # split_pdf
    split_parser = subparsers.add_parser("split", help="Split PDF into parts")
    split_parser.add_argument("file_path", help="Path to PDF file")
    split_parser.add_argument("--pages_per_part", type=int, default=30, help="Number of pages per part (default 30)")

    # excerpt_pages_from_pdf
    excerpt_parser = subparsers.add_parser("excerpt", help="Extract a range of pages from PDF")
    excerpt_parser.add_argument("file_path", help="Path to PDF file")
    excerpt_parser.add_argument("start_page", type=int, help="Start page number (starting from 1)")
    excerpt_parser.add_argument("end_page", type=int, help="End page number (starting from 1)")

    args = parser.parse_args()

    if args.command == "split":
        split_pdf(args.file_path, args.pages_per_part)
    elif args.command == "excerpt":
        # Convert page numbering from 1-based to 0-based
        excerpt_pages_from_pdf(args.file_path, args.start_page - 1, args.end_page)

