#!/usr/bin/env node
import { App } from 'aws-cdk-lib';
import 'source-map-support/register';
import { JupyterExecutorStack } from '../lib/JupyterExecutorStack';

const app = new App();
new JupyterExecutorStack(app, 'JupyterExecutorStack', {
    env: { region: 'ap-northeast-1', account: process.env.CDK_DEFAULT_ACCOUNT }
});