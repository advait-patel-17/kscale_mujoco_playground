import matplotlib.pyplot as plt
import numpy as np
def generate_terrain_data(nrow=100, ncol=100):
    def fractal_noise(size, octaves, lacunarity, gain):
        noise = np.zeros(size)
        frequency = 1.0
        amplitude = 1.0
        
        for _ in range(octaves):
            phase = np.random.randint(0, 1000)
            x = np.linspace(0, frequency, size[0])
            y = np.linspace(0, frequency, size[1])
            X, Y = np.meshgrid(x, y, indexing='ij')
            
            Z = np.random.uniform(-1, 1, size)
            noise += amplitude * Z
            
            frequency *= lacunarity
            amplitude *= gain
        
        return noise
    
    # Generate terrain using fractal noise with original parameters
    terrain = fractal_noise((nrow, ncol), octaves=2, lacunarity=2.0, gain=0.25)
    
    # Normalize and scale
    terrain = (terrain - terrain.min()) / (terrain.max() - terrain.min())
    terrain *= 0.15  # Lower height scaling from original 0.27
    
    
    return terrain

# Save the terrain as a PNG file
terrain = generate_terrain_data()
plt.imsave('assets/hfield.png', terrain, cmap='terrain')
