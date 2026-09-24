param(
    [string]$Environment = "dev",   # dev | test | prod
    [string]$ProjectName = "twin"
)
$ErrorActionPreference = "Stop"

Write-Host "Deploying $ProjectName to $Environment ..." -ForegroundColor Green

# 1. Build Lambda package
Set-Location (Split-Path $PSScriptRoot -Parent)   # project root
Write-Host "Building Lambda package..." -ForegroundColor Yellow
Set-Location backend
uv run deploy.py
if ($LASTEXITCODE -ne 0) { throw "Lambda packaging failed (exit code $LASTEXITCODE)." }
Set-Location ..

# 2. Terraform workspace & apply
Set-Location terraform
terraform init -input=false
if ($LASTEXITCODE -ne 0) { throw "Terraform init failed (exit code $LASTEXITCODE)." }

if (-not (terraform workspace list | Select-String $Environment)) {
    terraform workspace new $Environment
} else {
    terraform workspace select $Environment
}

if ($Environment -eq "prod") {
    terraform apply -var-file="prod.tfvars" -var="project_name=$ProjectName" -var="environment=$Environment" -auto-approve
} else {
    terraform apply -var="project_name=$ProjectName" -var="environment=$Environment" -auto-approve
}
if ($LASTEXITCODE -ne 0) { throw "Terraform apply failed (exit code $LASTEXITCODE)." }

$ApiUrl        = terraform output -raw api_gateway_url
$FrontendBucket = terraform output -raw s3_frontend_bucket
if (-not $FrontendBucket) {
    throw "Frontend bucket name is empty. Terraform output s3_frontend_bucket was not found."
}
try { $CustomUrl = terraform output -raw custom_domain_url } catch { $CustomUrl = "" }

# 3. Build + deploy frontend
Set-Location ..\frontend

# Create production environment file with API URL
Write-Host "Setting API URL for production..." -ForegroundColor Yellow
"NEXT_PUBLIC_API_URL=$ApiUrl" | Out-File .env.production -Encoding utf8

npm install
if ($LASTEXITCODE -ne 0) { throw "npm install failed (exit code $LASTEXITCODE)." }
npm run build
if ($LASTEXITCODE -ne 0) { throw "npm run build failed (exit code $LASTEXITCODE)." }
aws s3 sync .\out "s3://$FrontendBucket/" --delete
if ($LASTEXITCODE -ne 0) { throw "S3 sync failed (exit code $LASTEXITCODE)." }
Set-Location ..

# 4. Final summary
$CfUrl = terraform -chdir=terraform output -raw cloudfront_url
Write-Host "Deployment complete!" -ForegroundColor Green
Write-Host "CloudFront URL : $CfUrl" -ForegroundColor Cyan
if ($CustomUrl) {
    Write-Host "Custom domain  : $CustomUrl" -ForegroundColor Cyan
}
Write-Host "API Gateway    : $ApiUrl" -ForegroundColor Cyan