import financedatabase as fd

# Initialize the Equities database
equities = fd.Equities()

# Obtain all countries from the database
equities_countries = equities.options("country")

# Obtain a selection from the database
equities_united_states = equities.select(market="Bolsa de Comercio de Santiago de Chile")



