import mujoco
import numpy as np
import mujoco.viewer
import pathlib

ROOT_PATH = pathlib.Path("playground/zbot")
FEET_ONLY_FLAT_TERRAIN_XML = (
    ROOT_PATH / "xmls" / "scene_mjx_feetonly_flat_terrain.xml"
)
FEET_ONLY_ROUGH_TERRAIN_XML = (
    ROOT_PATH / "xmls" / "scene_mjx_feetonly_rough_terrain.xml"
)


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
    visualize_scene("playground/zbot/xmls/zbot_feet_only.xml")