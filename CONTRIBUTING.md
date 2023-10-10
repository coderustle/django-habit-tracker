# 🚀 Contribution Guide: Habitstacker

Welcome to the Habitstacker contribution guide. Thank you for deciding to contribute and make our app even better!

Habitstacker is a Django-based web application that's designed to help users track their habits. Whether you're a newbie or a seasoned contributor, your help can make a big difference. Let's work together to make Habitstacker the best it can be!

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [Setting Up the Project](#setting-up-the-project)
3. [Contribution Guidelines](#contribution-guidelines)
4. [Pull Request Process](#pull-request-process)
5. [Code of Conduct](#code-of-conduct)
6. [Getting Help](#getting-help)

## 🌱 Getting Started

1. **Fork the Repository**: Click the 'Fork' button at the top right of the main repo page. This will create a copy of the repo in your GitHub account.
2. **Clone Your Fork**: Open a terminal, navigate to the directory where you'd like to store the project, and run:
    ```bash
    git clone https://github.com/coderustle/habitstacker.git
    ```
3. **Add Upstream Remote**: This allows you to sync changes:
    ```bash
    git remote add upstream https://github.com/coderustle/habitstacker.git
    ```

## 🔧 Setting Up the Project

1. Set up a virtual environment (this ensures you don't mix package versions between projects):
    ```bash
    cd habitstacker
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run bootstrap.py. This will create the .env with the needed environment variables:
    ```bash
    ./scripts/bootstra.py
    ```



5. Visit `http://localhost:8000/` in your browser to see the app running.

## 🌟 Contribution Guidelines

- **Check for open issues**: Before starting, check if someone else is already working on the issue you're interested in. If there's no existing issue for what you want to work on, create a new one to discuss the changes/features with maintainers.
- **Branching**: Always create a new branch for your changes:
    ```bash
    git checkout -b feature/your-feature-name
    ```

- **Coding Standards**: Please adhere to standard coding conventions, which includes proper indentation, descriptive variable names, and clear commit messages.
- **Test your changes**: Ensure the app runs smoothly with your changes and try to add tests if possible.
- **Commit in Logical Chunks**: Break down your work into meaningful commits with descriptive messages.

## 🎉 Pull Request Process

1. Update your fork and branch with the latest changes from the `main` branch:
    ```bash
    git pull upstream main
    ```

2. Push your changes to your fork on GitHub:
    ```bash
    git push -u origin your-feature-branch-name
    ```

3. Go to the main Habitstacker repo on GitHub and click the "New Pull Request" button. Ensure you're comparing `main` from the original repo to your feature branch.
4. Fill in the PR template, describing the changes you've made and any other relevant information.
5. Wait for maintainers to review your PR. They might suggest some changes. Stay responsive.

Thank you for your interest in contributing to Habitstacker! We appreciate all efforts, big or small, and we look forward to seeing the project grow with your help.
