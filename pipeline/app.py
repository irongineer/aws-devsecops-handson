#!/usr/bin/env python3
import os
import yaml
from aws_cdk import core as cdk
from aws_cdk import core

from appsec_workshop.appsec_workshop_stack import AppsecWorkshopStack

with open("./config.yaml") as stream:
    config = yaml.safe_load(stream)

app = core.App()
AppsecWorkshopStack(app, "AppSecWorkshopStack", config)

app.synth()
