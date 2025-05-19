<<<<<<< HEAD

# Azure CLI Neon Extension #
This is an extension to Azure CLI to manage Neon Postgres resources.

## How to use ##
#### Install the extension ####
=======
# Azure CLI Neon Extension #

This is an extension to Azure CLI to manage Neon Postgres resources.

## How to use ##

### Install the extension ###

>>>>>>> upstream/main
Install this extension using the below CLI command:
```
az extension add --name neon
```

<<<<<<< HEAD
#### Check the version ####
=======
### Check the version ###

>>>>>>> upstream/main
```
az extension show --name neon --query version
```

<<<<<<< HEAD
#### Connect to Azure subscription ####
=======
### Connect to Azure subscription ###

>>>>>>> upstream/main
```
az login
az account set -s {subs_id}
```

<<<<<<< HEAD
#### Create a resource group (or use an existing one) ####
=======
### Create a resource group (or use an existing one) ###

>>>>>>> upstream/main
```
az group create -n demoResourceGroup -l eastus
```

## Available Commands ##

<<<<<<< HEAD
### Create a Neon Postgres Instance ###
```
az neon postgres create --resource-group {resource_group} --name {resource_name} --user-details '{"first-name": "{user_first_name}", "last-name": "{user_last_name}", "email-address": "{user_email}", "upn": "{user_upn}", "phone-number": "{user_phone}"}' --company-details '{"company-name": "{company_name}", "office-address": "{office_address}", "country": "{country}", "domain": "{domain}", "number-of-employees": {number_of_employee}}' --partner-organization-properties '{"organization-id": "{org_id}", "org-name": "{partner_org_name}", "single-sign-on-properties": {"single-sign-on-state": "{sso_state}", "enterprise-app-id": "{app_id}", "single-sign-on-url": "{sso_url}", "aad-domains": ["{domain}"]}}' --tags "{key:value}" --location {location}
```

### Show a Neon Postgres Organization ###
=======
### Organization Commands ###

#### Create a Neon Postgres Organization ####

```
az neon postgres organization create --resource-group {resource_group} --name {resource_name} --user-details '{{"first-name": "{user_first_name}", "last-name": "{user_last_name}", "email-address": "{user_email}", "upn": "{user_upn}", "phone-number": "{user_phone}"}}' --marketplace-details '{{"subscription-id": "{subscription_id}", "subscription-status": "{subscription_status}", "offer-details": {{"publisher-id": "{publisher_id}", "offer-id": "{offer_id}", "plan-id": "{plan_id}", "plan-name": "{plan_name}", "term-unit": "{term_unit}", "term-id": "{term_id}"}}}}' --company-details '{{"company-name": "{company_name}", "office-address": "{office_address}", "country": "{country}", "domain": "{domain}", "number-of-employees": {number_of_employee}}}' --partner-organization-properties '{{"organization-id": "{org_id}", "org-name": "{partner_org_name}", "single-sign-on-properties": {{"single-sign-on-state": "{sso_state}", "enterprise-app-id": "{app_id}", "single-sign-on-url": "{sso_url}", "aad-domains": ["{domain}"]}}}}' --tags "{key:value}" --location {location}
```

#### Show a Neon Postgres Organization ####

>>>>>>> upstream/main
```
az neon postgres organization show --resource-group {resource_group} --name {resource_name}
```

<<<<<<< HEAD
### Delete a Neon Postgres Organization ###
=======
#### Delete a Neon Postgres Organization ####

>>>>>>> upstream/main
```
az neon postgres organization delete --resource-group {resource_group} --name {resource_name}
```

<<<<<<< HEAD
### List Neon resources by subscription ID ###
=======
#### List Neon Organizations by Subscription ####

>>>>>>> upstream/main
```
az neon postgres organization list --subscription {subscription_id} --resource-group {resource_group}
```

<<<<<<< HEAD
### Update a Neon Postgres Organization (without location and marketplace details) ###
```
az neon postgres organization update --resource-group {resource_group} --name {resource_name} --user-details '{"first-name": "{user_first_name}", "last-name": "{user_last_name}", "email-address": "{user_email}", "upn": "{user_upn}", "phone-number": "{user_phone}"}' --company-details '{"company-name": "{company_name}", "office-address": "{office_address}", "country": "{country}", "domain": "{domain}", "number-of-employees": {number_of_employee}}' --partner-organization-properties '{"organization-id": "{org_id}", "org-name": "{partner_org_name}", "single-sign-on-properties": {"single-sign-on-state": "{sso_state}", "enterprise-app-id": "{app_id}", "single-sign-on-url": "{sso_url}", "aad-domains": ["{domain}"]}}' --tags "{key:value}"
=======
#### Update a Neon Postgres Organization ####

```
az neon postgres organization create --resource-group {resource_group} --name {resource_name} --user-details '{{"first-name": "{user_first_name}", "last-name": "{user_last_name}", "email-address": "{user_email}", "upn": "{user_upn}", "phone-number": "{user_phone}"}}' --marketplace-details '{{"subscription-id": "{subscription_id}", "subscription-status": "{subscription_status}", "offer-details": {{"publisher-id": "{publisher_id}", "offer-id": "{offer_id}", "plan-id": "{plan_id}", "plan-name": "{plan_name}", "term-unit": "{term_unit}", "term-id": "{term_id}"}}}}' --company-details '{{"company-name": "{company_name}", "office-address": "{office_address}", "country": "{country}", "domain": "{domain}", "number-of-employees": {number_of_employee}}}' --partner-organization-properties '{{"organization-id": "{org_id}", "org-name": "{partner_org_name}", "single-sign-on-properties": {{"single-sign-on-state": "{sso_state}", "enterprise-app-id": "{app_id}", "single-sign-on-url": "{sso_url}", "aad-domains": ["{domain}"]}}}}' --tags "{key:value}" --location {location}
```

### Project Commands ###

#### Create a Neon Postgres Project with in an Organization ####

```
az neon postgres project create --resource-group {resource_group} --organization-name {organization_name} --name {project_name} --region {region} --pg-version {pg_version} --branch '{{"branch-name": "{banch_name}", "database-name": "{database_name}", "role-name": "{reole_name}""}}'
```

#### Show a Neon Postgres Project in an Organization ####

```
az neon postgres project show --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id}
```

#### List Neon Postgres Projects under an Organization ####

```
az neon postgres project list --resource-group {resource_group} --organization-name {organization_name}
```

#### Delete a Neon Postgres Project in an Organization ####

```
az neon postgres project delete --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id}
```

### Branch Commands ###

#### Create a Branch in a Neon Postgres Project ####

```
az neon postgres branch create --resource-group {resource_group} --organization-name {organization_name} --project-name {project_id} --project-id {project_id} --branch-name {branch_name} --role-name {role_name} --database-name {database_name}
```

#### Show a Branch in a Neon Postgres Project ####

```
az neon postgres branch show --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id} --branch-id {branch_id}
```

#### List Branches in a Neon Postgres Project ####

```
az neon postgres branch list --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id}
```

#### Delete a Branch in a Neon Postgres Project ####

```
az neon postgres branch delete --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id} --branch-id {branch_id}
```

### Neon Database Commands ###

#### List Databases in a Neon Postgres Branch ####

```
az neon postgres database list --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id} --branch-id {branch_id}
```

### Neon Role Commands ###

#### List Roles in a Neon Postgres Branch ####

```
az neon postgres neon-role list --resource-group {resource_group} --organization-name {organization_name} --project-id {project_id} --branch-id {branch_id}

>>>>>>> upstream/main
```

If you have issues, please give feedback by opening an issue at https://github.com/Azure/azure-cli-extensions/issues.
