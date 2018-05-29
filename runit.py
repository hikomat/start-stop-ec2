import boto3
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EC2 starter/stopper/status checker')
    parser.add_argument('action', choices=['start', 'stop', 'state'], help='EC2 action to perform')
    parser.add_argument('instance_id', type=str, help='EC2 instance ID')
    # parser.add_argument('dryrun', ddeaction='store_true', help='EC2 instance ID')
    
    args = parser.parse_args()

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(args.instance_id)
    if args.action == 'state':
        print(instance.state['Name'])        
    if args.action == 'start':
        if instance.state['Name'] == 'stopped':
            # instance.start(DryRun=True)
            instance.start()
            print('instance started')
        else:
            print('instance already started')
    if args.action == 'stop':
        if instance.state['Name'] in ('running', 'pending'):
            instance.stop()
            print('instance stopped')
        else:
            print('instance already stopped')
