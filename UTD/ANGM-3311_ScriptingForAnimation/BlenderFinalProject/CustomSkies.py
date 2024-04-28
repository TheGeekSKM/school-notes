import bpy

import math
import random

#region Creating Nodes + Variables
def create_variables():
    world_node_tree = bpy.context.scene.world.node_tree
    world_node_tree.nodes.clear()
    
    node_location_x_step = 300
    node_location_x = 0
    
    return world_node_tree, node_location_x_step, node_location_x

def create_sky_node(world_node_tree, node_location_x_step, node_location_x):
    node_sky = world_node_tree.nodes.new(type="ShaderNodeTexSky")
    node_location_x += node_location_x_step
    return node_sky, node_location_x

def create_first_background_node(world_node_tree, node_location_x_step, node_location_x):
    world_background_node = world_node_tree.nodes.new(type="ShaderNodeBackground")
    world_background_node.inputs["Strength"].default_value = 1.0
    world_background_node.location.x = node_location_x
    node_location_x += node_location_x_step
    return world_background_node, node_location_x

def create_mix_shader_node(world_node_tree, node_location_x_step, node_location_x):
    mix_shader_node = world_node_tree.nodes.new(type="ShaderNodeMixShader")
    mix_shader_node.location.x = node_location_x
    node_location_x += node_location_x_step
    return mix_shader_node, node_location_x

def create_rgb_shader_node(world_node_tree, node_location_x_step, node_location_x):
    rgb_shader_node = world_node_tree.nodes.new(type="ShaderNodeRGB")
    rgb_shader_node.location.x = node_location_x
    node_location_x += node_location_x_step
    return rgb_shader_node, node_location_x

def create_add_node(world_node_tree, node_location_x_step, node_location_x):
    add_shader_node = world_node_tree.nodes.new(type="ShaderNodeAddShader")
    add_shader_node.location.x = node_location_x
    node_location_x += node_location_x_step
    return add_shader_node, node_location_x

def create_additional_background_node(world_node_tree, node_location_x_step, node_location_x):
    additional_background_node = world_node_tree.nodes.new(type="ShaderNodeBackground")
    additional_background_node.inputs["Strength"].default_value = 0.15
    additional_background_node.location.x = node_location_x
    node_location_x += node_location_x_step
    return additional_background_node, node_location_x

def create_musgrave_texture_node(world_node_tree, node_location_x_step, node_location_x):
    musgrave_texture_node = world_node_tree.nodes.new(type="ShaderNodeTexMusgrave")
    musgrave_texture_node.inputs["Scale"].default_value = 3.3
    musgrave_texture_node.inputs["Detail"].default_value = 10
    musgrave_texture_node.inputs["Dimension"].default_value = 0.47
    musgrave_texture_node.inputs["Vector"].default_value = [0.0, 0.0, 0.0]
    musgrave_texture_node.location.x = node_location_x
    musgrave_texture_node.location.y = node_location_x - 400
    return musgrave_texture_node, node_location_x

def create_color_ramp_node(world_node_tree, rgb_shader_node, node_location_x_step, node_location_x):
    color_ramp_node = world_node_tree.nodes.new(type="ShaderNodeValToRGB")
    color_ramp_node.color_ramp.elements[1].position = 0.824
    color_ramp_node.color_ramp.elements[1].position = 0.082
    color_ramp_node.location.x = rgb_shader_node.location.x
    color_ramp_node.location.y = rgb_shader_node.location.y - 200
    return color_ramp_node, node_location_x

def create_output_node(world_node_tree, node_location_x_step, node_location_x):
    world_output_node = world_node_tree.nodes.new(type="ShaderNodeOutputWorld")
    world_output_node.location.x = node_location_x
    return world_output_node, node_location_x
#endregion



#region Applying Configurations
def apply_sun_config(node_sky, sun_config):
    for attr, value in sun_config.items():
        if hasattr(node_sky, attr):
            print(f" {attr} set to {str(value)}")
            setattr(node_sky, attr, value)
        else:
            print("\t warning: %s is not an attribute of ShaderNodeTexSky node", attr)
            
def apply_color_config(rgb_shader_node, mix_shader_node, color_config):
    print("Updating Color Data")
    color_value = color_config["sky_color"]
    mix_factor = color_config["mix_factor"]
    rgb_shader_node.outputs[0].default_value = color_value
    mix_shader_node.inputs[0].default_value = mix_factor
    print(f"Color Value: {color_value}")
    print(f"Mix Factor: {mix_factor}")
    
def apply_cloud_config(musgrave_texture_node, color_ramp_node, additional_background_node, cloud_config):
    cloud_size = cloud_config["cloud_size"]
    cloud_vector = cloud_config["cloud_vector"]
    cloud_opacity = cloud_config["cloud_opacity"]
    cloud_intensity = cloud_config["cloud_intensity"]
    cloud_color = cloud_config["cloud_color"]
    
    musgrave_texture_node.inputs["Scale"].default_value = cloud_size
    musgrave_texture_node.inputs["Vector"].default_value = cloud_vector
    color_ramp_node.color_ramp.elements[1].position = (1 - cloud_opacity)
    additional_background_node.inputs["Strength"].default_value = cloud_intensity
    color_ramp_node.color_ramp.elements[1].color = cloud_color
    
    print(f"Cloud Size: {cloud_size}")
    print(f"Cloud Vector: {cloud_vector}")
    print(f"Cloud Opacity: {cloud_opacity}")
    print(f"Cloud Intensity: {cloud_intensity}")
    print(f"Cloud Color: {cloud_color}")
    
#endregion



#region Linking Nodes to Each Other
def connect_nodes(world_node_tree, node_sky, world_background_node, mix_shader_node, rgb_shader_node, 
                  add_shader_node, additional_background_node, musgrave_texture_node, color_ramp_node, 
                  world_output_node):
    '''Connects the nodes to each other'''
    world_node_tree.links.new(node_sky.outputs["Color"], world_background_node.inputs["Color"])
    world_node_tree.links.new(world_background_node.outputs["Background"], mix_shader_node.inputs[1])
    world_node_tree.links.new(mix_shader_node.outputs[0], add_shader_node.inputs[0])
    world_node_tree.links.new(rgb_shader_node.outputs[0], mix_shader_node.inputs[2])
    world_node_tree.links.new(musgrave_texture_node.outputs[0], color_ramp_node.inputs["Fac"])
    world_node_tree.links.new(color_ramp_node.outputs["Color"], additional_background_node.inputs["Color"])
    world_node_tree.links.new(additional_background_node.outputs["Background"], add_shader_node.inputs[1])
    world_node_tree.links.new(add_shader_node.outputs[0], world_output_node.inputs["Surface"])
#endregion

def set_up_sky(sun_config=None, cloud_config=None, color_config=None,  strength=1.0):
    world_node_tree, node_location_x_step, node_location_x = create_variables()
    
    # Sky Node
    node_sky, node_location_x = create_sky_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Background Nodes
    world_background_node, node_location_x = create_first_background_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Mix Shader Node
    mix_shader_node, node_location_x = create_mix_shader_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # RGB Shader Node
    rgb_shader_node, node_location_x = create_rgb_shader_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Add Shader Node
    add_shader_node, node_location_x = create_add_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Additional Background Node
    additional_background_node, node_location_x = create_additional_background_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Musgrave Texture Node
    musgrave_texture_node, node_location_x = create_musgrave_texture_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Color Ramp Node
    color_ramp_node, node_location_x = create_color_ramp_node(
        world_node_tree, rgb_shader_node, node_location_x_step, node_location_x
    )
    
    # Output Node
    world_output_node, node_location_x = create_output_node(
        world_node_tree, node_location_x_step, node_location_x
    )
    
    # Apply Configurations
    if sun_config:
        print("Updating Sun Data")
        apply_sun_config(node_sky, sun_config)
                
    if color_config:
        apply_color_config(rgb_shader_node, mix_shader_node, color_config)
    
    if cloud_config:
        print("Updating Cloud Data")
        apply_cloud_config(musgrave_texture_node, color_ramp_node, additional_background_node, cloud_config)

    connect_nodes(
        world_node_tree, 
        node_sky, 
        world_background_node, 
        mix_shader_node, 
        rgb_shader_node, 
        add_shader_node, 
        additional_background_node, 
        musgrave_texture_node, 
        color_ramp_node, 
        world_output_node
    )
    



def random_color():
    '''Generates a random color'''
    color = []
    for i in range(3):
        color.append(random.uniform(0.0, 1.0))
    
    return color

#region Random Configurations
def generate_random_sun_config():
    '''Generates a random sun configuration'''
    sun_config = {
        "sun_rotation": math.radians(random.randint(0, 360)),
        "sun_intensity": random.randrange(1, 5),
        "sun_elevation": math.radians(random.randint(0, 90)),
        "altitude": math.radians(random.randint(0, 90)),
        "air_density": random.randint(1, 10),
        "dust_density": random.randint(1, 10),
        "ozone_density": random.randint(1, 10),
        "sun_size": math.radians(random.randint(0, 90))
    }
    return sun_config

def generate_random_color_config():
    '''Generates a random color configuration'''
    color = random_color()
    color_config = {
        "sky_color": (color[0], color[1], color[2], 1),
        "mix_factor": random.uniform(0.1, 0.9)
    }
    return color_config

def generate_random_cloud_config():
    '''Generates a random cloud configuration'''
    color = random_color()
    cloud_config = {
        "cloud_size": random.randint(1, 5),
        "cloud_vector": (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)),
        "cloud_opacity": random.uniform(0.0, 1.0),
        "cloud_intensity": random.uniform(0.0, 1.0),
        "cloud_color": (color[0], color[1], color[2], 1),
    }
    return cloud_config
#endregion

def execute():
    sun_config = generate_random_sun_config()
    color_config = generate_random_color_config()
    cloud_config = generate_random_cloud_config()

    set_up_sky(
        sun_config=sun_config, 
        strength=0.2, 
        color_config=color_config, 
        cloud_config=cloud_config
    )


if __name__ == "__main__":
    # main()
    pass