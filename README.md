# Image Encryption Tool

This Python script provides a simple tool for encrypting images using different methods: XOR encryption, additive encryption, and pixel swapping.

## Features

* **Image Encryption:** Encrypt images using three different methods.
    * **XOR Encryption:** Encrypts image pixels by performing a bitwise XOR operation with a key.
    * **Additive Encryption:** Encrypts image pixels by adding a key and applying a modulo operation.
    * **Pixel Swapping:** Encrypts an image by shuffling the pixel coordinates based on a seed.
* **Decryption:** The XOR and additive methods can be reversed for decryption. Pixel swapping can also be reversed if the same seed is used.
* **File Handling:** Loads and saves images using the Pillow (PIL) library.
* **Supports RGB Images:** The script works with RGB color images.

## Requirements

* Python 3
* Pillow (PIL) library (`pip install Pillow`)

## Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd image_encryption_tool
    ```
2.  **Run the script (the functions are designed to be used within a Python script, not directly from the command line):**
    ```python```
3.  **Replace `'input.png'` with the path to your image file.**
4.  **Modify the `encrypt_image` function calls to test different encryption methods and keys.** You can change the `method`, `key`, `seed`, and `output` parameters.
5.  **Run the Python script.** The encrypted images will be saved with the names specified in the `output` parameters.

## Function Details

* `load_image(path)`: Loads an image from the specified path using PIL.
* `save_image(img, path)`: Saves a PIL image to the specified path.
* `xor_encrypt(img, key)`: Encrypts the image by performing a bitwise XOR operation on each pixel's RGB values with the given key.
* `add_encrypt(img, key)`: Encrypts the image by adding the key to each pixel's RGB values, modulo 256.
* `pixel_swap(img, seed=42)`: Encrypts the image by shuffling the pixel coordinates using a pseudo-random number generator with the given seed.
* `encrypt_image(path, method='xor', key=123, seed=42, output='encrypted.png')`:  A helper function that performs the image encryption based on the specified method.
    * `path`: Path to the input image.
    * `method`:  The encryption method ('xor', 'add', or 'swap').
    * `key`:  The encryption key (integer).
    * `seed`:  The seed for pixel swapping (integer).
    * `output`:  The path to save the encrypted image.

## Notes

* The XOR and additive encryption methods are symmetric, meaning the same key is used for both encryption and decryption.  For additive encryption, use the negative of the original key to decrypt.
* The pixel swapping method is also symmetric; use the same seed to restore the original pixel order.
* This script provides basic image encryption for demonstration purposes.  For more secure encryption, consider using established cryptographic libraries like `cryptography` in Python.
* Error handling is minimal.  The script assumes valid input.
* The default seed for `pixel_swap` is 42, and the default key for `xor_encrypt` and `add_encrypt` is 123.
* The output file name defaults to "encrypted.png" if not specified.
