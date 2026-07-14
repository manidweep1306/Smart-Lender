import os

print("Model exists:", os.path.exists("smart_lender_model.pkl"))
print("Model size:", os.path.getsize("smart_lender_model.pkl"), "bytes")