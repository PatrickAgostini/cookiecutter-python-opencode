Architecture Decision Records
=============================

This directory contains Architecture Decision Records (ADRs) for {{ cookiecutter.project_name }}.

What are ADRs?
--------------

Architecture Decision Records capture important architectural decisions along with their context and consequences. Each ADR follows a standardized format to ensure consistency and completeness.

ADR Format
----------

Each ADR file follows the naming convention: ``ADR-XXX-short-title.rst``

Required Sections
-----------------

- **Status**: Current status of the decision (proposed, accepted, rejected, deprecated, superseded)
- **Context**: The situation that led to this decision
- **Decision**: The actual decision that was made
- **Alternatives Considered**: Other options that were evaluated
- **Consequences**: Results of applying this decision

ADR Index
---------

.. note:: TODO: Add index of ADRs as they are created

- ADR-001: [Title of first decision] - [Status]
- ADR-002: [Title of second decision] - [Status]

Creating New ADRs
-----------------

When making significant architectural decisions:

1. Create a new ADR file using the template below
2. Fill in all required sections
3. Update this index file
4. Commit the ADR with the implementation

ADR Template
------------

.. code-block:: rst

    ADR-XXX: [Short Title]
    ========================

    Status
    ------
    [proposed|accepted|rejected|deprecated|superseded]

    Context
    -------
    [Describe the context that led to this decision]

    Decision
    --------
    [Clearly state the decision that was made]

    Alternatives Considered
    -----------------------
    [List and describe alternatives that were considered]

    Alternative 1: [Name]
    ~~~~~~~~~~~~~~~~~~~~~
    [Description and why it was rejected]

    Alternative 2: [Name]
    ~~~~~~~~~~~~~~~~~~~~~
    [Description and why it was rejected]

    Consequences
    ------------
    [Describe the results of applying this decision]

    Positive Consequences
    ~~~~~~~~~~~~~~~~~~~~~
    [List positive outcomes]

    Negative Consequences
    ~~~~~~~~~~~~~~~~~~~~~
    [List negative outcomes and tradeoffs]

Review Process
--------------

All ADRs should be reviewed by:

1. The technical lead
2. Relevant stakeholders
3. The development team

Decisions can be updated or superseded as the project evolves, but the original ADR should be preserved for historical context.
