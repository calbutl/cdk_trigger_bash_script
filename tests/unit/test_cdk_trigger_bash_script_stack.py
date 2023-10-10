import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_trigger_bash_script.cdk_trigger_bash_script_stack import CdkTriggerBashScriptStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_trigger_bash_script/cdk_trigger_bash_script_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkTriggerBashScriptStack(app, "cdk-trigger-bash-script")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
