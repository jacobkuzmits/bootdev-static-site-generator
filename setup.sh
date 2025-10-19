#!/bin/bash

# Setup script to install git hooks

HOOK_DIR=".git/hooks"
HOOK_FILE="$HOOK_DIR/pre-commit"

echo "Setting up git hooks..."

# Create the pre-commit hook
cat > "$HOOK_FILE" << 'EOF'
#!/bin/sh

# Pre-commit hook to build the site with production basepath
# This ensures GitHub Pages gets the correct paths

echo "Running production build for GitHub Pages..."

python3 src/main.py production

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✓ Build successful"
    # Add the generated docs/ directory to the commit
    git add docs/
    exit 0
else
    echo "✗ Build failed - commit aborted"
    exit 1
fi
EOF

# Make the hook executable
chmod +x "$HOOK_FILE"

echo "✓ Pre-commit hook installed successfully!"
echo ""
echo "The hook will automatically run the production build before each commit."
