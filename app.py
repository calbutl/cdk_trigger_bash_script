#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lib.trigger_bash_script_stack import TriggerBashScriptStack


app = cdk.App()

TriggerBashScriptStack(app, "TriggerBashScriptStack")

app.synth()
