"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.filter(Brand.id==8).all()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name=="Corvette", Model.brand_name=="Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(Brand.discontinued.isnot(None) | Brand.founded < 1950).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name.isnot("Chevrolet")).all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model, Brand).filter(Model.year == year).join(Brand)

    for name, brand_name, headquarters in models.all():
        print Model.name, Model.brand_name, Brand.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Brand, Model).join(Model)

    for brand_name, model_name in brands.all():
        print brand_name.name, model_name.name 

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    search_results = []
    brands = Brand.query.filter(Brand.name == mystr | 
                                            Brand.name.like('%' + mystr + '%'))

    for brand in brands.all():
        search_results.append(brand)

def get_models_between(start_year, end_year):
    filtered_models = []
    models = Model.query.filter(Model.year > start_year, 
                                Model.year < end_year)
    for model in models.all():
        filtered_models.append(model)

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#That query returns <flask_sqlalchemy.BaseQuery object at 0x10cb75390> which is Object
# it's inherited from the flask_sqlalchemy model.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An associative table is a database table that exists to bridge the gap between
# two other tables. It has a one to many relationship with the other tables, this 
# is useful because otherwise the tables would rely on a many to many relationships
# which is not supported by SQL.
