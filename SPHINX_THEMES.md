# Sphinx Theme Guide

This guide explains the available Sphinx themes that can be selected when creating a project with this cookiecutter template.

## Available Themes

### Modern & Feature-Rich Themes

1. **Shibuya** (Default)
   - Clean, modern design
   - Excellent typography and spacing
   - Light/dark mode support
   - Responsive design

2. **Furo**
   - Minimalist, clean design
   - Fast loading
   - Good for technical documentation
   - Customizable color scheme

3. **PyData Sphinx Theme**
   - Designed for data science projects
   - Built-in navigation components
   - GitHub integration
   - Responsive sidebar

4. **Sphinx Book Theme**
   - Book-like layout
   - Ideal for tutorials and guides
   - Download buttons and repository links
   - Mobile-friendly

5. **Sphinx Immaterial**
   - Material Design inspired
   - Extensive customization options
   - Dark/light mode toggle
   - Search highlighting

### Classic Themes

6. **Alabaster** (Sphinx built-in)
   - Classic, simple design
   - Customizable sidebar
   - Good compatibility
   - No external dependencies

7. **Read the Docs Theme**
   - Popular and widely used
   - Three-column layout
   - Good search functionality
   - Stable and reliable

### Specialized Themes

8. **Sphinx Awesome Theme**
   - Bold, distinctive design
   - Good for modern projects
   - External links integration

9. **Piccolo Theme**
   - Clean, minimalist
   - Good for API documentation
   - Simple configuration

10. **Press Theme**
    - Typography-focused
    - Clean reading experience
    - Minimal distractions

## Choosing a Theme

When running the cookiecutter template, you'll be prompted to select a theme from this list. Each theme has its own strengths:

- **For modern projects**: Shibuya, Furo, or PyData
- **For books/tutorials**: Sphinx Book Theme
- **For API docs**: Piccolo or Furo
- **For compatibility**: Alabaster or Read the Docs

## Theme Configuration

Each theme is pre-configured with sensible defaults in `docs/conf.py`. The configuration includes:

- Color schemes (when supported)
- Navigation settings
- GitHub repository integration
- Custom branding options

You can further customize any theme by modifying the `html_theme_options` in `docs/conf.py` after project generation.

## Installation

Themes are automatically installed when you select them during project creation. If you want to install all themes for testing:

```bash
pip install -e ".[sphinx-themes]"
```

## Previewing Themes

To test different themes after project creation:

1. Install the desired theme package
2. Modify `sphinx_theme` in `docs/conf.py` 
3. Rebuild documentation:
   ```bash
   cd docs
   make html
   ```

The documentation will be available in `_build/html/index.html`.