# Phase 09 EKS Migration

AWS profile: testuser001
Region: ap-northeast-1
Cluster: docker-aws-study-phase08
Namespace: phase09-app
Images: frontend/api phase09-v1
Order: EKS access -> EBS CSI -> data -> Keycloak -> application -> gateway
GUI: http://localhost:18090/
