import mujoco
import numpy as np
import mujoco.viewer

def visualize_scene(xml_path):
    # Load the XML file
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

    # Create and run the viewer
    with mujoco.viewer.launch_passive(model, data) as viewer:
        # Simulate and render
        while viewer.is_running():
            # Step the simulation
            mujoco.mj_step(model, data)
            
            # Update the viewer
            viewer.sync()

if __name__ == "__main__":
    xml_path = "../resources/zbot/scene_mjx_feetonly_rough_terrain.xml"
    visualize_scene(xml_path)