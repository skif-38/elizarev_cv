import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from skimage import measure
from scipy.optimize import linear_sum_assignment

path = Path('out')
files = sorted(path.glob('*.npy'))

def get_center(image, label):
    center = np.argwhere(image == label).mean(axis=0)
    return center

def get_all_centers(file_path):
    data = np.load(file_path)
    labeled = measure.label(data)
    centers = []
    for label in sorted(np.unique(labeled))[1:]:
        center = get_center(labeled, label)
        centers.append(center)
    return np.array(centers)

def distance(p1, p2):
    return ((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2)**0.5

def get_distances(points1, points2):
    distances = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            distances[i, j] = distance(points1[i], points2[j])
    return distances

trajectories = [[], [], []]
prev_positions = None
speeds = np.zeros((3, 2))

for i, file_path in enumerate(files):
    curr_positions = get_all_centers(file_path)
    
    if i == 0:
        prev_positions = curr_positions
        for j in range(3):
            trajectories[j].append(prev_positions[j])
        continue
    
    predicted_pos = prev_positions + speeds
    dist_matrix = get_distances(predicted_pos, curr_positions)
    
    old_idx, new_idx = linear_sum_assignment(dist_matrix)
    new_centers = np.zeros((3, 2))
    
    for old, new in zip(old_idx, new_idx):
        found = curr_positions[new]
        dist = distance(found, prev_positions[old])
        
        if dist > 35 and i > 5:
            new_pos = prev_positions[old] + speeds[old]
        else:
            new_pos = found
        
        speeds[old] = new_pos - prev_positions[old]
        trajectories[old].append(new_pos)
        new_centers[old] = new_pos
    
    prev_positions = new_centers

plt.figure(figsize=(10, 10))
colors = ['red', 'blue', 'green']

for j in range(3):
    traj = np.array(trajectories[j])
    plt.plot(traj[:, 1], traj[:, 0], color=colors[j], 
            marker='o', markersize=2, alpha=0.7,
            linewidth=1, label=f'Ball {j}')

plt.gca().invert_yaxis()
plt.legend()
plt.show()