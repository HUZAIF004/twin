terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}


# Required by AWS specifically for CloudFront SSL certificates
provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"
}