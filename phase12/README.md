# Phase 12 CI/CD and GitOps

Repository: https://github.com/aitlabo2026/docker-aws-study.git
Branch: main
CI: GitHub Actions -> OIDC -> ECR
CD: GitOps -> Argo CD -> EKS
Route 53: not used
Application check: http://localhost:18093/
Argo UI: https://localhost:18092/

The API image is built from an updated Debian base, scanned with Trivy, and published only when no fixable HIGH or CRITICAL vulnerability remains. Findings without an upstream fix are reported but do not block deployment.
