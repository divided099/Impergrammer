import os
import platform
try:
    from transformers import pipeline
except ImportError:
    os.system("pip install transformers")
    os.system("pip3 install transformers")
    os.system("pip install pipeline")
    os.system("pip3 install pipeline")

banner = '''
 ___
|_ _|_ __ ___  _ __   ___ _ __ __ _ _ __ __ _ _ __ ___  _ __ ___   ___ _ __
 | || '_ ` _ \| '_ \ / _ | '__/ _` | '__/ _` | '_ ` _ \| '_ ` _ \ / _ | '__|
 | || | | | | | |_) |  __| | | (_| | | | (_| | | | | | | | | | | |  __| |
|___|_| |_| |_| .__/ \___|_|  \__, |_|  \__,_|_| |_| |_|_| |_| |_|\___|_|
              |_|             |___/
'''

def banner():
    print(f"{banner}\n")

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear()
banner()

def paraphrase_text(input_text):
    generator = pipeline(task="text2text-generation", model="t5-small", tokenizer="t5-small")
    paraphrased_text = generator(f"paraphrase: {input_text}", max_length=100, do_sample=True, temperature=0.7)[0]['generated_text']
    return paraphrased_text.strip()

def main():
    file_name = "Data.txt"
    try:
        with open(file_name, 'r') as file:
            original_text = file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' Not Found.")
        return
    except Exception as e:
        print(f"Error Occurred While Reading The File: {e}")
        return

    while True:
        try:
            user_input = input("Text To Rephrase: ")
            if user_input == "" or user_input == " " or user_input == "99":
                clear()
                break
            elif user_input == "clear" or user_input == "cls":
                clear()
            paraphrased_text = paraphrase_text(user_input)
            if paraphrase_text == "clear":
                clear()
                banner()
            else:
                print("\nParaphrased Text:")
                print(f"{paraphrased_text}\n")
        except KeyboardInterrupt:
            clear()
            exit()

if __name__ == "__main__":
    main()