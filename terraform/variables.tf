variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "twin"
}

variable "environment" {
  description = "Deployment environment (dev, test, prod)"
  type        = string
  default     = "dev"
}

variable "bedrock_model_id" {
  description = "AWS Bedrock model ID for LLM responses"
  type        = string
  default     = "amazon.nova-micro-v1:0"
}

variable "lambda_timeout" {
  description = "Timeout in seconds for Lambda function"
  type        = number
  default     = 60
}

variable "api_throttle_burst_limit" {
  description = "Burst limit for API Gateway throttling"
  type        = number
  default     = 10
}

variable "api_throttle_rate_limit" {
  description = "Rate limit for API Gateway throttling"
  type        = number
  default     = 5
}

variable "use_custom_domain" {
  description = "Whether to use a custom domain with CloudFront and Route53"
  type        = bool
  default     = false
}

variable "root_domain" {
  description = "Root domain name for custom domain (e.g., example.com)"
  type        = string
  default     = ""
}
