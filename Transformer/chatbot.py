from transformers import AutoModel,AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(input_text):
  input = tokenizer.encode(input_text, return_tensors="pt")
  output = model.generate(input, max_length=50, num_return_sequences=1)
  response = tokenizer.decode(output[0], skip_special_tokens=True)
  return response