# [intro to terraform (intermediate)](https://youtu.be/xskzEkoisNE)

Today I talk about terraform - an infrastructure-as-code tool for provisioning resources (often cloud resources)

## Interactive examples

### Bash

```Bash
mkdir terraform_examples
cd !$

git init .
nano aws_provider.tf

type tf

terraform init
git status
ls .terraform
nano .terraform.lock.hcl
nano .gitignore

git add .terraform.lock.hcl
git add aws_provider.tf .gitignore

git commit -m 'set up aws provider'
terraform fmt

nano instance.tf
git add instance.tf

terraform plan
terraform apply

terraform destroy
terraform --help

nano .pre-commit-config.yaml
git add .pre-commit-config.yaml

pre-commit install
git commit -m 'add ec2 instance'
```
