import boto3


client = boto3.client('autoscaling')

resp = client.describe_auto_scaling_groups(AutoScalingGroupNames=['runner'])
asg, = resp['AutoScalingGroups']
print(asg['LaunchTemplate'])
