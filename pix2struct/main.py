import requests
from PIL import Image
from transformers import Pix2StructForConditionalGeneration, Pix2StructProcessor
import warnings

warnings.filterwarnings("ignore")

image_url = "./testimage.jpg"
image = Image.open(image_url)

# model = Pix2StructForConditionalGeneration.from_pretrained("google/pix2struct-ai2d-base")
# model.save_pretrained("./model")
model = Pix2StructForConditionalGeneration.from_pretrained("./model")
# processor = Pix2StructProcessor.from_pretrained("google/pix2struct-ai2d-base")
# processor.save_pretrained("./processor")
processor = Pix2StructProcessor.from_pretrained("./processor")
question = "what is being discussed in this section?"
question1 = "where to find the model?"

inputs1 = processor(images=image, text=question, return_tensors="pt")
inputs2 = processor(images=image, text=question1, return_tensors="pt")

predictions = model.generate(**inputs1)

print(processor.decode(predictions[0], skip_special_tokens=True))

predictions1 = model.generate(**inputs2)

print(processor.decode(predictions1[0], skip_special_tokens=True))
