import torch
import time
import sys
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor
from packaging import version

# Configuration
MODELS = {
    "ZapPRO Tech (Logic)": "Qwen/Qwen2.5-14B-Instruct",
    "ZapPRO Vision (Eyes)": "Qwen/Qwen2-VL-7B-Instruct",
    "Jarvis CEO (Router)": "mistralai/Mistral-Nemo-12B-Instruct-v1"
}

def check_gpu_capabilities():
    print("--- GPU DIAGNOSTIC ---")
    if not torch.cuda.is_available():
        print("❌ CUDA not available. Running on CPU (Not recommended for production).")
        return False
    
    gpu_name = torch.cuda.get_device_name(0)
    vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"✅ GPU Detected: {gpu_name}")
    print(f"✅ VRAM Available: {vram_gb:.2f} GB")
    
    if "4090" in gpu_name:
        print("🚀 RTX 4090 confirmed. Ideal for Antigravity Stack.")
        return True
    return False

def benchmark_download_simulation():
    print("\n--- MODEL AVAILABILITY CHECK ---")
    print("Checking Hugging Face Hub connectivity and model existence...")
    
    try:
        from huggingface_hub import model_info
        for role, model_id in MODELS.items():
            print(f"📡 Checking {role} [{model_id}]...", end=" ")
            try:
                info = model_info(model_id)
                print(f"✅ FOUND (Downloads: {info.downloads})")
            except Exception as e:
                print(f"❌ ERROR: {e}")
    except ImportError:
        print("⚠️ huggingface_hub library not found. Install it to verify models online.")

def system_recommendation():
    print("\n--- OPTIMIZATION REPORT ---")
    print("Based on RTX 4090 (24GB), we recommend:")
    print("1. Use EXL2 (ExLlamaV2) quantization (4.0bpw or 4.65bpw) for ZapPRO Tech (Qwen 14B).")
    print("2. Use GPT-Fast or vLLM for serving.")
    print("3. Reserve ~10GB for Qwen 14B, ~6GB for Qwen2-VL, ~4GB for System/Context.")
    
if __name__ == "__main__":
    print("🚦 ANTIGRAVITY OS v2.1: MODEL BENCHMARK UTILITY")
    
    gpu_ready = check_gpu_capabilities()
    benchmark_download_simulation()
    
    if gpu_ready:
        system_recommendation()
        print("\n✅ READY TO INITIATE DOWNLOADS.")
    else:
        print("\n⚠️ SYSTEM NOT OPTIMIZED FOR SOTA MODELS.")
