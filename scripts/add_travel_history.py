import sys

changes = {
  ## IRANIAN
  "Australia/NSW05/2020": "Iran",
  "Australia/NSW06/2020": "Iran",
  "Canada/BC_37_0-2/2020": "Iran",
  "NewZealand/01/2020": "Iran",

  ## LOMBARDY
  "Brazil/SPBR-01/2020": "Lombardy",
  "Brazil/SPBR-02/2020": "Lombardy",
  "Finland/FIN-25/2020": "Lombardy",
  "Germany/Baden-Wuerttemberg-1/2020": "Lombardy",
  "Mexico/CDMX/InDRE_01/2020": "Lombardy",

  ## HUBEI / WUHAN
  "Canada/ON/PHL2445/2020": "Hubei",
  "Canada/ON/VIDO-01/2020": "Hubei",
  "Italy/INMI1-cs/2020": "Hubei",
  "USA/WA1/2020": "Hubei",
}

with open(sys.argv[1], 'r') as fhi:
  with open(sys.argv[2], 'w') as fho:
    # HEADER
    fields = fhi.readline().strip().split("\t")
    fields.insert(8, "division_exposure")
    print("\t".join(fields), file=fho)

    for line in fhi:
      fields = line.strip().split("\t")
      if fields[0] in changes:
        print("CHANGE", fields[0], fields[7], changes[fields[0]])
        fields.insert(8, changes[fields[0]])
      else:
        fields.insert(8, fields[7])
      print("\t".join(fields), file=fho)
