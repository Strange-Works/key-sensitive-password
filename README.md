# Password Key Tracker

## Overview

Key Sensitive Password is a Python-based application designed to monitor and analyze key presses during password entry. It specifically detects whether keys were entered using Caps Lock, Shift, both, or neither.

Ive always entered my password the exact same way despite there being an exponential number of different ways to achieve the same string, so I wanted to create a program that takes this into consideration to improve security.

![Screenshot](screenshot.png)

## Features

- **Detailed Key Tracking**: Detects and logs if keys were entered using Caps Lock, Shift, both, or neither.
- **Real-time Updates**: Displays password entry details in real-time.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Strange-Works/password-key-tracker.git
   cd password-key-tracker
   ```

2. **Install Required Libraries**:
   ```bash
   pip install pynput
   ```

## Usage

1. **Run the Script**:

   ```bash
   python password_key_tracker.py
   ```

2. **Enter Password**:
   - Type your password into the password entry field in the GUI.
   - Press Enter to submit your password.
   - The GUI will update in real-time, showing the details of each key press.

## Custom Devices and Security

Integrating Password Key Tracker into custom devices can significantly enhance security by providing detailed insights into how passwords are entered. Potential applications include:

- **Custom Keyboards**: Implement the software to track and analyze password entry on custom-built keyboards, alerting users if unusual typing patterns are detected.
- **Secure Access Systems**: Use the tool in secure environments to monitor and log password entry methods, ensuring that passwords are entered securely and not using easily guessable patterns.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Oliver Strange - [oliver@strangedesign.co.uk](mailto:oliver@strangedesign.co.uk)

Project Link: [https://github.com/Strange-Works/password-key-tracker](https://github.com/yourusername/password-key-tracker)
