# AWS China Region Content Validation Tool

This tool validates AWS global region technical content for compatibility with AWS China regions. It analyzes content to determine if services, features, and architectures can be implemented in AWS China regions (cn-north-1, cn-northwest-1).

## Core Features

- **Basic Validation**: Analyzes content for AWS service compatibility with China regions
- **Deep Validation**: Performs actual deployment/execution validation for feasible content
- **Intelligent Feasibility Gate**: Prevents resource waste on unfeasible content
- **Content Type Detection**: Automatically identifies project vs tutorial content

## Key Capabilities

- Converts web content to clean Markdown format
- Identifies AWS services mentioned in content
- Validates service availability in China regions
- Assesses overall feasibility (HIGH/MODERATE/LOW)
- Performs actual deployment validation for GitHub projects
- Executes step-by-step validation for tutorials
- Provides detailed adaptation recommendations

## Value Proposition

This tool saves significant time and resources by automating the validation process that would otherwise require manual verification by AWS Solutions Architects. It helps customers quickly determine if global AWS content can be implemented in China regions.