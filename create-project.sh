#!/bin/bash

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI is not installed. Please install it first."
    echo "Visit: https://cli.github.com/manual/installation"
    exit 1
fi

# Check if user is authenticated with GitHub CLI
if ! gh auth status &> /dev/null; then
    echo "You are not authenticated with GitHub CLI."
    echo "Please run 'gh auth login' to authenticate."
    exit 1
fi

# Function to display usage
function show_usage {
    echo "Usage: $0 <repo-name> [options]"
    echo ""
    echo "Options:"
    echo "  -t, --template <template>    Template repository to use (default: none)"
    echo "  -p, --private                Create private repository (default: public)"
    echo "  -d, --description \"text\"     Repository description"
    echo "  -h, --help                   Show this help message"
    echo ""
    echo "Example:"
    echo "  $0 my-new-project -t username/template-repo -d \"My awesome project\""
}

# Parse command line arguments
if [ $# -eq 0 ]; then
    show_usage
    exit 1
fi

REPO_NAME=$1
shift

TEMPLATE=""
VISIBILITY="--public"
DESCRIPTION=""

while (( "$#" )); do
    case "$1" in
        -t|--template)
            TEMPLATE="-p $2"
            shift 2
            ;;
        -p|--private)
            VISIBILITY="--private"
            shift
            ;;
        -d|--description)
            DESCRIPTION="-d \"$2\""
            shift 2
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            echo "Error: Unsupported option $1"
            show_usage
            exit 1
            ;;
    esac
done

# Create the repository
echo "Creating repository: $REPO_NAME"
COMMAND="gh repo create $REPO_NAME $TEMPLATE $VISIBILITY $DESCRIPTION"
echo "Executing: $COMMAND"
eval $COMMAND

# Check if repository creation was successful
if [ $? -eq 0 ]; then
    echo "Repository '$REPO_NAME' created successfully!"
    echo "You can clone it with: gh repo clone $REPO_NAME"
else
    echo "Failed to create repository."
    exit 1
fi