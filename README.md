# Cloud API DevSecOps Pipeline

## Overview

This project explores the design and implementation of an end-to-end DevSecOps pipeline for a containerized Python API.

The proejct itnegrates automated testing, SAST, dependency scanning, secret detection, Infrastrucutre-as-Code validation, container security, policy-as-code, Kubernetes deployment testing, DAST, SBOM generation, and software supply-chain controls.

## Problem Statement

To deliver software quickly in the age of AI, engineering teams must shift security, infrastructure, QA, and other engineering practices left into the early stages of development. Traditional processes introduce manual reviews, handoffs, and inconsistent standards that create late-stage bottlenecks and expose vulnerabilities when they are most expensive to fix.

## Project Goals

- Build a small production-style REST API.
- Implement CI/CD using GitHub Actions.
- Integrate security throughout the SDLC.
- Containerize the application using Docker.
- Define cloud infrastructure using Terraform
- Test Terraform without provisioning cloud resources.
- Define Kubernetes deployments using Helm.
- Deploy the application into ephemeral Kubernetes clusters during CI.
- Perform automated SAST, SCA, secret, container, IaC, and DAST scanning.
- Generate an SBOM for release artifacts.
- Produce a verified release candidate after all security gates pass.

## Architecture

## Technology Stack

## Repository Structure

## Development Roadmap

```text

 [1. Minimal Application]
           │
           ▼
 [2. Quality Gate] - pytest, Ruff
           │
           ▼
 [3. GitHub Actions]
           │
           ▼
 [4. Docker]
           │
           ▼
 [5. Source Security] - Gitleaks, Semgrep
           │
           ▼
 [6. SCA] - Trivy (Dependencies)
           │
           ▼
 [7. Infrastructure-as-Code] - fmt, validate, TFLint
           │
           ▼
 [8. Policy-as-Code] - OPA (Kubernetes & Terraform)
           │
           ▼
 [9. Container Security] - Trivy (Images)
           │
           ▼
 [10. SBOM Generation] - Syft
           │
           ▼
 [11. Kubernetes] - Helm, kind
           │
           ▼
 [12. Integration Testing]
           │
           ▼
 [13. DAST] - OWASP ZAP
           │
           ▼
┌────────────────────────────────────────────────────────┐
│ [14. Secure Release Workflow]                          │
│ └── Signing, Attestation, Provenance, Artifacts        │
└────────────────────────────────────────────────────────┘
```
