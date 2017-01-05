from webargs import validate

PRICE = validate.Regexp(r'^[0-9]+\.[0-9]{2}$')
