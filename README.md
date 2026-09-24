# Mohammed Huzaif's AI Digital Twin 🤖

[![Live Demo](https://img.shields.io/badge/Live%20Demo-CloudFront-232F3E?logo=amazon-aws&logoColor=white)](https://d2r24io8s6cv01.cloudfront.net/)
[![Next.js](https://img.shields.io/badge/Frontend-Next.js%2016-black?logo=next.js)](https://nextjs.org/)
[![AWS Bedrock](https://img.shields.io/badge/AI%20Model-Amazon%20Nova%20Pro-FF9900?logo=amazonaws)](https://aws.amazon.com/bedrock/)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform)](https://www.terraform.io/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions)](https://github.com/features/actions)

A full-stack, enterprise-grade **AI Digital Twin** representing Mohammed Huzaif. The twin answers questions, shares background and expertise, and converses with users in real-time. Built entirely on a **100% serverless AWS architecture**, provisioned with **Terraform**, and automated with a modern **GitHub Actions CI/CD pipeline using OIDC authentication**.

🔗 **Live Production Site:** [https://d2r24io8s6cv01.cloudfront.net/](https://d2r24io8s6cv01.cloudfront.net/)

---

## 🏗️ Architecture Overview

The application follows modern cloud and serverless design principles:

```mermaid
flowchart TD
    subgraph Client ["Client Layer"]
        User["User Browser"]
    end

    subgraph Edge ["Content Delivery"]
        CF["Amazon CloudFront CDN<br/>(Global Edge)"]
        S3Frontend["Amazon S3 Bucket<br/>(Static Website Hosting)"]
    end

    subgraph API ["Backend API & Compute"]
        APIGW["Amazon API Gateway HTTP API<br/>(CORS + Rate Limiting)"]
        Lambda["AWS Lambda Function<br/>(Python 3.11 Runtime)"]
    end

    subgraph Intelligence ["AI & Storage Layer"]
        Bedrock["Amazon Bedrock<br/>(Nova Pro / Nova Micro)"]
        DynamoDB["Amazon DynamoDB<br/>(Session & Chat History)"]
        S3Memory["Amazon S3 Bucket<br/>(Long-Term Knowledge Base)"]
    end

    subgraph DevOps ["CI/CD Pipeline"]
        GHA["GitHub Actions Workflow"]
        OIDC["AWS IAM OIDC Identity Provider"]
        TFState["S3 Backend State & DynamoDB Locks"]
    end

    User -->|Static Assets| CF
    CF -->|Fetch Build| S3Frontend
    User -->|Chat POST /chat| APIGW
    APIGW -->|Trigger| Lambda
    Lambda -->|Inference| Bedrock
    Lambda <-->|Session State| DynamoDB
    Lambda <-->|Knowledge Retrieval| S3Memory

    GHA -->|Assume Role via OIDC| OIDC
    GHA -->|Terraform Plan/Apply| TFState
    GHA -->|Sync Next.js Export| S3Frontend
    GHA -->|Invalidate Cache| CF
```

---

## ✨ Key Features

- **🧠 Advanced AI Foundation**:
  - **Production:** Powered by **Amazon Nova Pro** (`amazon.nova-pro-v1:0`) for complex, high-reasoning conversational intelligence.
  - **Development:** Powered by **Amazon Nova Micro** (`amazon.nova-micro-v1:0`) for ultra-low latency and cost-effective development cycles.
- **⚡ 100% Serverless & Pay-Per-Request**:
  - Zero idle cost — scales from 0 to thousands of concurrent users automatically.
  - AWS Lambda + API Gateway + DynamoDB on-demand mode.
- **🛡️ Secure, Keyless CI/CD (GitHub Actions + OIDC)**:
  - Uses AWS OpenID Connect (OIDC) with immutable subject claims.
  - **Zero permanent AWS access keys or secrets** stored in GitHub repository settings.
- **📦 Distributed Remote State Management**:
  - Multi-environment Terraform state stored in remote S3 bucket with client-side encryption.
  - Distributed state locking via DynamoDB to prevent concurrent deployment collisions.
- **🌐 High-Speed Edge Delivery**:
  - Next.js static export distributed across global AWS CloudFront edge locations.
  - Automated CloudFront cache invalidation on code deployment.
- **🔒 API Throttling & Protection**:
  - Configurable rate limits and burst protection via API Gateway (e.g., 50 burst / 25 rate limit in production).
  - Cross-Origin Resource Sharing (CORS) restricted to authorized origins.

---

## 📁 Repository Structure

```text
twin/
├── .github/
│   └── workflows/
│       ├── deploy.yml            # Automated CI/CD deployment pipeline
│       └── destroy.yml           # Safe manual teardown workflow
├── backend/
│   ├── lambda_handler.py         # Main AWS Lambda entry point & routing
│   ├── resources.py              # Bedrock, DynamoDB, and S3 integration
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── app/                      # Next.js App Router (layout.tsx, page.tsx)
│   ├── components/               # UI components (twin.tsx chat interface)
│   ├── public/                   # Static assets (avatar.jpg, favicon.ico)
│   ├── package.json              # Frontend dependencies
│   └── next.config.ts            # Static HTML export configuration
├── terraform/
│   ├── main.tf                   # Core AWS infrastructure (S3, CloudFront, Lambda, API Gateway)
│   ├── variables.tf              # Configurable variables & defaults
│   ├── outputs.tf                # Deployed URLs and resource identifiers
│   ├── backend.tf                # S3 remote backend declaration
│   ├── backend-setup.tf          # Terraform state bucket & lock table setup
│   ├── github-oidc.tf            # GitHub Actions OIDC provider & IAM deployment role
│   ├── terraform.tfvars          # Default workspace variables
│   └── prod.tfvars               # Production-specific overrides (Nova Pro, limits)
├── scripts/
│   ├── deploy.sh / deploy.ps1    # Cross-platform local deployment scripts
│   └── destroy.sh / destroy.ps1  # Cross-platform infrastructure destruction scripts
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Next.js 16, React 19, TypeScript | Modern chat interface with static export |
| **Styling** | Tailwind CSS, Lucide Icons | Clean, responsive UI with custom branding |
| **Backend** | Python 3.11, AWS Lambda | Lightweight serverless API execution |
| **LLM Inference** | AWS Bedrock (Amazon Nova) | Multimodal foundation models for digital persona |
| **Memory** | Amazon DynamoDB & Amazon S3 | Session chat history and document storage |
| **API** | Amazon API Gateway (HTTP API v2) | Low-latency HTTP routing with CORS & throttling |
| **CDN & Storage** | Amazon CloudFront & Amazon S3 | Global static asset caching and website hosting |
| **IaC** | Terraform (HashiCorp) | Declarative multi-environment infrastructure |
| **CI/CD** | GitHub Actions | Automated build, test, and zero-downtime deployment |

---

## 🚀 Deployment & Environments

### Multi-Environment Strategy
Terraform workspaces isolate each environment's state:
- **`dev`**: Default sandbox for active development and feature validation.
- **`test`**: Staging environment for integration and load testing.
- **`prod`**: Live portfolio environment with upgraded **Nova Pro** model and enhanced rate limits.

### Automated CI/CD (GitHub Actions)
Every push to the `main` branch automatically:
1. Validates and packages the Python Lambda backend.
2. Builds and exports the Next.js static frontend.
3. Assumes an AWS IAM Role via temporary OIDC credentials.
4. Executes `terraform init` and `terraform apply` against the remote S3 state.
5. Syncs the compiled frontend assets to the S3 bucket.
6. Invalidates CloudFront edge caches globally.

### Manual Workflows
- **Deploy Specific Environment**: Trigger `Deploy Digital Twin` from the GitHub Actions tab and select `dev`, `test`, or `prod`.
- **Teardown Environment**: Trigger `Destroy Infrastructure` from GitHub Actions, select the environment, and confirm with `destroy`.

---

## 👤 Author

**Mohammed Huzaif**
- **Live Digital Twin:** [https://d2r24io8s6cv01.cloudfront.net/](https://d2r24io8s6cv01.cloudfront.net/)
- **GitHub:** [@HUZAIF004](https://github.com/HUZAIF004)
