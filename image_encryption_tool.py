from PIL import Image
import random

def load_image(path):
    return Image.open(path)

def save_image(img, path):
    img.save(path)

def xor_encrypt(img, key):
    encrypted = img.copy()
    pixels = encrypted.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    return encrypted

def add_encrypt(img, key):
    encrypted = img.copy()
    pixels = encrypted.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return encrypted

def pixel_swap(img, seed=42):
    swapped = img.copy()
    pixels = swapped.load()
    width, height = img.size
    pixel_coords = [(x, y) for x in range(width) for y in range(height)]

    random.seed(seed)
    shuffled_coords = pixel_coords[:]
    random.shuffle(shuffled_coords)

    for (x1, y1), (x2, y2) in zip(pixel_coords, shuffled_coords):
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    return swapped

def encrypt_image(path, method='xor', key=123, seed=42, output='encrypted.png'):
    img = load_image(path)
    img = img.convert('RGB')

    if method == 'xor':
        encrypted = xor_encrypt(img, key)
    elif method == 'add':
        encrypted = add_encrypt(img, key)
    elif method == 'swap':
        encrypted = pixel_swap(img, seed)
    else:
        raise ValueError("Unknown method")

    save_image(encrypted, output)
    print(f"Image encrypted using {method}. Saved as '{output}'.")

encrypt_image('input.png', method='xor', key=123)
encrypt_image('input.png', method='add', key=50)
encrypt_image('input.png', method='swap', seed=999)
# Decrypt XOR
encrypt_image('encrypted.png', method='xor', key=123, output='xor_decrypted.png')

# Decrypt Add
encrypt_image('encrypted.png', method='add', key=-50, output='add_decrypted.png')

# Decrypt Swap
encrypt_image('encrypted.png', method='swap', seed=999, output='swap_decrypted.png')
