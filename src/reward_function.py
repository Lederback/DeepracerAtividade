def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    steps = params['steps']
    track_width = params['track_width']
    
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.75 * track_width

    MAX_SPEED = 4.0
    MIN_SPEED = 1.0
    SPEED_THRESHOLD = 0.5

    max_steps = 250
    
    reward = -0.05

    if steps < max_steps and progress >= 90:
        reward += 2.0
    
    if MIN_SPEED < speed < MAX_SPEED - SPEED_THRESHOLD:
        reward += 0.1
    elif speed < MIN_SPEED:
        reward -= 0.5
    elif speed > MAX_SPEED:
        reward -= 0.5

    if steps >= max_steps:
        reward -= 2.0

    if not all_wheels_on_track:
        reward -= 5.0
    
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward -= 0.05
    
    return float(reward)