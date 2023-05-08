import os
import platform
import subprocess
import sys

def check_ram():
    if platform.system() == "Windows":
        try:
            total_memory = int(subprocess.check_output("wmic OS get TotalVisibleMemorySize /Value", shell=True).decode('utf-8').strip().split('=')[-1]) // 1024
        except Exception as e:
            print("Failed to get total RAM:", e)
            total_memory = 0
    elif platform.system() == "Linux":
        try:
            with open('/proc/meminfo', 'r') as meminfo:
                total_memory = int(meminfo.readline().split()[1]) // 1024
        except Exception as e:
            print("Failed to get total RAM:", e)
            total_memory = 0
    else:
        print("Unsupported operating system.")
        total_memory = 0

    return total_memory

def install_vicuna():
    # Install FastChat
    subprocess.run([sys.executable, "-m", "pip", "install", "fschat"])

    # Clone FastChat repository and navigate to the FastChat folder
    subprocess.run(["git", "clone", "https://github.com/lm-sys/FastChat.git"])
    os.chdir("FastChat")

    # Install the package
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."])

    # Download LLaMA weights and apply delta to obtain Vicuna-7B weights
    print("Download LLaMA weights and follow instructions to obtain Vicuna-7B weights.")
    print("Apply delta to the LLaMA weights using the low CPU memory conversion method.")
    
    base_model_path = input("Enter the path to LLaMA-7B weights: ")
    target_model_path = input("Enter the output path for Vicuna-7B weights: ")
    delta_path = "lmsys/vicuna-7b-delta-v1.1"

    subprocess.run([sys.executable, "-m", "fastchat.model.apply_delta",
                    "--base-model-path", base_model_path,
                    "--target-model-path", target_model_path,
                    "--delta-path", delta_path,
                    "--low-cpu-mem"])

    print("Vicuna-7B model is ready.")
    print("Run the following command to use the model:")
    print(f"python3 -m fastchat.serve.cli --model-path {target_model_path} --device cpu")


def main():
    total_memory = check_ram()

    if total_memory >= 30 * 1024:
        print("Your system has sufficient RAM to load the Vicuna-7B model.")
        install_vicuna()
    else:
        print("Your system does not have enough RAM to load the Vicuna-7B model.")
        print("Consider upgrading your system to use the Vicuna-13B model, which requires around 60GB of CPU memory.")


if __name__ == "__main__":
    main()
