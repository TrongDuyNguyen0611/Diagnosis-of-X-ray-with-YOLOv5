import shutil
import os
import random
import pickle

raw_folder = "/Users/mac/Creative Cloud Files/Python Project/Diagnosis_Xray/VINAI_Chest_Xray/train/train"

with open('file_list.pkl','rb') as f:
    file_list = pickle.load(f)


total_files= len(file_list) # Tổng số file có nhãn trong thư mục train
print("Tổng số file  = ", total_files)

#  Tạo sẵn thư mục này nếu chưa có
train_folder = "/Users/mac/Creative Cloud Files/Python Project/Diagnosis_Xray/VINAI_Chest_Xray/yolo_data/images/train"
val_folder = "/Users/mac/Creative Cloud Files/Python Project/Diagnosis_Xray/VINAI_Chest_Xray/yolo_data/images/val"

train_labels_folder = "/Users/mac/Creative Cloud Files/Python Project/Diagnosis_Xray/VINAI_Chest_Xray/yolo_data/lables/train"
val_labels_folder = "/Users/mac/Creative Cloud Files/Python Project/Diagnosis_Xray/VINAI_Chest_Xray/yolo_data/lables/val"


# Tạo ra index cho train, val
total_files_validation = int(0.2 * total_files) # 20% cho validation
validaiton_files = random.choices(file_list, k=total_files_validation)
print("Số bản ghi validation = " , len(validaiton_files))

# Copy images và labels to validation folder
for file in validaiton_files:
    print("Validation file ", file)
    # Copy images
    shutil.copy(os.path.join(raw_folder, file), os.path.join(val_folder, file))

    # Copy labels
    shutil.copy(os.path.join(raw_folder, file[:-3] + 'txt'), os.path.join(val_labels_folder, file[:-3] + 'txt'))


# Copy images và labels to train folder
# noinspection PyTypeChecker
for file in file_list:
    print("Train file ", file)
    # Copy images
    shutil.copy(os.path.join(raw_folder, file), os.path.join(train_folder, file))

    # Copy labels
    shutil.copy(os.path.join(raw_folder, file[:-3] + 'txt'), os.path.join(train_labels_folder, file[:-3] + 'txt'))

