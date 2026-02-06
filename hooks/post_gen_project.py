from pathlib import Path


def validate_project_structure():
    """Validate that the project was generated correctly."""
    project_root = Path(".")

    # Check required directories
    required_dirs = [
        "src",
        f"src/{{cookiecutter.package_name}}",
        "docs",
        "tests",
        "tests/unit",
        "tests/integration",
        "tests/e2e",
        "docs/general",
        "docs/implementation",
    ]

    missing_dirs = []
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if not full_path.exists():
            missing_dirs.append(str(full_path))

    # Check required files
    required_files = [
        f"src/{{cookiecutter.package_name}}/__init__.py",
        "pyproject.toml",
        "opencode.yml",
        "docs/index.rst",
        "docs/general/vision.rst",
        "docs/implementation/plan.rst",
        "tests/conftest.py",
        "tests/test_plan.md",
        "tox.ini",
    ]

    missing_files = []
    for file_path in required_files:
        full_path = project_root / file_path
        if not full_path.exists():
            missing_files.append(str(full_path))

    # Report any issues
    if missing_dirs:
        print("Missing required directories:")
        for dir_path in missing_dirs:
            print(f"   - {dir_path}")

    if missing_files:
        print("Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")

    if missing_dirs or missing_files:
        raise SystemExit("Project generation failed - missing required structure")

    print("Project generated successfully!")
    print(f"Project: {{cookiecutter.project_name}}")
    print(f"Package: {{cookiecutter.package_name}}")
    print(f"Python: {{cookiecutter.python_version}}")
    print("\nNext steps:")
    print("   1. cd {{cookiecutter.project_slug}}")
    print("   2. tox -e install-dev")
    print("   3. Complete the planning documents in docs/")
    print("   4. Run tests with: tox -e test")


if __name__ == "__main__":
    validate_project_structure()
