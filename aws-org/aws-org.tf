resource "aws_organizations_organization" "org" {
  aws_service_access_principals = [
    "cloudtrail.amazonaws.com",
    "config.amazonaws.com",
  ]

  feature_set = "ALL"

}

resource "aws_organizations_account" "cs_secops" {
  name  = "cs2-secops"
  email = "cs2-secops@fojilabs.net"
  parent_id = aws_organizations_organizational_unit.cs2_secops.id
}

resource "aws_organizations_account" "cs2_sandbox" {
  name  = "cs2-sandbox"
  email = "cs2-sandbox@fojilabs.net"
  parent_id = aws_organizations_organizational_unit.cs2_sandbox.id
}


resource "aws_organizations_organizational_unit" "cs2_secops" {
  name      = "secops"
  parent_id = aws_organizations_organization.org.roots[0].id
}

resource "aws_organizations_organizational_unit" "cs2_sandbox" {
  name      = "sandbox"
  parent_id = aws_organizations_organization.org.roots[0].id
}