import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
import random
import os

class SensorDataset(Dataset):
    def __init__(self, file_paths):
        self.data = []
        self.sample_indices = []
        valid_files = [file for file in file_paths if os.path.exists(file)]
        
        if not valid_files:
            raise FileNotFoundError("No valid CSV files found. Check the directory path.")
        
        sample_counter = 1
        for file in valid_files:
            df = pd.read_csv(file, header=None)  
            sensor_data = df.values  
            self.data.append(sensor_data)
            self.sample_indices.extend(range(sample_counter, sample_counter + sensor_data.shape[0]))
            sample_counter += sensor_data.shape[0]
        
        self.data = np.concatenate(self.data, axis=0)  
        self.data = torch.tensor(self.data, dtype=torch.float32)
        self.sample_indices = np.array(self.sample_indices)
        
        self.remaining_indices = np.arange(len(self.data))
        np.set_printoptions(precision=2, suppress=True, threshold=10)  

    def __len__(self):
        return len(self.data)

    def length(self):
        return len(self.data)

    def __getitem__(self, idx):
        if idx >= len(self.data):
            raise IndexError("Index out of range")
        return self.sample_indices[idx], self.data[idx]  

    def get_random_item(self):
        if len(self.remaining_indices) == 0:
            raise ValueError("No remaining samples left. Please reset the dataset.")
        
        chosen_idx = random.choice(self.remaining_indices)
        self.remaining_indices = np.setdiff1d(self.remaining_indices, [chosen_idx])
        
        return self.sample_indices[chosen_idx], self.data[chosen_idx]
    
    def reset_samples(self):
        self.remaining_indices = np.arange(len(self.data))


def get_data_loader(file_paths, batch_size):
    dataset = SensorDataset(file_paths)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)

if __name__ == "__main__":
    base_path = "/Users/aravindbala/Desktop/research/vib/"
    file_names = [
        "p1l1_vib.csv", "p1l2_vib.csv", "p2l1_vib.csv", "p2l2_vib.csv",
        "p3l1_vib.csv", "p3l2_vib.csv", "p4l1_vib.csv", "p4l2_vib.csv",
        "p5l1_vib.csv", "p5l2_vib.csv", "p6l1_vib.csv", "p6l2_vib.csv"
    ]
    file_paths = [os.path.join(base_path, f) for f in file_names]
    
    dataset = SensorDataset(file_paths)
    batch_size = 32
    data_loader = get_data_loader(file_paths, batch_size)
    
    while True:
        user_input = input("\nEnter 'get' for a random sample or number of samples to display (or 'exit' to quit): ").strip()
        
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "get":
            try:
                sample_id, sample = dataset.get_random_item()
                formatted_sample = np.array2string(sample.numpy(), precision=2, suppress_small=True, threshold=10)
                print(f"Random Sample {sample_id}: {formatted_sample}")
            except ValueError as e:
                print(e)
        else:
            try:
                num_samples = int(user_input)
                if num_samples < 1 or num_samples > len(dataset):
                    raise ValueError(f"Please enter a number between 1 and {len(dataset)}.")
                
                chosen_indices = np.random.choice(dataset.remaining_indices, size=num_samples, replace=False)
                dataset.remaining_indices = np.setdiff1d(dataset.remaining_indices, chosen_indices)
                
                print(f"\nDisplaying {num_samples} unique samples:")
                for idx in chosen_indices:
                    sample_id, sample = dataset[idx]
                    formatted_sample = np.array2string(sample.numpy(), precision=2, suppress_small=True, threshold=10)
                    print(f"Sample {sample_id}: {formatted_sample}")
            except ValueError as e:
                print(e)
                continue
        
        print(f"Remaining samples: {len(dataset.remaining_indices)}")
        print(f"Total dataset length: {dataset.length()}")
        
        if len(dataset.remaining_indices) == 0:
            reset_choice = input("\nAll samples have been tested. Do you want to reset? (yes/no): ").strip().lower()
            if reset_choice == "yes":
                dataset.reset_samples()
            else:
                print("Exiting program. No samples left.")
                break
