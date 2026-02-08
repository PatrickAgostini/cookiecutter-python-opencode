# {{ cookiecutter.project_name }}

{{ cookiecutter.project_name }} is a Python project bootstrapped with a **strict, planning-first Cookiecutter template** designed for agentic coding with OpenCode.

## 🎯 Project Overview

This project follows engineering discipline with:
- **Documentation-first development** - All public APIs documented
- **Comprehensive testing** - Unit, integration, and E2E tests
- **Planning before implementation** - No code without documented plans
- **Quality enforcement** - 85% coverage, linting, type checking

## 🚀 Quick Start

### Prerequisites
- Python {{ cookiecutter.python_version }}+

### Setup
```bash
# Install development dependencies
tox -e install-dev

# Run tests to verify setup
tox -e tests

# Build documentation
tox -e docs
```

### Development Commands
```bash
tox -e tests                               # Run tests
tox -e cov                                 # Run tests with coverage
tox -e lint                                # Check code quality
tox -e format                              # Format code
tox -e typecheck                           # Run type checking
tox -e docs                                # Build documentation
tox -e serve-docs                          # Serve documentation locally
tox -e clean                               # Clean build artifacts
```

## 📁 Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.package_name }}/    # Python package
├── docs/                                   # Project documentation
│   ├── general/                           # High-level documentation
│   ├── implementation/                    # Implementation tracking
│   └── architecture/                      # Architecture Decision Records
├── tests/                                 # Test suite
│   ├── unit/                             # Unit tests
│   ├── integration/                      # Integration tests
│   └── e2e/                              # End-to-end tests
├── pyproject.toml                        # Python packaging
├── opencode.yml                          # OpenCode rules
└── Makefile                              # Development commands
```

## 📋 Required Planning Documents

Before implementing any features, complete these planning documents:

### **1. Project Vision** (`docs/general/vision.rst`)
- Problem statement
- Target users and success criteria
- Project goals and non-goals
- Constraints and requirements

### **2. System Architecture** (`docs/architecture/architecture.rst`)
- System context and components
- Data flow and external dependencies
- Technology choices and tradeoffs
- Architecture decisions

### **3. Implementation Plan** (`docs/implementation/plan.rst`)
- Development milestones
- Dependencies and risks
- Validation strategy
- Timeline and deliverables

### **4. Test Plan** (`tests/test_plan.md`)
- Testing scope and strategy
- Unit, integration, and E2E test requirements
- Test data and environment setup
- Success criteria

## 🤖 OpenCode Integration

This project includes OpenCode configuration with:

### **Multi-Agent System**
- **`project-planning-agent`** - Technical planning and architecture
- **`project-review-agent`** - Independent design review
- **`python-project-steward`** - Implementation and maintenance

### **Quality Gates**
- **Planning completeness gate** - Requires vision, architecture, and implementation plans
- **Design review gate** - Independent architecture review
- **Testing gate** - Comprehensive test planning required

### **Quality Requirements**
- ✅ 85%+ test coverage
- ✅ Zero linting errors (ruff)
- ✅ Consistent code formatting (black)
- ✅ Type checking passes (mypy)
- ✅ Clean documentation build (Sphinx)

## 🛠️ Development Workflow

### **1. Planning Phase**
1. Complete `docs/general/vision.rst`
2. Design system in `docs/architecture/architecture.rst`
3. Create milestones in `docs/implementation/plan.rst`
4. Plan testing in `tests/test_plan.md`

### **2. Implementation Phase**
1. Implement features with comprehensive tests
2. Ensure 85%+ test coverage
3. Pass all quality gates (linting, formatting, type checking)
4. Update documentation and implementation status

### **3. Quality Assurance**
```bash
# Run full quality check
tox -e cov       # Verify coverage ≥85%
tox -e lint      # Check code quality
tox -e format    # Format code
tox -e docs      # Build documentation
```

## 📊 Project Status

Current implementation status is tracked in `docs/implementation/status.rst`.

### **Quality Metrics**
- Test Coverage: [Measured with `tox -e cov`]
- Code Quality: [Checked with `tox -e lint`]
- Documentation: [Built with `tox -e docs`]
- Type Safety: [Checked with `tox -e typecheck`]

## 🔧 Configuration

### **Dependencies**
Add dependencies in `pyproject.toml`:
```toml
[project.dependencies]
requests = "^2.28.0"
```

### **Development Dependencies**
Development tools are configured in the `[project.optional-dependencies]` section.

### **OpenCode Rules**
Modify `opencode.yml` to customize agent behavior and quality gates.

## 📚 Documentation

- **[API Documentation](docs/api/)** - Generated API reference
- **[Architecture Guide](docs/architecture/architecture.rst)** - System design
- **[Implementation Status](docs/implementation/status.rst)** - Progress tracking
- **[Architecture Decisions](docs/architecture/decisions.rst)** - Design rationale

## 🤝 Contributing

Contributions must follow the project's strict standards:

1. **Planning First** - Update planning documents before implementation
2. **Comprehensive Testing** - Include unit, integration, and E2E tests
3. **Documentation** - Document all public APIs and decisions
4. **Quality Gates** - Pass all quality checks (coverage, linting, formatting)

### **Development Process**
1. Plan changes in relevant documentation
2. Implement with tests
3. Verify quality metrics
4. Update implementation status
5. Submit for review

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Author**: {{ cookiecutter.author_name }}
- **Email**: {{ cookiecutter.author_email }}
- **Python Version**: {{ cookiecutter.python_version }}+

---

**Built with the [Cookiecutter Python OpenCode Template](https://github.com/anomalyco/cookiecutter-python-opencode)** - Engineering discipline for Python projects.
