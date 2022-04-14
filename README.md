# Photo😉
This program reads images from the addresses stated in .jsonl file, draws boxes over them using the coordinates stated in the same .jsonl file and saves the images at a particular destination folder.
## Requirements
1. Python
## Python libraries required
1. [jsonlines](https://pypi.org/project/jsonlines/)
2. [opencv](https://pypi.org/project/opencv-python/)
## How to test?
1. Download and paste the address of test.jsonl file in the python script.
2. Keep few images in a test folder, paste the addresses of those images in test.jsonl file and replace all '\\' with '_' in the addresses (Notepad can be used to edit the test.jsonl file). 
3. Change the coordinates accordingly in test.jsonl file (keep in mind that the image has been resized to 720x500 pixels in the python script).
4. Run the script.
