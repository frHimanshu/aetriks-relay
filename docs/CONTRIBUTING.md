# Contributing to Aetriks

Thank you for your interest in contributing to the Aetriks project. This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Standards](#code-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Security Considerations](#security-considerations)

## Code of Conduct

This project is committed to providing a welcoming and inclusive environment for all contributors. By participating in this project, you agree to:

- Be respectful and considerate of others
- Focus on constructive feedback and discussions
- Follow the project's coding standards and guidelines
- Maintain the educational and research-focused nature of the project

## Getting Started

Before contributing, please ensure you understand the project's purpose and scope:

- This is an educational cybersecurity research project
- All contributions must maintain the educational focus
- Code should be well-documented and maintainable
- Security best practices must be followed

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Java 17 or higher
- Maven 3.6 or higher
- Git

### Local Development Environment

1. Fork the repository to your GitHub account
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/aetriks-relay.git
   cd aetriks-relay
   ```

3. Set up the development environment:
   ```bash
   # Install Python dependencies
   pip install -r keylogger/requirements.txt
   
   # Build the relay server
   cd relay-server
   mvn clean install
   cd ..
   ```

4. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Code Standards

### General Guidelines

- Write clear, readable, and maintainable code
- Follow the existing code style and conventions
- Add comprehensive comments for complex logic
- Include proper error handling
- Write self-documenting code with meaningful variable names

### Python Code Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for all functions and classes
- Handle exceptions gracefully
- Use meaningful variable and function names

### Java Code Standards

- Follow Google Java Style Guide
- Use meaningful class and method names
- Include JavaDoc comments for public methods
- Handle exceptions appropriately
- Use proper access modifiers

### Documentation Standards

- Update relevant documentation for any changes
- Include examples in documentation
- Keep setup instructions current
- Document any new configuration options

## Testing Guidelines

### Unit Testing

- Write unit tests for new functionality
- Ensure existing tests pass before submitting changes
- Aim for good test coverage
- Use descriptive test names

### Integration Testing

- Test the complete workflow (keylogger to server)
- Verify data transmission and logging
- Test error conditions and edge cases
- Validate configuration changes

### Manual Testing

- Test on both Windows and Linux systems
- Verify build processes work correctly
- Test deployment scenarios
- Validate security features

## Pull Request Process

### Before Submitting

1. Ensure your code follows the project's standards
2. Run all tests and verify they pass
3. Update documentation as needed
4. Test your changes thoroughly

### Pull Request Guidelines

1. Use a clear and descriptive title
2. Provide a detailed description of changes
3. Include any relevant issue numbers
4. List any breaking changes or new dependencies
5. Add screenshots or examples if applicable

### Review Process

- All pull requests require review
- Address feedback and requested changes
- Ensure CI/CD checks pass
- Maintain a professional and constructive tone

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

- Clear description of the issue
- Steps to reproduce the problem
- Expected vs actual behavior
- System information (OS, versions, etc.)
- Relevant logs or error messages

### Feature Requests

For feature requests, please include:

- Detailed description of the feature
- Use case and benefits
- Implementation suggestions if applicable
- Priority level

### Security Issues

For security-related issues:

- Report privately to the maintainers
- Provide detailed technical information
- Include potential impact assessment
- Suggest mitigation strategies

## Security Considerations

### Code Security

- Follow secure coding practices
- Validate all inputs
- Use secure communication protocols
- Implement proper authentication where needed
- Avoid hardcoding sensitive information

### Testing Security

- Test security features thoroughly
- Verify data protection measures
- Test access controls
- Validate encryption implementations

### Deployment Security

- Document security requirements
- Provide secure configuration examples
- Include security best practices
- Warn about potential risks

## Communication

### Discussion Channels

- GitHub Issues for bug reports and feature requests
- GitHub Discussions for general questions
- Pull request comments for code review discussions

### Response Times

- We aim to respond to issues within 48 hours
- Pull request reviews typically within 1 week
- Security issues are prioritized for immediate attention

## Recognition

Contributors will be recognized in the following ways:

- Listed in the project's contributors section
- Mentioned in release notes for significant contributions
- Acknowledged in documentation updates

## Questions and Support

If you have questions about contributing:

- Check existing documentation first
- Search existing issues and discussions
- Create a new issue for clarification
- Contact maintainers for complex questions

Thank you for contributing to the Aetriks project. Your contributions help make this educational tool more valuable for the cybersecurity community. 