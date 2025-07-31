import fitz  # PyMuPDF
import os

input_dir = "data"
output_dir = "invoice_images"
os.makedirs(output_dir, exist_ok=True)

# Loop through all PDFs in the data/ directory
for pdf_file in os.listdir(input_dir):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, pdf_file)
        doc = fitz.open(pdf_path)

        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=200)
            image_name = f"{os.path.splitext(pdf_file)[0]}_page_{i+1}.png"
            image_path = os.path.join(output_dir, image_name)
            pix.save(image_path)
            print(f"Saved: {image_path}")
