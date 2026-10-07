import os
import random
import shutil

# Folder sumber
image_dir = "dataset/images"
label_dir = "dataset/labels"

# Folder tujuan
train_image_dir = "dataset/train/images"
train_label_dir = "dataset/train/labels"

val_image_dir = "dataset/val/images"
val_label_dir = "dataset/val/labels"

# Buat folder
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Ambil semua gambar
images = [
    f for f in os.listdir(image_dir)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Acak
random.shuffle(images)

# 80% train
split = int(len(images) * 0.8)

train_images = images[:split]
val_images = images[split:]

# Fungsi copy
def copy_data(files, image_destination, label_destination):
    for image in files:
        image_path = os.path.join(image_dir, image)

        # Nama label mengikuti nama gambar
        name = os.path.splitext(image)[0]
        label = name + ".txt"
        label_path = os.path.join(label_dir, label)

        # Copy gambar
        shutil.copy2(image_path, image_destination)

        # Copy label
        if os.path.exists(label_path):
            shutil.copy2(label_path, label_destination)
        else:
            print("Label tidak ditemukan:", label)


# Copy data
copy_data(train_images, train_image_dir, train_label_dir)
copy_data(val_images, val_image_dir, val_label_dir)

print("Selesai!")
print("Jumlah gambar:", len(images))
print("Train:", len(train_images))
print("Val:", len(val_images))