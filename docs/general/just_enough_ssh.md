# Just Enough SSH

## Intro
This article treats SSH like a car. You want know how to use car so it can get your places, but you don't really care about the finer points unless they matter.

## Assumptions
This assumes you need to create a server and get code on it using:
* AWS EC2 instances launched from console with "Launch Templates"
* Code stored in Bitbucket


## Private and Public key pair
* The private key and public key are a pair.
* The private key is generated. From that the public key can always be recovered.
* The private key only generates one public key and its always the same.
* Once generated the public key can be given to multiple servers eg the same key could be used to SSH onto multiple servers.

## How SSH works
Add diagram

1. The client(user) machine sends its private key to the the server
2. The server uses the private key to generate the public key and matches it to the public key it has on file
3. The authentication is complete and the session starts

## General setup
* Private key on the machine you are going to be SSHing from.
* Public key on the machine you are going to be SSHing into.
* Said another way, the private key is for the machine that needs to be authenticated, the public key is for the machine doing the authenticating

## Other Bits
* SSH keys must have 0600 permissions. Run `chmod <filename> 0600` to set.
* Present the SSH key specifically, so that you can know if its the right one in case your machine already has multiple. Run `ssh -i ~/.ssh/<key_nam>` to do so. If you do not, then it will automatically try a bunch of defaults and you won't know which one is right.
* To troubleshoot use `-v` option for verbosity, ie `ssh -v -i ~/.ssh/<key_nam>`. That will give you enough to Google

## How to setup SSH from scratch for AWS EC2

### Generate the key
1. From EC2 console home, on the left under "Network & Security" click on "Key Pairs"
1. At the top click "create key pair"
1. Fill out the form. For name I use my_company_use_case_# eg tbe_access_server_1. Leave the defaults. Add a new tag called description, where you write out more clearly what the key is for.
1. Key_name.pem will populate in your downloads
### Place private key in correct spot with correct perms
1. Copy key_name.pem to ~/.ssh/key_name. The file extension is for a format we won't use, so remove it.
2. run `chmod 0600 <key_name>` These permissions are required for SSH keys.
### Generate public key
1. run `keygen -y -f <key_name> > <key_name>.pub`. This generates the public key. The .pub suffix tell you this is the public key for the private key of the same name.
### Place public key on EC2 instance
1. From EC2 console home, on the left under "Instances" select "Launch Templates"
1. Select the desired template. From "Actions", select "Modify Template (Create a new version)"
1. Under "Key pair (login)" select the key that was created above. This places the public key in the correct spot(authorized keys) at startup.
1. Select other settings as desired and create the new template version
### Connect to the instance
1. Launch instance from created template version
1. The public dns can be found in the details tab for the running instance with a format like ec1-45-239-006-050.us-west-1.compute.amazonaws.com
1. SSH into the instance with `ssh -i /.ssh/key_name <user>@<public_dns>` eg `ssh -i /.ssh/tbe_access_server_1 ubuntu@ec1-45-239-006-050.us-west-1.compute.amazonaws.com`

## Configure Bitbucket and add public key

To be finished at some point ...

### Generate key
### Place private key in correct spot with correct perms
### Generate public key
### Place public key in bitbucket
### test
