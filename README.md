# Leetcode_Obsidian

This repository contains a script that automates the process of scraping LeetCode problems and their solutions, saving them as Markdown files in a structured folder format suitable for use with Obsidian, a powerful knowledge base tool. The script leverages Selenium to navigate LeetCode and BeautifulSoup for parsing HTML content.

## Features

- **Automated Scraping:** Automatically scrape LeetCode problems, including problem descriptions and code implementations.
- **Markdown Formatting:** Save problem descriptions and code in Markdown format, ready for use in Obsidian.
- **Folder Structure:** Organize problems into folders by type for easy navigation and reference.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- ChromeDriver

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/xiaotuor/Leetcode_Obsidian.git
    cd Leetcode_Obsidian
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver:**
    - Download the ChromeDriver version that matches your installed Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/).
    - Place the `chromedriver` executable in a directory that is in your system's PATH, or specify the path to `chromedriver` in the script.

## Usage

1. **Update the `obsidian_folder_path` in the script:**
    ```python
    obsidian_folder_path = r"C:\D\ProgramFiles\Obsidian\Tools\highLeecode"
    ```
    Ensure this path points to your desired folder for storing the LeetCode problems.

2. **Run the script:**
    ```bash
    python leetcode_obsidian.py
    ```

3. **Navigate to LeetCode:**
    - The script will open a browser window and navigate to the LeetCode problem list page. It will then start processing each problem type and problem, saving them as Markdown files in the specified folder.

## Folder Structure

The script creates a folder structure where each problem type is a folder, and each problem is saved as a Markdown file within its respective type folder. Example:
```python
obsidian_folder_path/
├── Array
│ ├── Problem 1.md
│ ├── Problem 2.md
│ └── ...
├── String
│ ├── Problem 1.md
│ ├── Problem 2.md
│ └── ...
└── ...
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only. Please ensure that your use of the script complies with LeetCode's terms of service and does not violate any copyright laws.


