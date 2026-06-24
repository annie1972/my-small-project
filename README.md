# Hello World Flask App

A minimal Python Flask app that returns `Hello, world!`.

## Setup

1. Create a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Run the app:

   ```powershell
   python app.py
   ```

4. Open the app in a browser:

   ```text
   http://localhost:5000
   ```

## GitHub Connection

1. Initialize Git in this folder:

   ```powershell
   git init
   git add .
   git commit -m "Initial Flask hello world"
   ```

2. Create a GitHub repository on GitHub.com, then add it as a remote:

   ```powershell
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```

If you have the GitHub CLI installed, you can also run:

```powershell
gh repo create <repo-name> --public --source=. --remote=origin --push
```

## Notes

- GitHub hosts the code repository, not the running web server.
- To access this app from any computer on the internet, deploy it to a hosting service such as Render, Railway, Fly.io, or another cloud provider.
