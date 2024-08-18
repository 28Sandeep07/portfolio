# GitHub Actions Documentation

## Overview

GitHub Actions is a CI/CD (Continuous Integration and Continuous Deployment) tool that allows you to automate workflows for building, testing, and deploying your code. It is integrated into GitHub repositories and enables you to create workflows that can be triggered by various events such as push, pull requests, or issues.

## Workflow Description

In this project, i created a GitHub Actions workflow to run Python unit tests. The workflow is defined in a YAML file and is located in the `.github/workflows` directory of the repository.

### Workflow File

The workflow file is named `python-app.yml` and is configured as follows:

```yaml
name: Python application

on: [push, pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Run tests
      run: |
        python portfolio/github-actions/test_script.py
