module "staging" {
  source             = "github.com/fojiglobal/clovis-tf-modules//staging?ref=v1.1.1" 
  vpc_cidr           = local.vpc_cidr
  env                = local.env
  public_subnets     = local.public_subnets
  private_subnets    = local.private_subnets
  pub-sub-name       = "pub-sub-1"
  user_data          = filebase64("web.sh")
  public_sg_egress   = local.public-sg-egress
  public_sg_ingress  = local.public-sg-ingress
  private_sg_egress  = local.private-sg-egress
  private_sg_ingress = local.private-sg-ingress
  bastion_sg_ingress = local.bastion-sg-ingress
  bastion_sg_egress  = local.bastion-sg-egress
  ami_id             = "ami-036841078a4b68e14"
  alb_ssl_cert_arn   = data.aws_acm_certificate.alb_cert.arn
  alb_ssl_profile    = "ELBSecurityPolicy-2016-08"
  dns_zone           = data.aws_route53_zone.fojiapps.zone_id
  dns_name           = "stage.fojiapps.com"
  alb_rule_condition = ["stage.fojiapps.com", "www.stage.fojiapps"]
}


output "vpc_id" {
  value = module.staging.vpc_id
}

output "pub_subnet_id" {
  value = module.staging.public_subnet_ids
}

