# SmallPixels

## Description

A clone of Python Discord Pixels focusing on being lightweight.

## Contributing

### Fork The Repo
Use `git clone https://github.com/cat-dev-group/smallpixels`.

### Install the Deta CLI

**MacOS and Linux**:
```sh
curl -fsSL https://get.deta.dev/cli.sh | sh
```

**Windows Powershell**:
```sh
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

### Login to the Deta CLI

Run `deta login` and sign in through your browser.

### Deploy to Deta

CD to the project's root, then type `deta new --python`. Then, use `deta deploy`. Then, get the URL that Deta spits out in the output of the first command and go to /tokens if you need to test any endpoints that require auth. If you make any changes, ensure you `deta deploy` to test. Once you are done making changes, open your PR.
