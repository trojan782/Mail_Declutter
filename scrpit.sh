echo '[all]' > inventory

aws --region us-west-2 \
ec2 describe-instances \
--filters \
"Name=instance-state-name,Values=running" \
"Name=instance-id,Values=i-069138d9e651b77cb" \
--query 'Reservations[*].Instances[*].[PublicIpAddress]' \
--output text >> inventory