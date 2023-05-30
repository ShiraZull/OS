# Code Dev environment
xcode-select --install

# Install home-brew package manager
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/$USER/.zprofile
#eval "$(/opt/homebrew/bin/brew shellenv)"

# Install packages
packages=(
# Utility
	logi-options-plus
	idrive

# Documentation
	google-chrome
	obs

# Code Environment
	visual-studio-code
	git
	flutter
	docker
	gitlab-runner
	warp
)

brew install "${packages[@]}"
