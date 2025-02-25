# Stego Shield - Image Steganography Tool 🔒

A web-based steganography application that allows users to securely hide and extract text messages within images. Built with Streamlit and Python, this tool provides an intuitive interface for steganographic operations with password protection.

## Features ✨

- **Message Hiding**: Embed secret text messages within images
- **Password Protection**: Secure your hidden messages with password encryption
- **Message Extraction**: Retrieve hidden messages using the correct password
- **User-Friendly Interface**: Clean and intuitive web interface
- **Secure Encoding**: Uses LSB (Least Significant Bit) steganography with random pixel selection
- **Image Support**: Works with PNG, JPG, and JPEG formats

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/pranavkoushik/Stego_Shield.git
cd Stego_Shield
```

2. Install the required packages:
```bash
pip install streamlit numpy Pillow
```

3. Run the application:
```bash
streamlit run steganography.py
```

## Usage 📝

### Hiding a Message
1. Select the "Hide Message" tab
2. Upload an image file (PNG, JPG, or JPEG)
3. Enter your secret message
4. Set a password for encryption
5. Click "Hide Message"
6. Download the encoded image

### Extracting a Message
1. Select the "Extract Message" tab
2. Upload an image containing a hidden message
3. Enter the correct password
4. Click "Extract Message"
5. View the decoded message

## Technical Details 🔧

- **Encoding Algorithm**: Uses LSB (Least Significant Bit) steganography
- **Password Security**: SHA-256 hashing for password-based pixel selection
- **Image Processing**: Numpy for efficient image manipulation
- **Web Framework**: Streamlit for the user interface
- **Image Handling**: PIL (Python Imaging Library) for image operations

## Security Features 🛡️

- Random pixel selection based on password hash
- Password-protected message extraction
- Non-sequential bit storage for improved security
- Delimiter-based message encoding

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
