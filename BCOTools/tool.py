import os,sys
import json
from optparse import OptionParser, __version__
from collections import OrderedDict

def main():
    usage = "\n%prog  [options]"
    parser = OptionParser(usage, version="%prog " + __version__)
    # parser.add_option("--GalaxyHistory", action="store", dest="GalaxyHistory", help="Input GalaxyHistory File")
    parser.add_option("--provenance_domain_name", action="store", dest="provenance_domain_name", help="Input provenance_domain.name")
    parser.add_option("--provenance_domain_version", action="store", dest="provenance_domain_version", help="Input provenance_domain_version")
    parser.add_option("--provenance_domain_license", action="store", dest="provenance_domain_license", help="Input provenance_domain_license")
    parser.add_option("--provenance_domain_created", action="store", dest="provenance_domain_created", help="Input provenance_domain_created")
    parser.add_option("--provenance_domain_modified", action="store", dest="provenance_domain_modified", help="Input provenance_domain_modified")
    parser.add_option("--orcid", action="store", dest="orcid", help="Input orcid")
    parser.add_option("--affiliation", action="store", dest="affiliation", help="Input affiliation")
    parser.add_option("--name", action="store", dest="name", help="Input name")
    parser.add_option("--email", action="store", dest="email", help="Input email")
    parser.add_option("--contribution", action="store", dest="contribution", help="Input contribution")
    # parser.add_option("--name", action="store", dest="name", help="Input name")
    # parser.add_option("--email", action="store", dest="email", help="Input email")


    parser.add_option("--jsonFile", action="store", dest="jsonFile", help="Output json file")

    (options, args) = parser.parse_args()
    # for input in ([options.username, options.password]):
    #     if not (input):
    #         parser.print_help()
    #         sys.exit(0)
    # GalaxyHistory = options.GalaxyHistory
    provenance_domain_name = options.provenance_domain_name
    provenance_domain_version = options.provenance_domain_version
    provenance_domain_license = options.provenance_domain_license
    provenance_domain_created = options.provenance_domain_created
    provenance_domain_modified = options.provenance_domain_modified
    orcid = options.orcid
    affiliation = options.affiliation
    name = options.name
    email = options.email
    contribution = options.contribution
    outFile = options.jsonFile

    dic = OrderedDict()
    dic['provenance_domain_name'] = provenance_domain_name
    dic['provenance_domain_version'] = provenance_domain_version
    dic['provenance_domain_license'] = provenance_domain_license
    dic['provenance_domain_created'] = provenance_domain_created
    dic['provenance_domain_modified'] = provenance_domain_modified
    dic['orcid'] = orcid
    dic['affiliation'] = affiliation
    dic['name'] = name
    dic['email'] = email
    dic['contribution'] = contribution

    with open(outFile,'w') as f:
        json.dump(dic,f)



if __name__ == '__main__':
    main()
