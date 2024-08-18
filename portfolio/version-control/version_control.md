# Version Control Documentation

This document explains the version control steps performed using Git and GitHub, as well as the purpose of each Git command used in the process.

## 1. Creating the Repository

### Step:
- **Created a new repository on GitHub** named `portfolio`.
- **Cloned the repository locally** to begin working on the project.

### Commands Used:
- `git clone https://github.com/yourusername/portfolio.git`
  
  **Explanation:** This command creates a local copy of the GitHub repository, allowing you to work on it locally and sync changes with the remote repository.

---

## 2. Initial Commit

### Step:
- **Created a folder structure**: Inside the `portfolio` folder, a subfolder named `version-control` was created.
- **Added an initial file**: A `sample.txt` file was created with some initial content.
- **Committed the initial file** to the repository.

### Commands Used:
- `git add portfolio/version-control/sample.txt`
  
  **Explanation:** Adds the specified file to the staging area, preparing it for commit.

- `git commit -m "Add sample.txt for version control demonstration"`

  **Explanation:** Commits the changes in the staging area to the repository with a descriptive message.

- `git push origin main`

  **Explanation:** Pushes the committed changes to the remote repository on GitHub.

---

## 3. Creating and Merging a Feature Branch

### Step:
- **Created a new branch**: This branch was used to add more content to `sample.txt`.
- **Modified the file**: Added additional content to `sample.txt` in the new branch.
- **Merged the branch back** into the `main` branch.

### Commands Used:
- `git checkout -b feature-branch`
  
  **Explanation:** Creates a new branch named `feature-branch` and switches to it.

- `echo "More content" >> portfolio/version-control/sample.txt`
  
  **Explanation:** This command appends additional content to `sample.txt`.

- `git add portfolio/version-control/sample.txt`
  
  **Explanation:** Adds the modified file to the staging area.

- `git commit -m "Updated sample.txt with more content"`

  **Explanation:** Commits the changes to the repository with a message.

- `git checkout main`
  
  **Explanation:** Switches back to the `main` branch.

- `git merge feature-branch`

  **Explanation:** Merges the changes from `feature-branch` into the `main` branch.

- `git push origin main`

  **Explanation:** Pushes the updated `main` branch to the remote repository.

---

## 4. Pulling Changes from GitHub

### Step:
- **Edited `sample.txt` directly in GitHub**: Added a line of text directly on the GitHub website to simulate remote changes.
- **Pulled the changes locally** to ensure the local repository is up-to-date.

### Commands Used:
- `git pull origin main`
  
  **Explanation:** Fetches and integrates changes from the remote `main` branch into the local `main` branch.

---

## 5. Summary of Git Commands

- **`git clone`**: Copies a remote repository to your local machine.
- **`git add`**: Stages changes for the next commit.
- **`git commit`**: Saves your staged changes to the repository with a message.
- **`git push`**: Sends your committed changes to the remote repository.
- **`git checkout -b`**: Creates and switches to a new branch.
- **`git merge`**: Combines changes from one branch into another.
- **`git pull`**: Updates your local repository with changes from the remote repository.

---

## 6. Conclusion

Through the steps documented above, the correct use of version control using Git and GitHub was demonstrated. The process covered adding files, creating and merging branches, and synchronizing changes between the local and remote repositories.
