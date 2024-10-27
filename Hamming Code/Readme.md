# HammingCode
Hamming codes are a powerful error-correcting technique used in digital communication and data storage systems. This Python program demonstrates the implementation of Hamming codes for error detection and correction.
## Introduction
Hamming codes are widely used to ensure data integrity in scenarios where errors can occur during data transmission or storage. They achieve this by adding redundant bits (parity bits) to the original data, allowing for the detection and correction of errors.
This Python program allows you to encode and decode data using Hamming codes. It includes functions to generate valid matrices, input data, encode data, decode data, and check for errors.
## Explanation
Hamming code parameters (n, k, r) are defined, 
The generator matrix G is created by combining an identity matrix (I) and a parity matrix (P) to encode a k-bit data vector (D) into a code word (C).
To check for errors, the received code word (R) is multiplied by the transposed parity-check matrix (H) to calculate the syndrome (S), enabling identification of the erroneous bit's position for potential correction if S is non-zero.

