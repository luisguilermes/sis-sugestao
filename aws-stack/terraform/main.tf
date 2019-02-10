provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "{{S3_BUCKET_NAME}}"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}

//resource "aws_kms_key" "a" {
//  description             = "KMS key 1"
//  deletion_window_in_days = 10
//}

resource "aws_sqs_queue" "terraform_queue" {
  name                              = "{{QUEUE_NAME}}"
//  kms_master_key_id                 = "${aws_kms_key.a.key_id}"
//  kms_data_key_reuse_period_seconds = 300
}
