import numpy as np

# Defining somem function for the passive force
def get_passive_force(joint_pos, Joint_vel):
    if joint_pos < -10*np.pi/180:
        return 0
    elif joint_pos >= -30*np.pi/180 and joint_pos < 30*np.pi/180:
        return -joint_pos*500 - 100*Joint_vel
    elif joint_pos >= 30*np.pi/180 and joint_pos < 135*np.pi/180:
        np.sin(joint_pos)
        return -41.5*np.sin(joint_pos) - 100*Joint_vel
    elif joint_pos >= 135*np.pi/180:
        return -100 - 100*Joint_vel
    else:
        print("angle out of ang")