from paddleocr import PaddleOCR

# Initialize the PaddleOCR instance
ocr = PaddleOCR()

# Load and recognize text in the image
result = ocr.ocr('dataset/Trial.png')

# Process the recognition result
recognized_text = []
for line in result[0]:
    line_text = ' '.join([word_info[-1] for word_info in line])
    recognized_text.append(line_text)

# Join the lines to form the final recognized text
final_text = '\n'.join(recognized_text)

print(final_text)
