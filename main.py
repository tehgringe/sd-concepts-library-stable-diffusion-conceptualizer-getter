import requests
import os
import gradio as gr
import wget
from diffusers import StableDiffusionPipeline
from huggingface_hub import HfApi
from transformers import CLIPTextModel, CLIPTokenizer

dest_path = '/Volumes/embeddings/'

api = HfApi()
models_list = api.list_models(author="sd-concepts-library", sort="likes", direction=-1)
models = []

print("Setting up the public library")
for model in models_list:
  model_content = {}
  model_id = model.modelId
  model_content["id"] = model_id
  embeds_url = f"https://huggingface.co/{model_id}/resolve/main/learned_embeds.bin"
  model_name = model_id.split(sep='/')[1]
  print(model_id.split(sep='/')[1], " ", embeds_url)
  try:
    print(f"Getting file...{model_id}")
    wget.download(embeds_url, out=f"{dest_path}{model_name}.pt")
  except:
    continue
