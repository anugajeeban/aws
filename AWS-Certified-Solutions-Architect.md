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

You have millions of objects in an s3 bucket. You are storing data that may require light real-time access, and that you can recreate if you need to.  Which of the following is the cheapest suitable storage class to use?

1. Standard
2. S3 One Zone - IA
3. S3 Standard - IA
4. Glacier

Answer : S3 Standard - IA


S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB retrieval fee. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files. 


---

Your are an EC2 Administrator. You create an EC2 instance, and attach an EBS volume. Two weeks later, your supervisor informs you that the data on the EBS volume must be encrypted.  What must you do to encrypt the existing EBS volume?

1. In the EC2 Dashboard, select the EBS volume, and under actions select the encrypt volume
2. You can enables encryption on a volume by changing the volume type to an instance store volume. Instance store volumes are automatically encrypted
3. It is not possible to encrypt an existing EBS volume. You must delete the existing volume and all existing data will be lost. You will have to recreate the data on the new encrypted volume

4. It is not possible to encrypt an existing EBS volume. You can take a snapshot of the unencrypted volume. Once the snapshot is taken, copy the snapshot and enable encryption on the copy so that the target snapshot is encrypted. Once the target snapshot is created, you can attach a new encrypted volume to the EC2 instance, and restore the encrypted snapshot to a new volume.
