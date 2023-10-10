import os
from aws_cdk import (
    Stack,
    Duration,
    BundlingOptions,
    triggers,
    aws_lambda as lambda_,
    aws_iam as iam,
)
from constructs import Construct


class TriggerBashScriptStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, 
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = iam.Role(self, f"TriggerBashScriptLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name='TriggerBashScriptLambda',
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
            ],
        )
        
        lambda_dir = os.path.join(os.path.dirname(__file__), '..', "lambda")
        triggers.TriggerFunction(self, f"BashScriptTriggerFunction",
            function_name=f"TriggerBashScript",
            role=lambda_role,
            runtime=lambda_.Runtime.NODEJS_18_X,
            timeout=Duration.seconds(20),
            handler="myScriptRunner.handler",
            code=lambda_.Code.from_asset(
                lambda_dir,
                bundling=BundlingOptions(
                    image=lambda_.Runtime.NODEJS_18_X.bundling_image,
                    command=[
                        "bash", "-c",
                        ' && '.join([
                            "chmod +x myScript.sh",
                            "npm install --prefix /asset-output --cache /asset-output/npm_cache owoify-cli",
                            "cp -au . /asset-output",
                        ]),
                    ],
                ),
            ),
            environment={
                "POSITIVE_APHORISM": "Do what you love and you'll never work a day in your life.",
            },
        )
