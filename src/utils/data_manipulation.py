# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from tqdm import tqdm

# Functions
def get_frame_number(frame_path):
    frame_suffix = frame_path.split('_')[-1]
    frame_number_split = frame_suffix.split('.')
    frame_number_str = '.'.join(frame_number_split[:-1])
    return int(float(frame_number_str))

def get_frame(frame_path):
    frame = list()
    with open(frame_path) as f:
        # Read comment line
        line = f.readline()
        while line:
            line = f.readline()
            line_split = line.strip().split(' ')
            if len(line_split) > 1:
                pedestrian = {'frame': get_frame_number(frame_path),
                              'pedestrianID': int(line_split[0]),
                              'x': float(line_split[1]),
                              'y': float(line_split[2])}
                frame.append(pedestrian)

    df = pd.DataFrame(frame)
    return df

# Directories
# Input and output parent directories
input_dir = './data/inputs/'
output_dir = './data/outputs/'
# Activation paths
activation_path  = input_dir + 'activation.dat'
output_activation_path = output_dir + 'activation.csv'
# Frames paths
frames_dir = input_dir + 'frames/'
output_frames_dir = output_dir + 'frames/'
if not os.path.exists(output_frames_dir):
    os.makedirs(output_frames_dir)
# Frames paths
frame_files = [f for f in os.listdir(frames_dir) if f.endswith('.dat')]
frame_paths = [frames_dir + f for f in frame_files]
# Change .dat to .csv for outputs
output_frame_files = [f[:-4] + '.csv' for f in frame_files]
output_frame_paths = [output_frames_dir + f for f in output_frame_files]
# Combined frames data
total_frames_path = output_dir + 'combined_frames.csv'


# Read in data
activations = pd.read_csv(activation_path, sep=' ')
frames = [get_frame(frame_path) for frame_path in frame_paths]

# Data modifications
# Remove unnecessary columns from activations
activations = activations.loc[:, ['pedestrianID', 'time_activation', 'gate_in', 'gate_out']]

# Join frames into single dataframe
df = pd.concat(frames)

# Write out data
# Activation rates
print('Outputting activation data...')
activations.to_csv(output_activation_path, index=False)
# Individual frames
print('Outputting individual frames...')
for i, frame in enumerate(tqdm(frames)):
    frame.to_csv(output_frame_paths[i], index=False)
# Collective frames
print('Outputting collected frames...')
df.to_csv(total_frames_path, index=False)
