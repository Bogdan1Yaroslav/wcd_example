# 🧨 Web Cache Deception Demo (PoC)

> A minimal and educational project demonstrating the **Web Cache Deception (WCD)** vulnerability using Flask + NGINX.  
> Inspired by PortSwigger Labs and based on the original 2017 disclosure by Omer Gil.

---

## ⚠️ Disclaimer

> This project is intended **solely for educational and ethical purposes**.  
> 
>  The techniques and concepts presented here are meant to help developers and security researchers understand Web Cache Deception and how to prevent it.
>  
> **Unauthorized testing or exploitation of systems without permission is illegal and may lead to criminal charges.**  
>  
>  The author does not condone malicious activity and shall not be held responsible for the misuse of this code.
---

## 📚 About the Project

This is a fully functional and intentionally vulnerable web application built to demonstrate how Web Cache Deception works in real-world scenarios.

- 🔐 Uses JWT for authentication  
- 📦 Behind an NGINX reverse proxy with intentionally misconfigured caching  
- 🔎 Includes dynamic routes like `/profile`, which are tricked into being cached as `/profile.css`  
- 🧪 Can be tested entirely locally using Docker Compose  

The attack flow is based on the technique first disclosed in [this blog post](https://www.acunetix.com/blog/articles/web-cache-deception/) by Omer Gil, and inspired by [PortSwigger Academy's WCD lab](https://portswigger.net/web-security/web-cache-deception).

---

## 🚀 Getting Started

### 🐳 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### ✅ Features

- 📦 NGINX reverse proxy  
- 🔐 JWT-based authentication  
- 🐍 Flask backend  
- 🧠 WCD-aware routing logic (for demonstration)  
- 🔎 Debug logging for cache behavior  


### ⚙️ Installation

```bash
git clone https://github.com/Bogdan1Yaroslav/wcd_example.git
cd wcd_example
docker-compose up --build
```

Then open your browser and go to:

```
http://localhost:80/
```

---

## 📂 .env file

The project includes a `.env` file in the repository.  
**This is intentional**, as the goal is to provide a plug-and-play PoC that works out of the box without additional configuration.

> ⚠️ In real-world production setups, sensitive data like secret keys should **never** be stored in versioned `.env` files.

---

## 📖 Article

Want to understand how it works in-depth?

👉 Read the full article:  
[**Web Cache Deception in Action: Realistic PoC with Flask + NGINX**](https://your-article-link.com)

Includes step-by-step attack breakdown, diagrams, protection strategies, and more.

---
