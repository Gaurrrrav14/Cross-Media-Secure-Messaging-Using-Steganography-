# Cross-Media-Secure-Messaging-Using-Steganography-
🕵️‍♂️ Steganography-Based Secure Messaging
A Python-based application that enables secure communication by embedding text messages into images, audio, video, and plain text files using Steganography and RC4 Encryption.

This project demonstrates how sensitive data can be hidden in plain sight using Least Significant Bit (LSB) techniques across multiple media types, with practical applications in digital privacy, forensics, and secure messaging.

🎯 Project Aim
To design a robust and user-friendly system that allows users to securely send and receive secret messages by embedding them within multimedia files, while ensuring the messages remain hidden and untraceable to the naked eye.

🔐 Core Features
Text Steganography:
Uses zero-width characters to hide messages invisibly within regular text.

Image Steganography (LSB):
Hides encrypted messages in the pixel data of images using the Least Significant Bit method.

Audio Steganography:
Hides data inside .wav audio files using LSB, keeping the audio perceptually unchanged.

Video Steganography (with Encryption):
Embeds encrypted messages into video frames using RC4 encryption and LSB.

RC4 Encryption:
Adds a security layer to encrypt the message before embedding, and decrypt after extraction.

💡 Technologies & Libraries Used
Python 3

OpenCV – for image and video processing

PIL – for image handling

wave – for audio processing

NumPy – for matrix and bit manipulation

Tkinter (optional) – for UI (if implemented)

🔧 Algorithms Used
RC4 Stream Cipher

Encrypts/decrypts messages using user-defined keys.

Includes KSA (Key Scheduling Algorithm) and PRGA (Pseudo-Random Generation Algorithm).

LSB (Least Significant Bit) Encoding

Subtly replaces the least significant bit of media data (image/audio/video) to hide messages.

Binary Encoding/Decoding

Converts characters to binary for LSB insertion and reverts during extraction.

🧠 Use Cases
Confidential messaging between users

Stealthy data transfer in sensitive environments

Educational tool to understand encryption and steganography

Demonstration of vulnerabilities in unencrypted communication

