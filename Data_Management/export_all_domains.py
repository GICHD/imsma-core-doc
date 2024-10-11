#Runs through all domains in a gdb and exports them to csv. Runs in python (open new notebook in pro)


arcpy.env.workspace = "C:\\" #link to the folder where you want to store the output
gdb = "C:\\"  #link to the database
arcpy.env.overwriteOutput = True  

domains = arcpy.da.ListDomains(gdb)  

for domain in domains:  
     if domain.domainType == 'CodedValue':  
         domain_name = domain.name  
         print ('Exporting {0} coded values to table in {1}'.format(domain_name, gdb)  )
         coded_value_list = domain.codedValues  
         print ("The coded values / descriptions are"  )
         for value, descrip in coded_value_list.items():  
             print ("{0} : {1}".format(value, descrip)  )
         out_table_name = domain_name.lower() + ".csv" 
         arcpy.DomainToTable_management(gdb, domain_name, out_table_name, "item", "descrip")  
     else:  
         print ("{0} not a coded value domain. Passing it up.".format(domain.name) )
