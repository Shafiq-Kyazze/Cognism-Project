from Database.models import COMPANIES, LOCATION, LEGAL
from Database.database import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
s = Session()


class Namecomponents():
    """Class that returns that returns name components of the various companies"""
    def __init__(self):
        self.components = {} #Dictionary to hold the results

    def get_name_components(self, comp_name):
        self.components.update({"raw":comp_name,  "base_name": None , "location": None, "legal": None}) #Adding the raw input into the results components dictionary and setting the other keys to None to ensure no mix up

        """Splitting the raw input into 3 segments and strippping certain characters away from the segments"""
        split_comp_name = comp_name.split(' ') # items in split comp_names

        #Try block to deal with situations where there less than 3 items in the comp_name string
        try:
            segments = [ split_comp_name[0].strip("    ,.(){}[]#@''    "),
                         split_comp_name[1].strip("    ,.(){}[]#@''    "),
                         ' '.join(split_comp_name[2:]).strip("    ,.(){}[]#@''    ") ] #Used -1 instead of 2 because of spaced strings such as united kingdom , united states etcetra
        except IndexError: #If there are less than 3 items in the segments list
            segments = [
                part.strip("    ,.(){}[]#@''    ") for part in split_comp_name
            ]

        """loop to search for item in database"""
        for item in segments:
            if s.query(COMPANIES).filter(COMPANIES.company_name.ilike(f'%{item}%')).first() is not None and self.components["base_name"] is None :
                result = s.query(COMPANIES).filter(COMPANIES.company_name.ilike(f'%{item}%')).first()
                self.components.update({"base_name": result.__dict__['company_name'].lower()} )

            elif s.query(LOCATION).filter(LOCATION.location.ilike(f'%{item}%')).first() is not None and self.components["location"] is None :
                result = s.query(LOCATION).filter(LOCATION.location.ilike(f'%{item}%')).first()
                self.components.update({"location": result.__dict__['location'].lower() })

            elif s.query(LEGAL).filter(LEGAL.legal_term.ilike(f'%{item}%')).first() is not None and self.components["legal"] is None :
                result = s.query(LEGAL).filter(LEGAL.legal_term.ilike(f'%{item}%')).first()
                self.components.update({"legal": result.__dict__['legal_term'].lower() })

        """Deleting dictionary keys that are null"""
        for key in self.components.copy():  #Getting copy of dictionary because the length changes as items are deleted
            if self.components[key] is None:
                del self.components[key]

        return self.components

company_names = ["Cognism (Germany) Ldt.", "Cognism Limited United Kingdom" , "Cognism"]
for company_name in company_names:
    print(
        Namecomponents().get_name_components(company_name)
    )
