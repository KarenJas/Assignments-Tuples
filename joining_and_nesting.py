#5. Advanced Tuple Techniques: Joining and Nesting in Python

def merge_catalogs(*catalogs):
    #Initialize combined catalog
    combined_catalog = ()
    #Itterate through catalogs
    for catalog in catalogs:
        #Combine catalogs
        combined_catalog += catalog
    return combined_catalog


catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Merge catalogs
combined_catalog = merge_catalogs(catalog1, catalog2)

#Display combined catalog
for product in combined_catalog:
    print(product)
