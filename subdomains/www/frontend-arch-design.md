# Frontend Architecture Design

## Overview

Ideal architecture for a FastAPI backend with Jinja2Templates, HTMX, and Tailwind CSS v4.

---

## Template Composition Hierarchy

### 1. Layer Structure

```
┌─────────────────────────────────────────────────────┐
│  BASE LAYER (base.html)                             │
│  ┌─────────────────────────────────────────────┐   │
│  │ • HTML5 doctype                              │   │
│  │ • lang attribute                              │   │
│  │ • charset/meta tags                           │   │
│  │ • viewport configuration                      │   │
│  │ • title block                                │   │
│  │ • head block (CDN includes, fonts)            │   │
│  │ • body structure                              │   │
│  │ • main layout container                       │   │
│  │ • footer                                     │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                ↓ extends
┌─────────────────────────────────────────────────────┐
│  MACRO LAYER (main_macros.html)                     │
│  ┌─────────────────────────────────────────────┐   │
│  │ • navbar                                      │   │
│  │ • UI component utilities                      │   │
│  │ • CSS helper macros                           │   │
│  │ • shared form elements                        │   │
│  │ • navigation helpers                          │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                ↓ extends
┌─────────────────────────────────────────────────────┐
│  PARTIAL LAYER (htmx_partials/)                      │
│  ┌─────────────────────────────────────────────┐   │
│  │ • Reusable HTMX responses                    │   │
│  │ • Chat message components                     │   │
│  │ • Animation fragments                        │   │
│  │ • Dynamic content blocks                     │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                ↓ extends
┌─────────────────────────────────────────────────────┐
│  PROJECT LAYER (projects/)                           │
│  ┌─────────────────────────────────────────────┐   │
│  │ • HTML files that correlate to webpages      │
│  │ • Composed from custom HTML + layer components│
│  │ • Page assembly (not business logic)          │
│  │ • Layout composition                         │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘

*Projects layer is a composition layer - it assembles pages using
HTML from custom templates and reusable components from the
Base, Macro, and Partial layers. It does not contain business logic.*
```

### 2. Import Rules

**DO:**
```jinja
{% from 'macros/main_macros.html' import navbar, border_box_css, drop_shadow_css with context %}
{% extends 'macros/base.html' %}
```

**DON'T:**
```jinja
{% from 'macros/main_macros.html' import navbar with context %}
<!-- Import inside block tags or duplicate imports -->
{% from 'macros/main_macros.html' import navbar, navbar with context %}
```

---

## CSS Architecture

### 1. Token-Based Design System

```
static/assets/css/
├── tokens/                 # Design tokens (colors, spacing, typography)
│   ├── base.css            # Base design tokens
│   ├── project-a.css       # Project-specific overrides
│   └── project-b.css       # Project-specific overrides
├── components/             # Component styles
│   ├── card.css
│   ├── button.css
│   └── form.css
└── utilities/               # Reusable utility patterns
    ├── grid.css
    └── flexbox.css
```

### 2. Tailwind Integration

**Primary:** Use Tailwind v4 CSS-first approach
```css
@layer base, components, utilities;

@layer base {
  /* Override base styles */
  :root {
    --color-primary: oklch(75% 0.2 260);
  }
}

@layer components {
  /* Reusable component classes */
  .btn-primary {
    @apply bg-primary text-white px-4 py-2 rounded;
  }
}
```

**Project-Specific:** Keep project CSS in separate files
```jinja
<link rel="stylesheet" href="/static/css/projects/project-a.css">
```

---

## HTMX Integration

### 1. Version Management

**DO:** Use version manager with fallback
```jinja
{% set htmx_version = "2.0.6" %}
{% set htmx_integrity = "sha384-Akqfrbj/HpNVo8k11SXBb6TlBWmXXlYQrCSqEWmyKJe+hDm3Z/B2WVG4smwBkRVm" %}

<script src="https://cdn.jsdelivr.net/npm/htmx.org@{{ htmx_version }}/dist/htmx.min.js"
        integrity="{{ htmx_integrity }}"
        crossorigin="anonymous"></script>
```

**DON'T:** Hardcode CDN URLs
```jinja
<!-- ❌ Bad -->
<script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js"></script>
```

### 2. Response Patterns

**Chat/Message Responses:**
```jinja
<div hx-post="/api/chat" hx-target="this" hx-swap="innerHTML">
  <div id="messages"></div>
  <form id="message-form">
    <input type="text" name="message">
    <button>Send</button>
  </form>
</div>
```

**Dynamic Content:**
```jinja
<!-- Use keyframe attribute for animations -->
<img src="/image1.png" hx-get="/image2.png" 
     hx-target="this" 
     keyframe="1"
     hx-params="swap">
```

---

## Component System

### 1. Macro Organization

**main_macros.html structure:**
```jinja
{% macro navbar() %}
  <!-- Navigation component -->
{% endmacro %}

{% macro card() %}
  <!-- Card wrapper -->
{% endmacro %}

{% macro border_box_css() %}
  border rounded-md bg-gray-100
{% endmacro %}

{% macro drop_shadow_css() %}
  rounded-xl shadow-lg outline outline-black/20
{% endmacro %}

{% macro form_input() %}
  <!-- Reusable form input -->
{% endmacro %}
```

### 2. Partial Usage

**htmx_partials organization:**
```jinja
<!-- Reusable HTMX responses -->
<div hx-post="/api/update" hx-target="this">
  <div id="content"></div>
  <form>
    <!-- Dynamic content -->
  </form>
</div>

<!-- Chat message component -->
<div class="p-2 shadow-lg">
  <strong>AI:</strong>
  <p>{{ response | safe }}</p>
</div>
```

---

## Security Configuration

### 1. Content Security Policy

```python
# app/main.py
CSP = {
    "default-src": "'self'",
    "script-src": [
        "'wasm-unsafe-eval'",
        "https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js",
        "'self'",
    ],
    "style-src": ["'self'", "unsafe-inline"],  # Tailwind needs this
    "img-src": ["'self'", "data:"],
}
```

### 2. Header Implementation

```python
headers = {
    "Content-Security-Policy": self.parse_policy(CSP),
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Embedder-Policy": "require-corp",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Strict-Transport-Security": "max-age=31556926; includeSubDomains",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
}
```

---

## Migration Path

### Phase 1: Template Hierarchy
1. ✅ Establish base layer with proper doctype and meta tags
2. ✅ Create macro layer with reusable UI components
3. ✅ Set up partial layer for HTMX responses
4. 🔄 Migrate project templates to extend proper hierarchy

### Phase 2: CSS Architecture
1. 🔄 Extract shared styles to tokens directory
2. 🔄 Create component utility files
3. 🔄 Migrate project-specific CSS to separate files

### Phase 3: HTMX Standardization
1. 🔄 Implement version manager in base layer
2. 🔄 Document all hx-* attribute patterns
3. 🔄 Create partial component library

---

## Quick Reference

| Layer | File | Purpose |
|-------|------|---------|
| Base | `templates/macros/base.html` | HTML5 structure, head setup |
| Macros | `templates/macros/main_macros.html` | UI components, utilities |
| Partials | `templates/htmx_partials/*.html` | HTMX responses |
| Projects | `templates/projects/*.html` | Page composition (not business logic) |

| Category | Files | Purpose |
|----------|-------|---------|
| Tokens | `static/assets/css/tokens/*.css` | Design system |
| Components | `static/assets/css/components/*.css` | Reusable components |
| Utilities | `static/assets/css/utilities/*.css` | Pattern shortcuts |

---

## Key Principles

1. **Single Responsibility**: Each layer has a clear purpose
2. **Composition Over Inheritance**: Use extends/imports strategically
3. **DRY Macros**: Extract repeated patterns to macros
4. **Explicit HTMX**: Always specify version and integrity
5. **Token-Based CSS**: Separate design tokens from implementation
6. **Security First**: CSP and headers on every response

