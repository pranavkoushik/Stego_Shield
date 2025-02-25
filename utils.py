import numpy as np
import hashlib

def encode_message(image, message, password):
    # Create a copy of the image and ensure it's uint8
    encoded = image.copy().astype(np.uint8)

    # Convert message to binary
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '00000000'  # Add delimiter

    # Generate a seed from password for pseudo-random pixel selection
    seed = int(hashlib.sha256(password.encode()).hexdigest(), 16) % (2**32)
    np.random.seed(seed)

    # Get image dimensions
    height, width = image.shape[:2]

    if len(binary_message) > height * width * 3:
        raise ValueError("Message too long for this image")

    # Generate random positions for embedding
    positions = np.random.permutation(height * width * 3)[:len(binary_message)]

    # Embed each bit of the message
    for i, bit in enumerate(binary_message):
        pixel_position = positions[i]
        channel = pixel_position % 3
        pixel = pixel_position // 3
        row = pixel // width
        col = pixel % width

        # Get current pixel value
        pixel_value = int(encoded[row, col, channel])

        # Clear LSB and set new bit
        if int(bit) == 1:
            pixel_value = pixel_value | 1  # Set LSB to 1
        else:
            pixel_value = pixel_value & ~1  # Set LSB to 0

        # Ensure value stays in valid range
        pixel_value = max(0, min(255, pixel_value))

        # Store back as uint8
        encoded[row, col, channel] = np.uint8(pixel_value)

    return encoded

def decode_message(image, password):
    try:
        # Ensure image is uint8
        image = image.astype(np.uint8)

        # Generate the same seed from password
        seed = int(hashlib.sha256(password.encode()).hexdigest(), 16) % (2**32)
        np.random.seed(seed)

        # Get image dimensions
        height, width = image.shape[:2]

        # Generate the same random positions
        positions = np.random.permutation(height * width * 3)

        binary_message = ""
        # Extract bits until we find the delimiter or reach maximum length
        for i in range(min(len(positions), height * width * 3)):
            pixel_position = positions[i]
            channel = pixel_position % 3
            pixel = pixel_position // 3
            row = pixel // width
            col = pixel % width

            # Get the least significant bit
            pixel_value = int(image[row, col, channel])
            bit = pixel_value & 1
            binary_message += str(bit)

            # Check for delimiter every 8 bits
            if len(binary_message) % 8 == 0:
                try:
                    # Convert binary to string
                    chars = ''.join([chr(int(binary_message[j:j+8], 2)) 
                                   for j in range(0, len(binary_message), 8)])
                    if chars.endswith('\x00'):
                        return chars[:-1]
                except ValueError:
                    continue

        return None
    except Exception as e:
        print(f"Error during decoding: {str(e)}")
        return None