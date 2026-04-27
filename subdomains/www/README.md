# 🌐 Dumbfucks Club Website - Project Overview

## 🚀 Project Summary
This project is a modular, content-driven website built using **FastAPI**, designed to host diverse applications, from interactive AI tools to dynamic blogs and static demos. The architecture is highly decoupled, allowing individual projects to function as isolated micro-services, all orchestrated by a central FastAPI gateway.

## ✨ Core Features
The website currently offers the following high-level functionalities:

*   **Interactive AI Chatbot (`AI Tool`):** A dedicated module providing an interactive interface to local LLMs (via Ollama). It features custom logic to detect and render generated code blocks with proper syntax highlighting.
*   **Dynamic Blog/Content Delivery:** A content management system built around Markdown files. Blog posts are dynamically loaded from the `static/assets/blogs/` directory and converted to styled HTML.
*   **Modular Project Hosting:** The application is designed around multiple independent `Project` modules (AI, Blogs, DnD, etc.), ensuring a clean separation of concerns and high extensibility.
*   **Modern Frontend Interactivity (HTMX):** Utilizes HTMX to enable reactive user experiences, allowing for dynamic content updates (like chat responses) without full page reloads.
*   **Static Asset Hosting:** Serves all required visual assets, including custom CSS (Tailwind) and images.

## 🏗️ Technical Architecture
The system follows a **Modular API/Service-Oriented Architecture (SOA)** built on FastAPI.

*   **Gateway/Orchestrator:** `subdomains/www/app/main.py` serves as the central entry point, mounting all specialized project routers onto the main application instance.
*   **Domain Modules:** Each feature (e.g., `ai_project`) is an encapsulated service that handles its specific business logic, routing, and templating.
*   **Content Flow:** Static content (Markdown) is processed by the `markdown2html` utility to be rendered into HTML for presentation.
*   **Security:** Robust security is enforced via custom middleware, implementing policies like Content Security Policy (CSP), Strict Transport Security (HSTS), and Cross-Origin policies.

## 🛠️ Development Roadmap & Next Steps
While the application is functional, its current structure is a robust prototype. To evolve it into a scalable, production-grade platform, the following structural enhancements are prioritized:

### 🎯 High-Priority Structural Gaps (Roadmap)
1.  **Centralized Logging System:** Implement a dedicated logging service to replace basic `print()` calls, ensuring all application events are structured, centralized, and observable.
2.  **Dedicated Caching Layer:** Introduce a caching service (e.g., Redis) to significantly improve performance and reduce load on content retrieval and API calls.
3.  **Content Decoupling (CMS):** Migrate content from static Markdown files to a structured repository (like a database). This decouples the content source from the presentation logic, enabling a true Content Management System (CMS).
4.  **Formalized State Management:** Refactor services to use a strict **Router $\rightarrow$ Service $\rightarrow$ Repository** pattern, replacing mutable class attributes with injected, immutable services for predictable state management.

## 📂 Project Structure
The project is organized as follows:

*   `app/`: Contains the core Python logic, including `main.py`, project routers, utilities, and constants.
    *   `projects/`: Contains the independent, domain-specific modules (e.g., `ai_project.py`, `blog_project.py`).
    *   `utils/`: Contains helper functions, such as `markdown2html.py`.
    *   `constants/`: Stores global configuration and static parameters.
*   `static/`: Holds all public, client-facing assets.
    *   `assets/`: Contains images, CSS stylesheets, and raw content files (Markdown).
    *   `assets/blogs/`: Repository for raw blog Markdown files.

## 📦 Setup & Dependencies
**Required Dependencies:**
*   `fastapi[standard]`
*   `starlette`
*   `uvicorn`
*   `requests`
*   `ollama`

**Deployment:**
The application is containerized using `Dockerfile` and is configured to run using Uvicorn.