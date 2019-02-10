
output "sqs_id" {
  value = "${aws_sqs_queue.terraform_queue.id}"
}

output "sqs_name" {
  value = "${aws_sqs_queue.terraform_queue.name}"
}