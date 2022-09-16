# sd-concepts-library-stable-diffusion-conceptualizer-getter
This short script will grab the current list of sd-concepts-library/stable-diffusion-conceptualizer concepts and drop them into a directory you specify
https://huggingface.co/spaces/sd-concepts-library/stable-diffusion-conceptualizer

The script renames the file to the model_name and gives it an extension of .pt instead of .bin 
This was designed to be used with https://github.com/AUTOMATIC1111/stable-diffusion-webui

You will need to run ` huggingface-cli login` before running thi script, and have your HuggingFace token ready

TODO
* Check if the file and hash are not already present in the folder
* Probably some others issues that will need to be fixed
