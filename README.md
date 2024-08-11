# EasySocket

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)

## What is a Socket?

A socket is an endpoint for sending or receiving data across a computer network. Sockets allow communication between two different processes on the same or different machines. In the context of the Internet, sockets are typically used to enable communication between client and server applications.

In Python, the low-level `socket` library provides a means to create and interact with these communication endpoints. However, it can be complex and not so intuitive to use directly, especially for those new to networking. This is where **EasySocket** comes in.

## About EasySocket

**EasySocket** is a high-level interface designed to simplify the usage of Python's low-level `socket` library. It abstracts away much of the complexity, allowing developers to quickly and easily implement socket-based communication in their applications.

### Features

- Simplified socket creation and connection.
- Easy-to-use API for sending and receiving data.
- Only two methods to handle client-server interaction.
- Compatible only with TCP protocol (later version will implement also UDP).

### Installation

You can install locally **EasySocket** via executing:

```bash
pip install .
```

inside the project folder after cloning this github repository.

### Quick Start

Here’s an example of how you can use **EasySocket** to create a basic client-server application.

### Reference

For more detailed socket operations, you can refer to the official Python `socket` library documentation [here](https://docs.python.org/3/library/socket.html).

### Testing

The test scripts for **EasySocket** can be found in the files `client.py` and `server.py`.

To run the test examples:

1. **Important:** Start the server before the client.

2. Launch the server:

   ```bash
   python server.py
   ```

3. Then, launch the client:

   ```bash
   python client.py
   ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive guide to using the **EasySocket** library, including what sockets are, how to install and use the library, and how to run the test files.