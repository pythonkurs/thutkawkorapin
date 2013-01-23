import untangle

def assignment2():
    xml_file     = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    doc          = untangle.parse(xml_file)
    outages      = doc.NYCOutages.outage
    repair_count = 0
    for item in outages :
        if item.reason.cdata == 'REPAIR':
            repair_count += 1
    print "%d/%d" % (repair_count, len(outages))
