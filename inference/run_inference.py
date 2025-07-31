from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import os
import time

# Load model and processor
print("Loading model and processor...")
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model.eval()
print("Model loaded.")


questions = {
    "invoice_number": "What is the invoice number?",
    "invoice_date": "What is the invoice date?",
    "line_items": "What are the line items listed?"
}


def extract_field(image_path, question):
    try:
        image = Image.open(image_path).convert("RGB")
        pixel_values = processor(image, return_tensors="pt").pixel_values
        prompt = f"<s_docvqa><s_question>{question}</s_question><s_answer>"
        decoder_input_ids = processor.tokenizer(prompt, add_special_tokens=False, return_tensors="pt").input_ids
        with torch.no_grad():
            outputs = model.generate(pixel_values, decoder_input_ids=decoder_input_ids, max_length=512)
            result = processor.batch_decode(outputs, skip_special_tokens=True)[0]
            return result.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    image_dir = os.path.abspath("../invoice_images")
    if not os.path.exists(image_dir):
        print(f"Folder not found: {image_dir}")
        exit(1)

    print(f"Scanning folder: {image_dir}")
    image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(".png")])

    if not image_files:
        print("No PNG files found in folder.")
        exit(1)

    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        print(f"Processing: {image_file}")
        start = time.time()
        for field, question in questions.items():
            answer = extract_field(image_path, question)
            print(f"{field}: {answer}")
        print(f"Done in {round(time.time() - start, 2)} seconds")
