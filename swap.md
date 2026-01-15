
```c
# Check infomation
sudo swapon --show

# First, clean up any existing swap
sudo swapoff -a

# Remove the old swap file (you already did this)
# Now fix the new swap file

# Fix permissions - you need chmod, not chown
sudo chmod 600 /swapfile

# If chmod doesn't work because the file might be corrupted, let's recreate it properly:
sudo rm /swapfile
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile

# Format the file as swap
sudo mkswap /swapfile

# Enable the swap
sudo swapon /swapfile

# Verify it's working
sudo swapon --show
free -h
```