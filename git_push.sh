#!/bin/bash

# Initialize git repository if not already initialized
if [ ! -d .git ]; then
    git init
fi

# Create or overwrite .gitignore with specified content
cat > .gitignore <<EOL
/.idea
/.venv
myenv
EOL

# Stage all changes
git add .

# Prompt for commit message
echo -n "Commit Message: "
read message

# Commit with the provided message
git commit -m "$message"

# Push to GitHub (optional, uncomment next line if remote is set up)
git push origin main
