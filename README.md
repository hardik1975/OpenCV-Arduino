# Project Setup Guide

This guide will help you set up the development environment for the project.

## Prerequisites
- **Python Version**: Ensure Python 3.11.0 is installed on your system. You can download it from [python.org](https://www.python.org/).

## Steps to Set Up the Environment

### 1. Create a Virtual Environment
Creating a virtual environment helps isolate project dependencies.
```bash
python -m venv hardik_virtual_env
```

### 2. Activate the Virtual Environment
Activate the virtual environment based on your operating system:
- **Windows**:
  ```bash
  .\hardik_virtual_env\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source hardik_virtual_env/bin/activate
  ```

### 3. Install Required Libraries
Use `pip` to install the necessary dependencies:
```bash
pip install opencv-python
pip install mediapipe
pip install pyFirmata2
```

### 4. Additional Steps for Arduino Integration
- Install the `pyFirmata` library v2.5.8 from [this link](https://github.com/firmata/arduino).
- Upload the `StandardFirmata.ino` sketch to your Arduino board. You can find this sketch in the Arduino IDE under **File > Examples > Firmata > StandardFirmata**.

## Schematic

![image](https://github.com/user-attachments/assets/380dd4c5-2896-425f-a79e-0832cb077f22)

## Notes
- Ensure the virtual environment is activated before installing any libraries or running the project.
- If you encounter issues with library installations, consider upgrading `pip` using:
  ```bash
  python -m pip install --upgrade pip
  ```

You're now ready to start working on the project!
