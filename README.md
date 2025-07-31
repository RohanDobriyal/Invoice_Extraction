# Invoice Extraction using Donut (Document Understanding Transformer)

This project demonstrates how to extract key fields like **invoice number**, **invoice date**, and **line items** from invoice images. It uses the [Donut model](https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa) by Naver Clova, fine-tuned for document question answering (DocVQA).

---

##  Features

- Extracts structured fields (invoice number, date, line items) from invoice images
- PDF invoices are converted into images
- Uses HuggingFace’s Donut model for question-based visual extraction
- Scalable architecture – you can add any custom question for key-value extraction

---

##  Tech Stack

- Python 3.10+
- Hugging Face Transformers
- PyMuPDF (for PDF to image conversion)
- PIL & Torch
- DonutProcessor + VisionEncoderDecoderModel

---

## Folder Structure

```

invoice\_extractor/
├── invoice\_images/        # Contains PNG images converted from invoices
├── inference/
│   └── run\_inference.py   # Main script to extract fields from images
├── convert\_pdf\_to\_images.py
├── requirements.txt
└── README.md

````

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RohanDobriyal/Invoice_Extraction.git
   cd Invoice_Extraction
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download some sample PDF invoices and place them in the root or `data/` folder.

4. Convert PDFs to images:

   ```bash
   python convert_pdf_to_images.py
   ```

5. Run inference to extract fields:

   ```bash
   cd inference
   python run_inference.py
   ```

---

## Supported Fields

* `invoice_number`: What is the invoice number?
* `invoice_date`: What is the invoice date?
* `line_items`: What are the line items listed?

You can update the `questions` dictionary in `run_inference.py` to extract any other field.

---

## Model Used

* [`naver-clova-ix/donut-base-finetuned-docvqa`](https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa)

---
## Output
<img width="1396" height="603" alt="image" src="https://github.com/user-attachments/assets/e89b0958-9646-4cdf-8010-eed3e13d63a3" />


---

Let me know if you'd like a badge version or deployment instructions as well.
```
