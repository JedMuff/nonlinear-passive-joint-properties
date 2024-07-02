import mujoco, mujoco_viewer, os
from moviepy.editor import ImageSequenceClip

import numpy as np

from passive_joint_function import get_passive_force

##### Input parameters #####
record_gif=True
settings = ["right", "mid", "mid2", "mid3", "left", "leftist"]
#####

with open("joint.xml", 'r') as file:
    XML = file.read()

# Get Mujoco model and Data
model = mujoco.MjModel.from_xml_string(XML, dict())
data = mujoco.MjData(model)

def mjcb_passive_callback(model, data):
    joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "passive_joint")
    data.qfrc_passive[joint_id] = get_passive_force(data.qpos[joint_id] , data.qvel[joint_id])

# Setup Viewer
if not(record_gif):
    viewer = mujoco_viewer.MujocoViewer(model, data, 'window', hide_menus=True)
    viewer.cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
    viewer.cam.fixedcamid = 0
else:
    viewer = mujoco_viewer.MujocoViewer(model, data, 'offscreen')

###
for setting in settings:
    # Configure testing parameters: starting_angle and poke_action
    if setting == "right":
        starting_angle = -21*np.pi/180
        poke_action = [0,0]
    elif setting == "mid":
        starting_angle = 0
        poke_action = [1.0,0]
    elif setting == "mid2":
        starting_angle = 0
        poke_action = [5,0]
    elif setting == "mid3":
        starting_angle = 0
        poke_action = [10,0]
    elif setting == "left":
        starting_angle = 70*np.pi/180
        poke_action = [0,0.75]
    elif setting == "leftist":
        starting_angle = 135*np.pi/180
        poke_action = [0,2.3]

    # Setting initial pose
    data.qpos[0] = starting_angle

    # Simulate and Render
    imgs = []
    for i in range(200):
        data.ctrl[:] = poke_action # Applying action

        # Simulating
        mujoco.set_mjcb_passive(mjcb_passive_callback)
        mujoco.mj_step(model, data)

        # Rendering
        if record_gif:
            img = viewer.read_pixels(camid=0)
            imgs.append(img)
        else:
            viewer.render()

    # Reset sim
    mujoco.mj_resetData(model, data)
    mujoco.mj_forward(model, data)

    # Save GIF
    if record_gif:
        if not os.path.exists("./gifs"):
            os.makedirs("./gifs")
            
        clip = ImageSequenceClip(list(imgs[::3]), fps=1)
        clip.write_gif("./gifs/"+setting+".gif", fps=1)