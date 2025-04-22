from pprint import pprint

import boto3


def list_records(hosted_zone_id):
    client = boto3.client('route53')
    records = client.list_resource_record_sets(
        HostedZoneId=hosted_zone_id
    )

    pprint(records)


if __name__ == "__main__":
    HOSTED_ZONE_ID = "xxxxxxxxxxxxxxxxxxx"

    list_records(HOSTED_ZONE_ID)
