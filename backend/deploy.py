import os
import shutil
import stat
import subprocess
import time
import zipfile


def remove_readonly(func, path, excinfo):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        pass


def safe_rmtree(path):
    if not os.path.exists(path):
        return
    for attempt in range(5):
        try:
            shutil.rmtree(path, onexc=lambda func, p, exc: (os.chmod(p, stat.S_IWRITE), func(p)))
            return
        except TypeError:
            try:
                shutil.rmtree(path, onerror=remove_readonly)
                return
            except Exception:
                time.sleep(1)
        except Exception:
            time.sleep(1)

    if os.path.exists(path):
        try:
            subprocess.run(["powershell", "-Command", f"Remove-Item -Recurse -Force '{path}'"], check=False)
        except Exception:
            pass


def main():
    print("Creating Lambda deployment package...")

    # Clean up
    safe_rmtree("lambda-package")
    if os.path.exists("lambda-deployment.zip"):
        try:
            os.remove("lambda-deployment.zip")
        except Exception:
            pass

    # Create package directory
    os.makedirs("lambda-package", exist_ok=True)

    print("Installing dependencies for Lambda runtime (Linux x86_64)...")
    installed = False

    # Attempt 1: Fast direct install via uv with target platform Linux x86_64
    try:
        print("Trying uv pip install for Linux x86_64...")
        subprocess.run(
            [
                "uv",
                "pip",
                "install",
                "--target",
                "lambda-package",
                "-r",
                "requirements.txt",
                "--python-platform",
                "linux",
                "--python-version",
                "3.13",
            ],
            check=True,
        )
        installed = True
        print("[OK] Dependencies installed via uv.")
    except Exception as e:
        print(f"uv pip install failed or uv not available: {e}")

    # Attempt 2: Fallback to Docker if uv didn't work
    if not installed:
        print("Falling back to Docker for Lambda dependency installation...")
        subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{os.getcwd()}:/var/task",
                "--platform",
                "linux/amd64",
                "--entrypoint",
                "",
                "public.ecr.aws/lambda/python:3.13",
                "/bin/sh",
                "-c",
                "pip install --target /var/task/lambda-package -r /var/task/requirements.txt --platform manylinux2014_x86_64 --only-binary=:all: --upgrade",
            ],
            check=True,
        )

    # Copy application files
    print("Copying application files...")
    for file in ["server.py", "lambda_handler.py", "context.py", "resources.py"]:
        if os.path.exists(file):
            shutil.copy2(file, "lambda-package/")

    # Copy data directory
    if os.path.exists("data"):
        shutil.copytree("data", "lambda-package/data")

    # Create zip
    print("Creating zip file...")
    with zipfile.ZipFile("lambda-deployment.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("lambda-package"):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, "lambda-package")
                zipf.write(file_path, arcname)

    # Show package size
    size_mb = os.path.getsize("lambda-deployment.zip") / (1024 * 1024)
    print(f"[OK] Created lambda-deployment.zip ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()