#!/usr/bin/env python3

from azure.common.client_factory import get_client_from_cli_profile, get_azure_cli_credentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource import SubscriptionClient

from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

from pprint import pprint

from msrestazure.azure_active_directory import MSIAuthentication
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

credentials, sub_id = get_azure_cli_credentials()

print(credentials)

# exit(0)
# subscriptionClient = get_client_from_cli_profile(SubscriptionClient)

subscriptionClient = SubscriptionClient(credentials)

for subscription in subscriptionClient.subscriptions.list():
    subscription_id = subscription.subscription_id

    print("Subcription ID: {} Name: {} State: {} \n\tAuth: {}".format(subscription.subscription_id, subscription.display_name, subscription.state, subscription.authorization_source))
    print("\tLocation: {} \n\tQuota: {} \n\tSpendLimit: {}".format(subscription.subscription_policies.location_placement_id,
            subscription.subscription_policies.quota_id,
            subscription.subscription_policies.spending_limit
            ))

    storageClient = StorageManagementClient(credentials, subscription_id)
    storage_accounts = storageClient.storage_accounts.list()
    for sa in storage_accounts:
        print("\t\t{}".format(sa.id))


