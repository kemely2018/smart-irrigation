resource "aws_lambda_function" "cloud_lambda" {
  function_name = "irrigation_cloud_handler"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.12"
  handler       = "handler.handler"

  filename         = "cloud_lambda.zip"
  source_code_hash = filebase64sha256("cloud_lambda.zip")

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.irrigation_table.name
    }
  }
}
