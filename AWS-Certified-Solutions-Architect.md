# You have been asked to advice a junior college how to explicity deny traffic from an EC2 instance to specific remote 
internet FQDN. What advice would you give?

1. Use a security group attached to the VPC and explicitly deny traffic to FQDN
2. use a security group attached to the instance and explicitly deny traffic to the FQDN
3. Implement a proxy service in the VPC, adjust route tables, and use the proxy server to deny access to the remote
hosname
4. Use a NACl on the subnet that the EC2 instance is on, and deny traffic from the EC2 instance to the FQDN

Answer 4: Only NACLs can explicity 'block' anything. 

-----

# Your CIO has approached you with a Problem. You currently run a technical tecaching business and provide online learning to students. The service is hosted on premises, and you are unable to expand capacity.
  A full miration into AWS is not an option. The business needs time to adjust to the idea, and you have no infrastructre configured inside your recently created AWS account. 

The business needs to resolve the performance issues on the media delivery server. They need it done at the lowest
possible cost point, and ideally would also improve performance to internation students. What would you suggest?


Migrate the media to an EC2 instance, and use Amazon S3 as a content delivery network CDN


---

# You have millions of objects in an s3 bucket. You are storing data that may require light real-time access, and that you can recreate if you need to.  Which of the following is the cheapest suitable storage class to use?

1. Standard
2. S3 One Zone - IA
3. S3 Standard - IA
4. Glacier

Answer : S3 Standard - IA

S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB retrieval fee. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files. 


---

# Your are an EC2 Administrator. You create an EC2 instance, and attach an EBS volume. Two weeks later, your supervisor informs you that the data on the EBS volume must be encrypted.  What must you do to encrypt the existing EBS volume?

1. In the EC2 Dashboard, select the EBS volume, and under actions select the encrypt volume
2. You can enables encryption on a volume by changing the volume type to an instance store volume. Instance store volumes are automatically encrypted
3. It is not possible to encrypt an existing EBS volume. You must delete the existing volume and all existing data will be lost. You will have to recreate the data on the new encrypted volume

4. It is not possible to encrypt an existing EBS volume. You can take a snapshot of the unencrypted volume. Once the snapshot is taken, copy the snapshot and enable encryption on the copy so that the target snapshot is encrypted. Once the target snapshot is created, you can attach a new encrypted volume to the EC2 instance, and restore the encrypted snapshot to a new volume.

Answer : 4

---


# Which of the following services or service features are natively highly available in a region and can cope with a AZ 
  failure without itself failing?


1. Software VPN (Open VPN Rrunning on EC2)
2. Internet Gateway
3. Dynamic Hardware VPC VPN
4. Virtual Private Gateway


The third answer is correct because all three: Internet Gateway, Virtual Private Gateway, and Hardware VPN all do not 
depend on an Availability Zone.  A VPN connection is dependent on the hardware used on-premise and is not dependent 
on an Availability Zone.  The question asks which services can survive an AZ failure without the component itself 
failing.  Option A would be wrong because it is running on an EC2 instance and therefore is dependent on an 
Availability Zone.  Option D is not using AWS hardware, so it is not dependent on an AZ.  

---

# Your company has just employed ten student for one week, and it is your task to provide them with access to AWS 
  through IAM. Your supervisor has come to you and said that he wants to be able to track these students as a group, 
  rater than individually. Beacause of this, he as requested for them to all have same login ID but completely 
  different passwords. Which of the following is the best way to achive this?

1. It isnt possible to thave same login ID for multiple IAM users of the same account
2. user Multi Factor Authentication to verify each user, and they will all be able to use same login
3. Create various groups. and add each user with the same login ID to different groups. The user can login with their 
own group ID
4. Create a separate login ID, but give each IAM user the same alias so that each one can login with their alias.

Answer: 1

---

# Currently your helping with the design and architect a highly-available application. After building the initial 
evnironment, you found that part of your application dose not work correctly until port 443 is added to the security 
group.  After adding port 443 to the appropriate security group, how much time will it take before the changes are 
applied and the application begins working correctly?


1. Generally, it takes 2-5 minutes for the rules to propagate
2. It will take 60 seconds for the rules to apply to all Availability Zones with in the region
3. Immeditaley after a reboot of the EC2 instances belong to that security group
4. Changes apply instantely to the security group, and the applicatoin should be able to immeditely respond to 443 requests.

Answer: 4

---

# Your business generates a large amount of financial data within it's SQL-backed financial application. You have been
asked to suggest an AWS product which will allow storage of that data to be used for long term reporting, querying, 
forecasting, and business intelligence.  Which AWS product should you suggest?

1. Athena
2. Glacier
C. EMR
D. Redshift

Answer: D

---
