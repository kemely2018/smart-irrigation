resource "aws_dynamodb_table" "irrigation_table" {
  name         = "irrigation_events"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "timestamp"

  attribute {
    name = "timestamp"
    type = "S"
  }
}
