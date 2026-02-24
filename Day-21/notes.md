# Day 21: Virtual Environments and pip

## 1. Why Virtual Environments?

When working on multiple Python projects, different projects may require different package versions.

Without virtual environments:
- Packages can conflict
- System Python gets messy
- Projects become hard to maintain

A virtual environment creates an isolated Python workspace for each project.

---

## 2. Creating a Virtual Environment

### Step 1: Create environment

```bash
python -m venv venv
```

This creates a folder named `venv`.

---

### Step 2: Activate environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

When activated, you will see `(venv)` in your terminal.

---

### Step 3: Deactivate environment

```bash
deactivate
```

---

## 3. What is pip?

`pip` is Python's package manager. It allows you to install and manage external libraries.

---

## 4. Installing Packages

```bash
pip install requests
```

Install a specific version:

```bash
pip install requests==2.31.0
```

---

## 5. Viewing Installed Packages

```bash
pip list
```

---

## 6. Saving Dependencies (requirements.txt)

Save installed packages:

```bash
pip freeze > requirements.txt
```

Install from requirements file:

```bash
pip install -r requirements.txt
```

This is very important for sharing projects.

---

## 7. Best Practices

- Always use virtual environments
- Never install packages globally for projects
- Commit requirements.txt to GitHub
- Use clear environment names

---

## 🎯 Summary

Today you learned:

- Why virtual environments matter
- How to create and activate venv
- How to use pip
- How to manage project dependencies

You're now working like a real Python developer. 🚀
