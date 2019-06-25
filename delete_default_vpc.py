##################################################################
"""
Deletes "Default VPC" if no resources exist in VPC

"""
##################################################################

import mod_awstoolbox
import logging
import time


def deleteDefaultVPC_AllAccts():
    '''
    Delete default VPCs in all regions for all AWS accts
    Default VPC will only be deleted if no resources is using it
    '''
    print('<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    logging.info('<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    org_accts = mod_awstoolbox.get_aws_org_accts()
    # print(org_accts[5])
    for acct in org_accts:
        acct = (acct.split(',')[0])
        print('For AWS account ' + acct + ':')
        logging.info('For AWS account ' + acct + ':')
        mod_awstoolbox.delete_default_vpc(acct)
        print('=============================')


def deleteDefaultVPC_OneAccts(acctNumber):
    '''
    Delete default VPCs in all regions for one AWS acct
    Default VPC will only be deleted if no resources is using it
    '''
    print('<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    logging.info('<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('For AWS account ' + acctNumber + ':')
    logging.info('For AWS account ' + acctNumber + ':')
    mod_awstoolbox.delete_default_vpc(acctNumber)
    print('=============================')


def delete_default_vpcs(acct_target):

    run_all_accts = False

    if str(acct_target) == "all":
        run_all_accts = True

    if run_all_accts == True:
        deleteDefaultVPC_AllAccts()
    else:
        deleteDefaultVPC_OneAccts(acct_target)



if __name__ == "__main__":
    delete_default_vpcs('all')
