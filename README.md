![Template](https://img.shields.io/badge/GitHub-Template-blue)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

# Cookiecutter Python OpenCode Template

A **strict, planning-first Python project template** designed for agentic coding with OpenCode. This template enforces engineering discipline by requiring documentation, testing, and planning before any implementation.

## 🎯 What This Template Enforces

### **Non-Negotiable Standards**
- **`/docs` as living system memory** - Mandatory Sphinx documentation
- **`/tests` as first-class artifacts** - Comprehensive testing structure
- **Planning before implementation** - No code without documented plans
- **`src/`-based packaging** - Modern Python package structure
- **OpenCode rules enforcement** - Automated quality gates

### **Engineering Discipline**
- **Documentation-driven development** - Public APIs must be documented
- **Test-first approach** - Features require test plans
- **Status tracking** - Implementation progress must be tracked
- **Quality gates** - 85% test coverage, linting, formatting requirements
- **Architecture decisions** - ADRs for significant design choices

This template intentionally behaves like a **senior engineer with standards** - it prevents shortcuts and enforces best practices.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Cookiecutter: `pip install cookiecutter`

### Generate Project
```bash
cookiecutter gh:PatrickAgostini/cookiecutter-python-opencode
```

### Setup Generated Project
```bash
cd your-project-name
tox -e install-dev
```

### Complete Planning (Required)
1. Edit `docs/general/vision.rst` - Define problem and goals
2. Edit `docs/architecture/architecture.rst` - Design system architecture  
3. Edit `docs/implementation/plan.rst` - Create implementation milestones
4. Edit `tests/test_plan.md` - Plan comprehensive testing

### Start Development
```bash
tox -e test      # Run tests
tox -e lint      # Check code quality
tox -e docs      # Build documentation
tox -e quality   # Run all quality checks
```

---

## 📁 Generated Project Structure

```
your-project/
├── src/your_package/              # Python package (src-layout)
│   └── __init__.py               # Package metadata
├── docs/                         # Sphinx documentation
│   ├── general/                  # High-level docs
│   │   ├── index.rst             # Section entry point
│   │   ├── vision.rst            # Project vision & goals
│   │   └── description.rst       # Project description
│   ├── implementation/           # Implementation tracking
│   │   ├── index.rst             # Section entry point
│   │   ├── plan.rst              # Implementation milestones
│   │   └── status.rst            # Progress tracking
│   ├── architecture/            # Architecture documentation
│   │   ├── index.rst             # Architecture section entry point
│   │   ├── architecture.rst      # System architecture
│   │   └── decisions.md          # Architecture Decision Records
│   ├── api/                     # Auto-generated API docs
│   │   ├── index.rst           # API section entry point
│   │   └── modules.rst         # Module documentation
│   ├── conf.py                  # Sphinx configuration
│   └── index.rst                # Main documentation entry point
├── tests/                        # Comprehensive test suite
│   ├── unit/                    # Unit tests
│   ├── integration/             # Integration tests
│   ├── e2e/                     # End-to-end tests
│   ├── conftest.py              # Test configuration
│   └── test_plan.md             # Test planning document
├── pyproject.toml               # Modern Python packaging
├── opencode.yml                 # OpenCode rules & agents
├── tox.ini                      # Tox configuration for development
└── README.md                    # Project documentation
```

---

## 🤖 OpenCode Integration

This template includes sophisticated OpenCode configuration with:

### **Multi-Agent System**
- **`project-planning-agent`** - Technical planning and architecture
- **`project-review-agent`** - Independent design review  
- **`python-project-steward`** - Implementation and maintenance

### **Automated Project Validation**
- **Post-generation hooks** - Validate project structure completeness
- **Required file checks** - Ensure all planning documents exist
- **Directory validation** - Verify proper template structure
- **Success confirmation** - Clear next steps guidance

### **Execution Gates**
- **Planning completeness gate** - Blocks coding without plans
- **Design review gate** - Requires independent architecture review
- **Testing gate** - Prevents implementation without test plans

### **Quality Enforcement**
- **85% test coverage requirement**
- **Automated linting with ruff**
- **Code formatting with black**
- **Type checking with mypy**
- **Sphinx documentation validation**
- **GitHub Actions CI/CD** - Automated quality gates on every push
- **Pre-commit hooks** - Local quality enforcement
- **ADR enforcement** - Architecture Decision Records for design changes

---

## 🤖 Using This Template with OpenCode

This template is specifically designed for **agentic coding with OpenCode**. Here's how to use it effectively:

### **OpenCode Setup**

1. **Generate the Project** (as shown above)
2. **Navigate to Project Directory**:
   ```bash
   cd your-project-name
   ```
3. **Install Dependencies**:
   ```bash
   tox -e install-dev
   ```

### **OpenCode Agent Workflow**

The template includes three specialized agents that work together:

#### **🎯 Phase 1: Planning with `project-planning-agent`**

**Start OpenCode and specify the planning agent**:
```
You are the project-planning-agent. Help me complete the planning documents for this Python project.
```

**Required Planning Tasks**:
1. **Complete Vision Document** (`docs/general/vision.rst`):
   - Define the problem statement
   - Identify target users
   - Set success criteria
   - List non-goals and constraints

2. **Design Architecture** (`docs/architecture/architecture.rst`):
   - Create system context diagram
   - Define core components
   - Document data flow
   - List external dependencies

3. **Create Implementation Plan** (`docs/implementation/plan.rst`):
   - Define development milestones
   - Identify risks and dependencies
   - Plan validation strategy

4. **Plan Testing Strategy** (`tests/test_plan.md`):
   - Define testing scope
   - Plan unit, integration, and E2E tests
   - Set up test data requirements

#### **🔍 Phase 2: Review with `project-review-agent`**

**Switch to review agent for validation**:
```
You are the project-review-agent. Critically evaluate the planning documents I've completed.
```

**Review Tasks**:
- Validate architecture decisions
- Check for missing requirements
- Identify potential risks
- Suggest improvements

#### **⚡ Phase 3: Implementation with `python-project-steward`**

**Switch to implementation agent**:
```
You are the python-project-steward. Help me implement this project following the established plans.
```

**Implementation Tasks**:
- Write code with comprehensive tests
- Ensure 85%+ test coverage
- Document all public APIs
- Follow quality standards

### **OpenCode Quality Gates**

The template enforces these **automated quality gates**:

#### **🚪 Planning Completeness Gate**
- **Blocks**: Any code implementation
- **Requires**: Complete planning documents
- **Checked**: `docs/general/vision.rst`, `docs/architecture/architecture.rst`, `docs/implementation/plan.rst`

#### **🔍 Design Review Gate**  
- **Blocks**: Implementation start
- **Requires**: Independent review approval
- **Checked**: Review agent validation

#### **🧪 Testing Gate**
- **Blocks**: Feature implementation
- **Requires**: Comprehensive test plan
- **Checked**: `tests/test_plan.md`

### **OpenCode Quality Enforcement**

The agents automatically enforce:

#### **📊 Quality Metrics**
- **Test Coverage**: ≥85% (checked with `tox -e cov`)
- **Code Quality**: Zero ruff errors (checked with `tox -e lint`)
- **Type Safety**: Zero mypy errors (checked with `tox -e typecheck`)
- **Documentation**: Clean Sphinx build (checked with `tox -e docs`)

#### **🔄 Status-Driven Behavior**
The agents respond to project status:
- **Blocked Status**: Propose resolution steps
- **Missing Tests**: Require test plan updates
- **Feature Complete**: Ensure quality gates pass

### **OpenCode Best Practices**

#### **📝 Planning First**
- Never write code without completing planning documents
- Always get architecture review before implementation
- Document decisions with ADRs in `docs/architecture/decisions.md`

#### **🧪 Test-Driven Development**
- Write tests before or alongside code
- Ensure all public APIs are tested
- Maintain 85%+ coverage

#### **📚 Living Documentation**
- Update docs when code changes
- Keep implementation status current
- Generate API docs automatically

#### **🎯 Quality Standards**
- Run `tox -e quality` before commits
- Fix all linting and type errors
- Ensure documentation builds cleanly

### **OpenCode Example Session**

```
User: Help me start a new Python project for a web API
OpenCode: I'll use the project-planning-agent. Let's complete the vision document first...
[Agent helps complete docs/general/vision.rst]

User: Now let's design the architecture
OpenCode: I'll create the system architecture in docs/architecture/architecture.rst...
[Agent helps complete architecture]

User: Can you review these plans?
OpenCode: Switching to project-review-agent. I'll evaluate your plans...
[Review agent provides feedback]

User: Great! Now let's implement
OpenCode: Switching to python-project-steward. Let's start implementation...
[Implementation agent helps write code with tests]
```

### **OpenCode Integration Benefits**

✅ **Automated Quality Enforcement** - Agents prevent shortcuts  
✅ **Multi-Agent Collaboration** - Specialized agents for each phase  
✅ **Status-Driven Behavior** - Smart responses to project state  
✅ **Planning-First Development** - No coding without proper planning  
✅ **Comprehensive Testing** - Agents ensure test coverage  
✅ **Living Documentation** - Docs stay in sync with code  

---

## 🛠️ Development Workflow

### **1. Planning Phase** (Required)
```bash
# Edit planning documents
vim docs/general/vision.rst      # Define problem & success criteria
vim docs/architecture/architecture.rst # Design system architecture
vim docs/implementation/plan.rst  # Create implementation milestones
vim tests/test_plan.md            # Plan comprehensive testing
```

### **2. Implementation Phase**
```bash
# Development commands
tox -e cov        # Run tests with coverage (must be ≥85%)
tox -e lint       # Check code quality with ruff
tox -e format     # Format code with black
tox -e docs       # Build Sphinx documentation
tox -e quality    # Run all quality checks
```

### **3. Quality Gates**
The template enforces these quality requirements:
- ✅ All public APIs documented
- ✅ 85%+ test coverage
- ✅ Zero linting errors
- ✅ Clean Sphinx build
- ✅ Type checking passes
- ✅ Required planning documents completed
- ✅ ADRs for architecture changes
- ✅ CI/CD pipeline validation

---

## 📋 Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `project_name` | "My Python Project" | Human-readable project name |
| `project_slug` | "my-python-project" | URL-friendly project identifier |
| `package_name` | "my_python_project" | Python package name |
| `author_name` | "Your Name" | Project author |
| `author_email` | "you@example.com" | Contact email |
| `python_version` | "3.11" | Minimum Python version |
| `use_ruff` | `true` | Enable ruff linting |
| `use_black` | `true` | Enable black formatting |
| `sphinx_theme` | "shibuya" | Sphinx documentation theme (10+ options) |

### **Available Sphinx Themes**

Choose from 10+ carefully curated themes:

**Modern Themes (Recommended):**
- `shibuya` (Default) - Clean, modern design with light/dark mode
- `furo` - Minimalist, fast-loading design
- `pydata_sphinx_theme` - Data science focused with GitHub integration
- `sphinx_book_theme` - Book-like layout for tutorials
- `sphinx_immaterial` - Material Design inspired

**Classic & Specialized:**
- `sphinx_rtd_theme` - Popular Read the Docs theme
- `alabaster` - Classic Sphinx built-in theme
- `sphinxawesome_theme` - Bold, distinctive design
- `piccolo_theme` - Clean, minimalist
- `sphinx_press_theme` - Typography-focused

📖 **See [SPHINX_THEMES.md](SPHINX_THEMES.md)** for detailed theme descriptions, screenshots, and customization guides.

---

## 🆕 What's New in v1.0.0+

### **Latest Enhancements**
- **🎨 10+ Sphinx Theme Options** - Choose from modern, classic, and specialized themes
- **📖 Comprehensive Theme Guide** - Detailed SPHINX_THEMES.md with screenshots and customization
- **🔧 Automated Project Validation** - Post-generation hooks ensure template integrity
- **⚡ Enhanced CI/CD Pipeline** - GitHub Actions with comprehensive quality gates
- **📋 Improved Documentation Structure** - Better organization and navigation

---

## 🎯 Why This Template?

### **For Teams That Value Quality**
- **Prevents technical debt** - Enforces planning and documentation
- **Ensures maintainability** - Comprehensive testing and type checking
- **Standardizes workflows** - Consistent development practices
- **Reduces onboarding time** - Clear documentation and structure

### **For OpenCode Users**
- **Agent collaboration** - Multi-agent development workflow
- **Automated enforcement** - Quality gates prevent regressions
- **Status-driven behavior** - Smart responses to project state
- **Planning-first** - No coding without proper planning

### **For Long-Term Projects**
- **Architecture decisions** - ADRs track design choices
- **Living documentation** - Docs stay in sync with code
- **Comprehensive testing** - Unit, integration, and E2E tests
- **Quality metrics** - Coverage, linting, and type checking

---

## 🔧 Customization

### **Adding Dependencies**
Edit `pyproject.toml`:
```toml
[project.dependencies]
requests = "^2.28.0"

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    # ... other dev dependencies
]
```

### **Modifying OpenCode Rules**
Edit `opencode.yml` to customize agent behavior, quality gates, and enforcement rules.

### **Extending Documentation**
Add new sections to `docs/` and update `docs/index.rst` to include them in the Sphinx build.

---

## 📚 Additional Resources

- **[OpenCode Documentation](https://opencode.ai)** - Learn about agentic coding
- **[Sphinx Documentation](https://www.sphinx-doc.org/)** - Documentation generation
- **[pytest Documentation](https://docs.pytest.org/)** - Testing framework
- **[Python Packaging](https://packaging.python.org/)** - Modern Python packaging

---

## 🤝 Contributing

Contributions to this template are welcome! Please ensure that:
1. All changes maintain the strict quality standards
2. Documentation is updated for any new features
3. Tests are added for new functionality
4. OpenCode rules are kept in sync

---

## 📈 Template Status

**Version**: v1.0.0+ (actively maintained)  
**Last Updated**: February 2026  
**Compatibility**: Python 3.11+  
**CI/CD**: ✅ Passing on all platforms  
**Documentation**: ✅ Complete and current  

---

## 📄 License

This template is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**⚡ Ready to build high-quality Python projects with engineering discipline?** 

Use this template and experience the difference that planning-first development makes!
