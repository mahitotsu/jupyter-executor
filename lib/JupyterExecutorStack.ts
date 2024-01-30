import { CfnOutput, Duration, RemovalPolicy, Stack, StackProps } from "aws-cdk-lib";
import { DockerImageCode, DockerImageFunction, FunctionUrlAuthType, InvokeMode } from "aws-cdk-lib/aws-lambda";
import { LogGroup, RetentionDays } from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class JupyterExecutorStack extends Stack {
    constructor(scope: Construct, id: string, props: StackProps) {
        super(scope, id, props);

        const executor = new DockerImageFunction(this, 'Function', {
            code: DockerImageCode.fromImageAsset(`${__dirname}/../assets`),
            memorySize: 512,
            timeout: Duration.seconds(30),
        });
        new LogGroup(executor, 'LogGroup', {
            logGroupName: `/aws/lambda/${executor.functionName}`,
            retention: RetentionDays.ONE_DAY,
            removalPolicy: RemovalPolicy.DESTROY,
        });
        const endpoint = executor.addFunctionUrl({
            invokeMode: InvokeMode.BUFFERED,
            authType: FunctionUrlAuthType.NONE,
        });

        new CfnOutput(this, 'EndpointUrl', { value: endpoint.url });
    }
}