import torch

# Check if MPS is available
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    print("MPS device is available.")
else:
    print("MPS device is not available.")
